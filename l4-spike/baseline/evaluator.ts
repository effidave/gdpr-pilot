// Minimal three-valued (Kleene) rules evaluator - a measuring stick for the L4 spike.
// Rules are YAML; facts and judgements come from fixture JSON. A missing fact is
// UNDETERMINED, never false.

export type TV = true | false | null; // null = UNDETERMINED
export type Scalar = number | string | boolean | null;

export interface Cite { instrument: string; pinpoint: string; version: string; text: string; verified?: boolean }
export interface Judgement { value: 'yes' | 'no' | 'undetermined'; decided_by?: string; decided_on?: string; reason?: string }
export interface Fixture { id: string; evaluation_date: string; facts: Record<string, Scalar>; judgements: Record<string, Judgement> }
export interface Rule { label: string; cite?: Cite; expr?: any; outcomes?: { when: any; result: string }[]; otherwise?: string }

export interface Node {
  kind: string;
  label: string;
  value: TV | Scalar | string;
  cite?: Cite;
  source?: string; // e.g. "fact", "judgement by X: reason"
  missing?: string; // name of the fact/judgement that was missing
  children: Node[];
  possible?: string[]; // outcome tables: outcomes still possible
}

const show = (v: any) => (v === null || v === undefined ? 'UNDETERMINED' : typeof v === 'boolean' ? (v ? 'TRUE' : 'FALSE') : String(v));

export function addMonths(iso: string, n: number): string {
  const d = new Date(iso + 'T00:00:00Z');
  const day = d.getUTCDate();
  d.setUTCDate(1);
  d.setUTCMonth(d.getUTCMonth() + n);
  const last = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() + 1, 0)).getUTCDate();
  d.setUTCDate(Math.min(day, last));
  return d.toISOString().slice(0, 10);
}

const CMP: Record<string, (a: any, b: any) => boolean> = {
  gt: (a, b) => a > b, gte: (a, b) => a >= b, lt: (a, b) => a < b, lte: (a, b) => a <= b, eq: (a, b) => a === b,
};
const CMP_WORD: Record<string, string> = { gt: 'more than', gte: 'at least', lt: 'less than', lte: 'at most', eq: 'equals' };

export class Evaluator {
  private memo = new Map<string, Node>();
  private rules: Record<string, Rule>;
  private fx: Fixture;
  constructor(rules: Record<string, Rule>, fx: Fixture) { this.rules = rules; this.fx = fx; }

  rule(name: string): Node {
    const hit = this.memo.get(name);
    if (hit) return hit;
    const r = this.rules[name];
    if (!r) throw new Error(`unknown rule: ${name}`);
    const node = r.outcomes ? this.outcomeTable(name, r) : this.expr(r.expr);
    const out: Node = { kind: 'rule', label: `${name}: ${r.label}`, value: node.value, cite: r.cite, children: r.outcomes ? node.children : [node], possible: node.possible };
    this.memo.set(name, out);
    return out;
  }

  // First matching row wins. An UNDETERMINED row before the first TRUE row
  // means the result is undetermined between the rows still possible.
  private outcomeTable(name: string, r: Rule): Node {
    const children: Node[] = [];
    const possible: string[] = [];
    let matched = false;
    for (const row of r.outcomes!) {
      const c = this.expr(row.when);
      children.push({ kind: 'when', label: `if -> "${row.result}"`, value: c.value, children: [c] });
      if (c.value !== false) possible.push(row.result);
      if (c.value === true) { matched = true; break; }
    }
    if (!matched) possible.push(r.otherwise!);
    const result = possible.length === 1 ? possible[0] : null;
    return { kind: 'outcomes', label: name, value: result, children, possible: result === null ? possible : undefined };
  }

  private operand(o: any): Node {
    if (o && typeof o === 'object') {
      if ('fact' in o) {
        const v = this.fx.facts[o.fact];
        const known = v !== undefined && v !== null;
        return { kind: 'fact', label: o.fact, value: known ? v : null, source: 'fact', missing: known ? undefined : o.fact, children: [] };
      }
      if ('var' in o) return { kind: 'var', label: o.var, value: (this.fx as any)[o.var] ?? null, children: [] };
      if ('add_months' in o) {
        const [base, n] = o.add_months;
        const b = this.operand(base);
        return { kind: 'calc', label: `${b.label} + ${n} months`, value: b.value === null ? null : addMonths(String(b.value), n), children: [b] };
      }
    }
    return { kind: 'literal', label: String(o), value: o, children: [] };
  }

