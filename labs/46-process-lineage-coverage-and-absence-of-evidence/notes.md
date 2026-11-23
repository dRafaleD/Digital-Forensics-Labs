# Day 46 — Process-Lineage Coverage and Absence of Evidence

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python](coverage_demo.py)

## After Day 45
The previous lab distinguished **independent sensor origins** from mere relays. Today we add **coverage metadata**. If a source did not collect events at the relevant time, its silence must not be interpreted as evidence that the parent process did not exist.

## Model
An examiner-controlled registry maps collectors to original telemetry sources. Separate coverage metadata records whether each origin was collecting relevant events. The toy classifier recognizes corroborating parent GUID observations, contradictory parent claims, invalid parent/child chronology and uncovered periods.

- `CORROBORATED_CONTEXT`: two distinct registered and covered origins report the same parent.
- `SINGLE_ORIGIN`: one covered origin supports a hypothesis.
- `LIMITED_COVERAGE`: at least one required source has no relevant coverage.
- `NO_POSITIVE_EVIDENCE`: no admissible supporting observation; **not** proof of absence.
- Conflict labels flag contradictory or impossible claims.

## Reproduce
```bash
python3 labs/46-process-lineage-coverage-and-absence-of-evidence/coverage_demo.py
```

## Questions
Why is silence from an offline sensor not evidence against an event? Why do two relays not imply two independent witnesses? Why is a complete capture still insufficient to prove an initiating human? How would clock uncertainty and source compromise alter the conclusion?

## Limits
All records and coverage flags are invented. Real collection completeness and provenance require acquisition logs, trustworthy clock context and independent corroboration.
