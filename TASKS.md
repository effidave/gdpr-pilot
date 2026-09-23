# Tasks

Follow-up items noticed while working in this project, outside whatever the current focus was.
Check off items once they're done - nothing gets deleted, it just moves to Done.

## Open

- [ ] Verify every UNVERIFIED legal quote in `l4-spike/rules/*.l4` and `l4-spike/baseline/rules/*.yaml` against legislation.gov.uk (OSA 2023 s.4, s.95; SI 2025/226) and EUR-Lex (DSA Arts 3, 19, 24(3), 33, Recital 14; Rec 2003/361/EC), and update the rules and REPORT.md section 4 if the text differs
      *(from: L4 spike - primary sources were blocked from the cloud environment - 2026-09-23)*
- [ ] Decide whether Commission VLOP designation settles online-platform status (T1/T5), and whether to model Rec 2003/361/EC Annex Art 4(2) (two consecutive periods) and the linked/partner headcount aggregation
      *(from: L4 spike - disagreements with the brief's section 6 - 2026-09-23)*
- [ ] Test the L4 decision service (`jl4-service` REST route and query-plan endpoint) and the `jl4-wasm` in-browser build, which the spike did not get to
      *(from: L4 spike - integration criterion - 2026-09-23)*
- [ ] Raise with Legalese: `l4 batch` wrapper fails when a MAYBE parameter precedes another; a failing `#ASSERT` exits 0; `l4 run` never captures `#EVALTRACE` traces; `@ref` does not reach traces or output; status of RUNTIME-INPUT-STATE-SPEC / TYPICALLY
      *(from: L4 spike - blockers found in l4-ide 48fb400 - 2026-09-23)*

## Done
