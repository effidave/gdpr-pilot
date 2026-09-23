# L4 evaluation spike - report

Evaluation date for all runs: 2026-09-23. Everything referenced below is in this folder.

> **Legal text caveat.** legislation.gov.uk and EUR-Lex were blocked from the spike environment (see section 5). Every quoted provision in `rules/*.l4` and `baseline/rules/*.yaml` is from the author's knowledge and is marked UNVERIFIED. The disagreements in section 4 rest on that text and must be checked against the primary sources before anyone relies on them.

## 1. Verdict

**Build the bespoke three-valued evaluator as the engine. Don't adopt L4 as the rule layer for phase 1. Re-evaluate L4 when its planned "runtime input state" work ships.**

L4 is well engineered: a strong type checker, clear error messages, good rendering for lawyers, and a serious query planner and decision service. But on the criterion the brief calls critical, idiomatic L4 gets unknowns wrong:

- Plain `BOOLEAN` and `NUMBER` inputs cannot represent "unknown" at all.
- The prelude's comparisons on `MAYBE NUMBER` return `FALSE` when the value is missing. With unknown UK users, the Category 2B threshold comes out "not met", with no warning (`results/l4/probes/naive-run.txt`, probe E).

I got correct three-valued behaviour out of L4 only by writing my own Kleene logic library (`rules/kleene.l4`) and using `MAYBE BOOLEAN` throughout. That encoding gave the same answers as the baseline on all 10 fixtures, but it costs most of what L4 offers:

- The query planner refuses non-BOOLEAN decisions.
- The rendered prose gets harder to read.
- `l4 batch` could not accept the resulting function signatures because of a wrapper bug.

The bespoke baseline did the whole job in 218 lines of TypeScript. It traces each result with citations and names the missing facts that could change it, it runs in a browser with no server, and it passed its regression suite. The citation and unknowns layer is the part we need to own in either design, and it is the part L4 does not provide.

A hybrid ("L4 for authoring, our own layer for unknowns and citations") is possible later, e.g. by compiling `l4 ast` output into our evaluator. It isn't worth the cost now, because the parts of L4 we would keep (the planner and the readable rendering) are the parts that break under a three-valued encoding.

## 2. Scorecard

Scores are 1 (poor) to 5 (strong). "L4 (tri)" means L4 with my Kleene library; "idiomatic" means the documented style.

