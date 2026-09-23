// Runs every fixture through the L4 encodings (api.l4) with `l4 batch` and writes results/l4/*.
// Usage: L4=/path/to/l4 JL4_LIBRARY_PATH=... node rules/run-l4.mjs [--check]
import { readFileSync, readdirSync, writeFileSync, mkdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const L4 = process.env.L4 || 'l4';
const fixturesDir = join(here, '..', 'fixtures');
const outDir = join(here, '..', 'results', 'l4');
mkdirSync(outDir, { recursive: true });

const fixtures = readdirSync(fixturesDir).filter((f) => f.endsWith('.json')).sort()
  .map((f) => JSON.parse(readFileSync(join(fixturesDir, f), 'utf8')));

// Unknown facts are sent as JSON null (decoded to NOTHING).
const v = (x) => (x === undefined ? null : x);
const judgement = (fx, name) => {
  const j = fx.judgements?.[name];
  if (!j) return { answer: null, 'decided by': '', reason: 'no judgement given' };
  return { answer: j.value === 'yes' ? true : j.value === 'no' ? false : null, 'decided by': j.decided_by ?? '', reason: j.reason ?? '' };
};
const toRow = (fx) => ({ s: {
  'evaluation date': fx.evaluation_date,
  'monthly active UK users': v(fx.facts.uk_monthly_active_users),
  'average monthly active EU recipients': v(fx.facts.eu_monthly_active_recipients),
  'group staff headcount': v(fx.facts.group_staff_headcount),
  'annual turnover': v(fx.facts.annual_turnover_eur),
  'annual balance sheet total': v(fx.facts.annual_balance_sheet_eur),
  'formerly micro or small': v(fx.facts.formerly_micro_or_small),
  'status lost on': v(fx.facts.micro_small_status_lost_on),
  'stores user content at request': v(fx.facts.stores_user_content_at_request),
  'public posting': v(fx.facts.public_posting),
  'direct messaging': v(fx.facts.direct_messaging),
  'content recommender system': v(fx.facts.content_recommender_system),
  'forward or share functionality': v(fx.facts.forward_or_share_ugc),
  'capable of use in the UK': v(fx.facts.capable_of_use_in_uk),
  'designated as VLOP': v(fx.facts.vlop_designated),
  'notification date': v(fx.facts.vlop_notification_date),
  'on register as Category 1': v(fx.facts.ofcom_register_category_1),
  'on register as Category 2B': v(fx.facts.ofcom_register_category_2b),
  'significant number of UK users': judgement(fx, 'significant_number_of_uk_users'),
  'UK is a target market': judgement(fx, 'uk_target_market'),
  'material risk of significant harm': judgement(fx, 'material_risk_of_significant_harm_uk'),
  'hosting service judgement': judgement(fx, 'hosting_service'),
  'dissemination judgement': judgement(fx, 'disseminates_to_the_public'),
  'minor ancillary exception': judgement(fx, 'minor_ancillary_exception'),
} });

const inputsPath = join(outDir, 'inputs.json');
writeFileSync(inputsPath, JSON.stringify(fixtures.map(toRow), null, 2));

// Plain-text rendering of an L4 result value as returned by `l4 batch`.
function show(r) {
  if (r === null || r === undefined) return 'null';
  if (typeof r !== 'object') return String(r);
  if (Array.isArray(r)) return r.map(show).join(' | ');
  if ('error' in r) return `ERROR: ${String(r.error).trim()}`;
  return JSON.stringify(r);
}

const ENTRYPOINTS = ['T1', 'T1 enterprise size', 'T2', 'T3', 'T4', 'T4 limbs', 'T5'];
const summary = Object.fromEntries(fixtures.map((f) => [f.id, {}]));
for (const ep of ENTRYPOINTS) {
  let out;
  try {
    out = execFileSync(L4, ['batch', join(here, 'api.l4'), '--inputs', inputsPath, '--entrypoint', ep, '--fixed-now', '2026-09-23T12:00:00Z'],
      { cwd: here, encoding: 'utf8', maxBuffer: 64 << 20 });
  } catch (e) { out = e.stdout ?? ''; }
  writeFileSync(join(outDir, `${ep.replace(/ /g, '-')}.ndjson`), out);
  const lines = out.trim().split('\n').filter((l) => l.startsWith('{')).map((l) => JSON.parse(l));
  lines.forEach((l, i) => {
    summary[fixtures[i].id][ep] = l.status === 'success' ? show(l.output?.[0]?.result) : `BATCH ERROR: ${JSON.stringify(l.diagnostics).slice(0, 300)}`;
  });
}
writeFileSync(join(outDir, 'summary.json'), JSON.stringify(summary, null, 2));

if (process.argv.includes('--check')) {
  const expected = JSON.parse(readFileSync(join(here, 'expected-l4.json'), 'utf8'));
  let fails = 0, n = 0;
  for (const [id, cases] of Object.entries(expected)) for (const [k, want] of Object.entries(cases)) {
    n++;
    if (summary[id]?.[k] !== want) { fails++; console.log(`FAIL ${id} ${k}\n  want: ${want}\n  got:  ${summary[id]?.[k]}`); }
  }
  console.log(fails ? `${fails} regression failure(s)` : `all ${n} expectations pass`);
  process.exit(fails ? 1 : 0);
} else {
  for (const [id, r] of Object.entries(summary)) console.log(`\n${id}\n` + Object.entries(r).map(([k, x]) => `  ${k}: ${x}`).join('\n'));
}
