# Day 47 — Coverage Intervals and Process Evidence Boundaries

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](coverage_intervals.py)

Day 46 used a boolean source-coverage flag. Day 47 models actual half-open collection intervals [start,end). Adjacent and overlapping intervals can cover an entire investigation window, but even a one-unit gap prevents a complete-coverage conclusion. Missing observations remain NO_POSITIVE_EVIDENCE, never proof of nonexistence. Conflicting parent claims are retained when coverage is complete.

**Questions:** Why must acquisition metadata describe the relevant time window? How might clock uncertainty affect interval boundaries? Why should partial coverage not be confused with a clean system?

Only fictional intervals and parent labels are used. This simplified routine does not measure actual event capture completeness or filter observations by timestamp.

## Run
```bash
python3 labs/47-coverage-intervals-and-process-evidence-boundaries/coverage_intervals.py
```