| # | Criterion | L4 | Baseline | Evidence |
|---|---|---|---|---|
| 1 | **Unknown handling** (critical) | **2** | **5** | Idiomatic L4: `MAYBE NUMBER` comparisons return FALSE on NOTHING (prelude `__GT__` etc.). Probe E: unknown UK users gives "2B threshold met = FALSE"; probe C: unknown staff gives "Section 3 applies = TRUE". Plain types reject missing input loudly, which is safe but can't express unknown. L4 (tri) handled all 5 variants correctly, but only with 140 lines of hand-built logic. Baseline: correct by construction (section 3). |
| 2 | **Relevant questions** | 3 | 4 | L4's planner (`:qp`) does real three-valued partial evaluation and ranks the questions still needed (`results/l4/probes/queryplan.txt`), but: (a) BOOLEAN decisions only, so it can't run on the tri encoding (`queryplan-tri.txt`); (b) it rejects numeric bindings (`users=2500000`), so it cannot see that 2.5m settles both OSA limbs (the S4 case); (c) the REPL can't address backtick names with spaces. Baseline lists the missing facts that could change each result (e.g. S2-U: `group_staff_headcount`), but doesn't rank them. |
| 3 | **Explanation trace** | 2 | 4 | L4 traces are evaluation traces: they show `CONSIDER`, `<function>`, `IF a THEN FALSE ELSE TRUE` (`results/l4/traces/repl-traceascii.txt`). They are only available through the REPL and `l4 trace`; `l4 run` always prints "no trace captured". Baseline trace: see section 3. |
| 4 | **Citations** | 1 | 4 | L4's `@ref` / `@ref-map` are clickable editor links only (`jl4-core/src/L4/Citations.hs`). They don't reach the evaluator, the traces, the JSON output or the rendered text, and `@ref-src` (CSV) has been removed. Quoted text and version can only go in comments. Baseline: a `cite` block (instrument, pinpoint, version, text, verified) on every rule, printed at each node of the trace. |
| 5 | **Judgement inputs** | 3 | 4 | L4: a `Judgement` record (answer, decided by, reason) typed and decoded from JSON without trouble, but the provenance never shows in any output. Baseline: judgements carry `decided_by` and `reason`, which appear in the trace. |
| 6 | **Time and versions** | 3 | 2 | L4 has DATE types and a date library, but no "add months", so I wrote one (no end-of-month clamping). Both get the Art 33(6) four months and the Art 19 twelve-month grace right (S3-D). Neither has thresholds that change over time or rule versions. |
| 7 | **Lawyer readability** | 4 (plain) / 3 (tri) | 3 | `l4 render` turns plain L4 into clean bullets (`results/l4/render/naive.txt`). With the tri encoding the helpers leak into the prose ("any of list of limb 5(a) with the judgement ..."). YAML is readable but less natural. See the rule quoted in section 3. |
| 8 | **Integration** | 3 | 4 | L4: REST/OpenAPI/MCP service and JSON batch exist, and a WASM build exists (not tested). Problems found: the `l4 batch` wrapper fails to parse when a MAYBE parameter comes before another (`rules/probes/batchbug.l4`); records come back as positional arrays without field names; a row that fails to decode reports `"status":"success"`; and it takes about 10 seconds per row (70 rows in 12 minutes). Baseline: plain TypeScript, runs in a browser or Node, and facts never leave the machine. There's no schema or REST out of the box. |
| 9 | **Tests** | 3 | 4 | L4: `#ASSERT` in the language is pleasant (`rules/scenarios.l4`, 17 assertions pass), but **a failing `#ASSERT` still exits 0**, so CI needs output parsing. `rules/run-l4.mjs --check` wraps batch as a regression runner. Baseline: `npm test`, 130 expectations, exits 1 on failure (checked with a planted failure). |
| 10 | **Effort and friction** | 2 | 5 | Measured wall-clock time in this spike: L4 took 30 minutes from clone to working binaries (a source build via Nix, since every packaged route was blocked, and one locale failure; section 5). Writing the five rules then took several type-check rounds, each fixing a syntax rule the docs don't make obvious (comma-separated `LIST`, `GIVEN` order must match the definition, layout). Type errors are excellent: they name the mismatch and the fix. CLI output is noisy with LSP "Info" diagnostics. Baseline: about 20 minutes for the evaluator, rules and runner, with no install. |

## 3. Unknown-handling findings

**Missing-fact variants** (the full output is in `results/baseline/*.txt` and `results/l4/summary.json`). "L4 (tri)" and the baseline gave identical results in every case.

| Variant | Expected | Baseline and L4 (tri) output | Idiomatic L4 |
|---|---|---|---|
| S2-U: staff unknown | enterprise size undetermined; names staff count | `micro_or_small_enterprise => UNDETERMINED [needs: group_staff_headcount]`. L4: `T1 enterprise size: null`. T1 overall is still `Not relevant: not an online platform`, which is correct: S2 fails T5 whatever its size. | Probe B: `small enterprise = FALSE`. Probe C: `Section 3 applies = TRUE`. **Silent default.** |
| S3-U: designation unknown | "threshold met, designation unknown" | `vlop_threshold_met => yes`. T2 `UNDETERMINED (one of: Threshold met, not designated \| Designated, obligations not yet applicable \| Designated, obligations applicable) [needs: vlop_designated, vlop_notification_date]` | A BOOLEAN `designated` cannot be omitted, so the batch run errors. |
| S3-D: designated 2026-08-01 | not yet applicable | `Designated, obligations not yet applicable` (applicable from 2026-12-01) | n/a |
| S1-U: significant users undetermined | T4 yes via target market | `uk_links => yes`. L4 `T4 limbs: s.4(5)(b) UK is a target market` | n/a |
| S4: 2.5m users, resharing unknown | firm "not met" for 1 and 2B | `cat1_threshold_met => no`, `cat2b_threshold_met => no`, `cat1_on_register => UNDETERMINED [needs: ofcom_register_category_1]` | Probe E with users unknown gives **FALSE** (wrongly "not met"). L4's planner cannot take `users=2500000` at all. |

**The quiet false.** `jl4-core/libraries/prelude.l4` defines `__GEQ__`, `__LEQ__`, `__LT__` and `__GT__` on `MAYBE NUMBER` as `WHEN NOTHING THEN FALSE`. That's what a lawyer gets by writing `users GREATER THAN JUST 3000000`. L4's own design docs describe the fix (`specs/todo/RUNTIME-INPUT-STATE-SPEC.md`: four input states and a TriBool resolution), but it is marked **BLOCKED** because the `TYPICALLY` default feature it depends on was reverted.