  expr(e: any): Node {
    if (typeof e === 'string') return this.expr({ ref: e });
    if ('ref' in e) return this.rule(e.ref);
    if ('fact' in e) {
      const n = this.operand(e);
      if (n.value !== null && typeof n.value !== 'boolean') throw new Error(`fact ${e.fact} is not boolean`);
      return n;
    }
    if ('judgement' in e) {
      const j = this.fx.judgements?.[e.judgement];
      const value: TV = j?.value === 'yes' ? true : j?.value === 'no' ? false : null;
      const source = j ? `judgement "${j.value}" by ${j.decided_by ?? '?'}${j.reason ? ': ' + j.reason : ''}` : 'judgement not given';
      return { kind: 'judgement', label: e.judgement, value, source, missing: value === null ? e.judgement : undefined, children: [] };
    }
    if ('not' in e) {
      const c = this.expr(e.not);
      return { kind: 'not', label: 'NOT', value: c.value === null ? null : !c.value, children: [c] };
    }
    if ('all' in e || 'any' in e) {
      const isAll = 'all' in e;
      const cs: Node[] = (isAll ? e.all : e.any).map((x: any) => this.expr(x));
      const vals = cs.map((c) => c.value);
      const decisive = isAll ? false : true;
      const value: TV = vals.includes(decisive) ? decisive : vals.includes(null) ? null : !decisive;
      return { kind: isAll ? 'all' : 'any', label: isAll ? 'ALL of' : 'ANY of', value, children: cs };
    }
    if ('yes_if' in e) {
      const c = this.expr(e.yes_if);
      return { kind: 'yes_if', label: 'YES IF (otherwise undetermined)', value: c.value === true ? true : null, children: [c] };
    }
    if ('coalesce' in e) {
      const cs: Node[] = e.coalesce.map((x: any) => this.expr(x));
      const first = cs.find((c) => c.value !== null);
      return { kind: 'coalesce', label: 'FIRST KNOWN of', value: first ? first.value : null, children: cs };
    }
    const op = Object.keys(CMP).find((k) => k in e);
    if (op) {
      const [a, b] = e[op].map((x: any) => this.operand(x));
      const value: TV = a.value === null || b.value === null ? null : CMP[op](a.value, b.value);
      return { kind: 'cmp', label: `${a.label} (${show(a.value)}) ${CMP_WORD[op]} ${b.label}`, value, children: [a, b] };
    }
    throw new Error(`bad expression: ${JSON.stringify(e)}`);
  }
}

// Facts whose answer could change an UNDETERMINED result: leaves reachable from
// the root through UNDETERMINED nodes only (sound for Kleene logic, because an
// UNDETERMINED node has no child that already decides it).
export function relevantMissing(n: Node, acc = new Set<string>()): Set<string> {
  if (n.value !== null) return acc;
  if (n.missing) acc.add(n.missing);
  for (const c of n.children) if (c.value === null) relevantMissing(c, acc);
  return acc;
}

export function renderTrace(n: Node, indent = ''): string {
  const mark = n.value === true ? '[YES]' : n.value === false ? '[NO] ' : n.value === null ? '[?]  ' : `[${n.value}]`;
  let line = `${indent}${mark} ${n.label}`;
  if (n.possible) line += `  (still possible: ${n.possible.join(' | ')})`;
  if (n.source && n.kind === 'judgement') line += `  <- ${n.source}`;
  if (n.kind === 'fact') line += n.missing ? '  <- MISSING FACT' : `  = ${show(n.value)}`;
  if (n.cite) line += `\n${indent}      cite: ${n.cite.instrument}, ${n.cite.pinpoint} (${n.cite.version})${n.cite.verified === false ? ' [text UNVERIFIED]' : ''}`;
  return [line, ...n.children.filter((c) => c.kind !== 'literal').map((c) => renderTrace(c, indent + '   '))].join('\n');
}
