// Runs every fixture through the L4 encodings with `l4 batch` and writes results/l4/*.
// Usage: L4=/path/to/l4 node rules/run-l4.mjs
import { readFileSync, readdirSync, writeFileSync, mkdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const L4 = process.env.L4 || 'l4';
const fixturesDir = join(here, '..', 'fixtures');
const outDir = join(here, '..', 'results', 'l4');
mkdirSync(join(outDir, 'inputs'), { recursive: true });

const fixtures = readdirSync(fixturesDir).filter((f) => f.endsWith('.json')).sort()
  .map((f) => JSON.parse(readFileSync(join(fixturesDir, f), 'utf8')));

const val = (v) => (v === undefined ? null : v);
const judgement = (fx, name) => {
  const j = fx.judgements?.[name];
  if (!j) return { answer: null, 'decided by': '', reason: 'no judgement given' };
  return { answer: j.value === 'yes' ? true : j.value === 'no' ? false : null, 'decided by': j.decided_by ?? '', reason: j.reason ?? '' };
};

function batch(file, entrypoint, rows, tag) {
  const inPath = join(outDir, 'inputs', `${tag}.json`);
  writeFileSync(inPath, JSON.stringify(rows, null, 2));
  let out;
  try {
    out = execFileSync(L4, ['batch', join(here, file), '--inputs', inPath, '--entrypoint', entrypoint, '--fixed-now', '2026-09-23T12:00:00Z'],
      { cwd: here, encoding: 'utf8', env: { ...process.env } });
  } catch (e) {
    out = e.stdout; // l4 batch exits non-zero if any row errors; keep the NDJSON
  }
  writeFileSync(join(outDir, `${tag}.ndjson`), out);
  return out.trim().split('\n').filter((l) => l.startsWith('{')).map((l) => JSON.parse(l));
}

const results = Object.fromEntries(fixtures.map((f) => [f.id, {}]));
const record = (tag, lines) => lines.forEach((l, i) => { results[fixtures[i].id][tag] = l.status === 'success' ? l.output : { error: l.diagnostics }; });

// T5 first: its result feeds T1.
const t5 = batch('t5-dsa-online-platform.l4', 'is an online platform', fixtures.map((fx) => ({
  'hosting service judgement': judgement(fx, 'hosting_service'),
  'stores user content at request': val(fx.facts.stores_user_content_at_request),
  'dissemination judgement': judgement(fx, 'disseminates_to_the_public'),
  'public posting': val(fx.facts.public_posting),
  'minor ancillary exception': judgement(fx, 'minor_ancillary_exception'),
})), 'T5');
record('T5', t5);

const extract = (line) => {
  // result of the generated `#EVAL CONSIDER decodeArgs ... WHEN RIGHT args THEN JUST (f ...)`
  const r = line.output?.[0]?.result;
  return r;
};

const t1 = batch('t1-dsa-art19.l4', 'Section 3 outcome for', fixtures.map((fx, i) => ({
  'evaluation date': fx.evaluation_date,
  'online platform': t5[i]?.status === 'success' ? unwrapMaybe(extract(t5[i])) : null,
  'designated as VLOP': val(fx.facts.vlop_designated),
  'group staff headcount': val(fx.facts.group_staff_headcount),
  'annual turnover': val(fx.facts.annual_turnover_eur),
  'annual balance sheet total': val(fx.facts.annual_balance_sheet_eur),
  'formerly micro or small': val(fx.facts.formerly_micro_or_small),
  'status lost on': val(fx.facts.micro_small_status_lost_on),
})), 'T1');
record('T1', t1);

const t2 = batch('t2-dsa-art33.l4', 'VLOP status on', fixtures.map((fx) => ({
  'evaluation date': fx.evaluation_date,
  'average monthly active EU recipients': val(fx.facts.eu_monthly_active_recipients),
  'designated as VLOP': val(fx.facts.vlop_designated),
  'notification date': val(fx.facts.vlop_notification_date),
})), 'T2');
record('T2', t2);

const t3 = batch('t3-osa-categories.l4', 'OSA categorisation', fixtures.map((fx) => ({
  'monthly active UK users': val(fx.facts.uk_monthly_active_users),
  'content recommender system': val(fx.facts.content_recommender_system),
  'forward or share functionality': val(fx.facts.forward_or_share_ugc),
  'direct messaging': val(fx.facts.direct_messaging),
  'on register as Category 1': val(fx.facts.ofcom_register_category_1),
  'on register as Category 2B': val(fx.facts.ofcom_register_category_2b),
})), 'T3');
record('T3', t3);

const t4rows = fixtures.map((fx) => ({
  'significant number of UK users': judgement(fx, 'significant_number_of_uk_users'),
  'UK is a target market': judgement(fx, 'uk_target_market'),
  'capable of use in the UK': val(fx.facts.capable_of_use_in_uk),
  'material risk of significant harm': judgement(fx, 'material_risk_of_significant_harm_uk'),
}));
record('T4', batch('t4-osa-uk-links.l4', 'has links with the UK', t4rows, 'T4'));
record('T4 limbs', batch('t4-osa-uk-links.l4', 'satisfied limbs', t4rows, 'T4-limbs'));

// The batch wrapper returns JUST (result) on a good decode and NOTHING on a decode
// failure, so a MAYBE result arrives double-wrapped. Unwrap one level.
function unwrapMaybe(r) {
  if (r && typeof r === 'object' && 'JUST' in r) return unwrapMaybe1(r.JUST);
  return r;
}
function unwrapMaybe1(r) {
  if (r === null || r === undefined) return null;
  if (typeof r === 'object' && 'JUST' in r) return r.JUST;
  if (r === 'NOTHING' || (typeof r === 'object' && 'NOTHING' in r)) return null;
  return r;
}

writeFileSync(join(outDir, 'summary.json'), JSON.stringify(results, null, 2));
console.log(JSON.stringify(results, null, 1));