**Baseline trace, S3-U T2** (this is the trace a non-lawyer would read):

```
t2_vlop_status => UNDETERMINED (one of: Threshold met, not designated | Designated, obligations not yet applicable | Designated, obligations applicable)
  questions that could change this: vlop_designated, vlop_notification_date
  [?]   t2_vlop_status: VLOP status on the evaluation date
        cite: Regulation (EU) 2022/2065 (Digital Services Act), Art 33(1), (4), (6) (OJ L 277, 27.10.2022 (original text)) [text UNVERIFIED]
     [NO]  if -> "Threshold not met"
        [NO]  NOT
           [YES] vlop_threshold_met: Average monthly active recipients in the Union are 45 million or more
                 cite: ... Art 33(1) ...
              [YES] eu_monthly_active_recipients (50000000) at least 45000000
     [?]   if -> "Threshold met, not designated"
        [?]   NOT
           [?]   vlop_designated  <- MISSING FACT
     [?]   if -> "Designated, obligations not yet applicable"
        [?]   evaluation_date (2026-09-23) less than vlop_notification_date + 4 months
              [?]   vlop_notification_date  <- MISSING FACT
```

**The same evaluation in L4** (REPL `:traceascii`; the excerpt is the designation step):

```
│││┌ PAIR OF (not OF `designated as VLOP`), `Threshold met, not designated`
││││┌ not OF `designated as VLOP`
│││││┌ not
│││││└ <function>
││││├ CONSIDER x WHEN JUST b THEN JUST OF (NOT b),
│││││              WHEN NOTHING THEN NOTHING
││││├ NOTHING
```

**Lawyer readability: one rule in each system.** A lawyer could check the Category 1 threshold in either. The L4 plain form, as rendered, reads:

```
• Category 2B threshold met (plain) holds if:
    all of the following are true:
    - monthly active UK users is more than 3,000,000
    - direct messaging
```

The same rule in the baseline YAML:

```yaml
cat2b_threshold_met:
  expr:
    all:
      - gt: [ { fact: uk_monthly_active_users }, 3000000 ]
      - { fact: direct_messaging }
```

## 4. Disagreements with section 6

1. **S1 and S3, T5 "online platform: Yes".** The brief makes the Art 3(i) ancillary exception a judgement that is always input, and gives no answer for S1 or S3, so both engines return **undetermined** and ask for `minor_ancillary_exception`. With the exception answered "no" (my added fixtures S1-J and S3-J), both return yes. This carries into T1: S1 is "not relevant or does not apply (micro)", and S3 is "not relevant or applies (VLOP)". For S3 one could argue that Commission designation under Art 33(4) settles online-platform status. I haven't encoded that; it is a policy choice to make.
2. **S3, T4 "Yes".** No s.4(5)-(6) judgements were given for S3. Since the brief says never to derive judgements from numbers, 20m UK users doesn't settle "significant number", and the result is **undetermined** (it asks for all three limbs). S3-J answers them and gets yes.
3. **S3, T2 "applicable from 2026-07-01".** Art 33(6) runs "from four months after the notification to the provider concerned referred to in paragraph 5", not from the designation decision. The fixtures assume notification on the designation date and say so; the rule takes the notification date as its input.
4. **S2, T2 "Not relevant".** Both engines report "Threshold not met" (2m is below 45m), because T2 doesn't check platform status. The substance is the same.
5. **S2-U expectation.** "Anything depending on enterprise size is undetermined" holds for the size test itself. But T1 as a whole is correctly settled as "not relevant", because S2 is not an online platform. That is the engine working as intended, not a failure.
6. **Enterprise size (T1).** Rec 2003/361 Annex Art 2 uses "turnover **and/or** balance sheet", so either financial ceiling is enough; it's encoded as `any`. Two points to flag:
   - Annex Art 4(2): status is only gained or lost after the ceilings are crossed in **two consecutive accounting periods**. S2's 60 staff may still leave it "small" if that's the first year over 50. Art 4(2) is not modelled.
   - Linked and partner enterprises (Annex Arts 3 and 6): group headcount is an input fact, not computed. The aggregation rules (100% for linked, pro rata for partners) need their own rule if we want the engine to compute them.
