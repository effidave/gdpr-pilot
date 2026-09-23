// Runs every fixture through T1-T5 and writes results/baseline/*. With --check, compares
// against expected.json and exits non-zero on any difference (regression tests).
import { readFileSync, readdirSync, writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';
import { Evaluator, relevantMissing, renderTrace, type Fixture, type Rule } from './evaluator.ts';

const here = dirname(fileURLToPath(import.meta.url));
const fixturesDir = join(here, '..', 'fixtures');
const outDir = join(here, '..', 'results', 'baseline');
mkdirSync(outDir, { recursive: true });

const rules: Record<string, Rule> = {};
for (const f of readdirSync(join(here, 'rules')).sort()) Object.assign(rules, parse(readFileSync(join(here, 'rules', f), 'utf8')));

const TESTS: Record<string, string[]> = {
  T1: ['t1_section3', 'micro_or_small_enterprise'],
  T2: ['t2_vlop_status', 'vlop_threshold_met'],
  T3: ['cat1_threshold_met', 'cat1_on_register', 'cat2b_threshold_met', 'cat2b_on_register'],
  T4: ['uk_links', 'limb_5a_significant_uk_users', 'limb_5b_uk_target_market', 'limb_6_material_risk'],
  T5: ['online_platform'],
};
const fmt = (v: any) => (v === true ? 'yes' : v === false ? 'no' : v === null ? 'UNDETERMINED' : v);

const summary: Record<string, Record<string, string>> = {};
for (const file of readdirSync(fixturesDir).filter((f) => f.endsWith('.json')).sort()) {
  const fx: Fixture = JSON.parse(readFileSync(join(fixturesDir, file), 'utf8'));
  const ev = new Evaluator(rules, fx);
  const json: any = { fixture: fx.id, evaluation_date: fx.evaluation_date, tests: {} };
  const text: string[] = [`# ${fx.id} evaluated on ${fx.evaluation_date}`];
  summary[fx.id] = {};
  for (const [t, names] of Object.entries(TESTS)) {
    json.tests[t] = {};
    text.push(`\n## ${t}`);
    for (const name of names) {
      const node = ev.rule(name);
      const missing = [...relevantMissing(node)];
      const result = node.value === null && node.possible ? `UNDETERMINED (one of: ${node.possible.join(' | ')})` : fmt(node.value);
      json.tests[t][name] = { result, relevant_missing: missing, trace: node };
      summary[fx.id][`${t}.${name}`] = result + (missing.length ? `  [needs: ${missing.join(', ')}]` : '');
      text.push(`\n${name} => ${result}${missing.length ? `\n  questions that could change this: ${missing.join(', ')}` : ''}`);
      if (name === names[0]) text.push(renderTrace(node, '  '));
    }
  }
  writeFileSync(join(outDir, `${fx.id}.json`), JSON.stringify(json, null, 2));
  writeFileSync(join(outDir, `${fx.id}.txt`), text.join('\n') + '\n');
}
writeFileSync(join(outDir, 'summary.json'), JSON.stringify(summary, null, 2));

if (process.argv.includes('--check')) {
  const expected: Record<string, Record<string, string>> = JSON.parse(readFileSync(join(here, 'expected.json'), 'utf8'));
  let fails = 0;
  for (const [id, cases] of Object.entries(expected))
    for (const [k, want] of Object.entries(cases)) {
      const got = summary[id]?.[k];
      if (got !== want) { fails++; console.log(`FAIL ${id} ${k}\n  want: ${want}\n  got:  ${got}`); }
    }
  console.log(fails ? `${fails} regression failure(s)` : `all ${Object.values(expected).reduce((n, c) => n + Object.keys(c).length, 0)} expectations pass`);
  process.exit(fails ? 1 : 0);
} else {
  for (const [id, r] of Object.entries(summary)) console.log(`\n${id}\n` + Object.entries(r).map(([k, v]) => `  ${k}: ${v}`).join('\n'));
}