7. **OSA register date (10 July 2026).** I couldn't check this; the rules treat register entry as an input fact.

## 5. Blockers and workarounds

| Blocker | What happened | Workaround |
|---|---|---|
| Primary legal sources | legislation.gov.uk, EUR-Lex and data.europa.eu were blocked by the environment's network policy, for curl and web fetch alike | Quoted from knowledge, marked UNVERIFIED everywhere. **Needs checking.** |
| VS Code extension / Claude Code plugin | Marketplace, Open VSX and GitHub releases blocked; no VS Code; `/plugin marketplace add` is a user slash command | Not tested |
| Web editor and docs site | jl4.legalese.com and legalese.com blocked | Used the repo's `doc/` and `skills/writing-l4-rules/` instead |
| GHCup blocked; apt has GHC 9.4.7 | L4 needs GHC 9.10 | Nix 2.28.3 installed from releases.nixos.org; GHC 9.10.3 and cabal 3.16 from the Nix cache using the nixpkgs revision pinned in `flake.lock` |
| Build failed at 64/66 modules | Template Haskell reading `excel-date.l4` failed under a non-UTF-8 locale (`invalid argument (cannot decode byte sequence)`) | `LANG=C.UTF-8`. The error message doesn't point to the fix. |
| `l4 batch` with MAYBE parameters | The generated wrapper `a IS MAYBE OF NUMBER` followed by `, b IS ...` gives a layout error (`rules/probes/batchbug.l4`) | `rules/api.l4`: one record parameter per entry point |
| `l4 run` traces | Always prints "no trace captured", even with `#EVALTRACE` and `--trace full` | REPL `:traceascii` and `l4 trace --format dot` |
| `#ASSERT` failure exits 0 | Can't be used as a CI gate as is | Batch-based `run-l4.mjs --check` |
| REPL `:qp` | Can't address names with spaces | Plain-identifier copy in `rules/probes/queryplan.l4` |
| Imports | Only resolve from the importing file's folder; a missing import also reports "Your module depends on itself" | Put the scenario tests beside the rules |
| `jl4-service` | Started building at the end of the day; not finished in time | Not tested live. Its source (`Backend/Jl4.hs`) maps missing or null MAYBE parameters to NOTHING and rejects missing non-MAYBE parameters. |

## 6. Versions used

- **l4-ide:** `legalese/l4-ide` at `48fb400d8cfe25dc1a74c23b2b9407986a014119` (2026-09-23, "Merge pull request #462"). Built from source with `cabal build exe:l4 exe:jl4-repl`; Hackage index as of 2026-09-23.
- **Toolchain:** GHC 9.10.3 (the repo asks for 9.10.2); cabal-install 3.16.0.0; Nix 2.28.3, single-user; nixpkgs `a8d610af3f1a5fb71e23e08434d8d61a466fc942`; GraphViz 2.43.0 (apt).
- **Baseline:** Node.js 22.22.2 with built-in TypeScript type stripping; `yaml` 2.9.1.
- **OS:** Ubuntu 24.04 container.

## 7. Recommended next step

1. **Verify the law.** Check every UNVERIFIED quote against legislation.gov.uk and EUR-Lex, and settle the disagreements in section 4 (especially whether VLOP designation settles online-platform status, and Annex Art 4(2)).
2. **Turn the baseline into the phase-1 engine core.** Keep the three-valued semantics and the `cite` blocks. Add:
   - rule versions with in-force dates;
   - a JSON Schema for facts, generated from the rules;
   - ranking of the missing facts that could change a result;
   - a numeric-aware "could this still change?" check, so S4-style cases are settled from ranges.
3. **Ask Legalese about the unknowns work.** Ask about the status and timeline of `RUNTIME-INPUT-STATE-SPEC` and `TYPICALLY`, a fix for the batch MAYBE wrapper and the `#ASSERT` exit code, and whether `@ref` can flow into traces. If three-valued inputs and citations in traces ship, re-run this spike (the fixtures and runners are reusable) and consider L4 as an authoring front end that compiles into our engine.

---

**How to reproduce.** Baseline: `cd baseline && npm install && npm test`. L4: build l4-ide as in section 6, then `export L4=<path to l4> JL4_LIBRARY_PATH=<l4-ide>/jl4-core/libraries LANG=C.UTF-8`. Run `$L4 check rules/t1-dsa-art19.l4` (and the others), `$L4 run rules/scenarios.l4`, and `node rules/run-l4.mjs --check`.
