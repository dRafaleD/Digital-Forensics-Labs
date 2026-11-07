# Day 31 — Clock Skew and Timeline Uncertainty

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](clock_skew_demo.py)

## Learning objective

Learn the trust and evidence boundaries of **Clock Skew and Timeline Uncertainty** using harmless local fixtures.

## Core concepts

1. Events observed on different hosts can have different clock offsets even if all are written in UTC.

2. Document observed timestamp, known correction and confidence; never silently change source evidence.

3. Overlapping uncertainty intervals do not establish which event happened first; reports should mark the order as inconclusive.

## Safe hands-on

Read the code and predict its output before running:

```bash
python clock_skew_demo.py
```

Output is synthetic; no operations are sent to a live target.

## Assignments

1. Identify input provenance and untrusted fields.
2. Add and test a negative or boundary case.
3. Separate direct observations from interpretations.
4. Describe additional validation needed in a real environment.

## Knowledge check

- Is any single indicator sufficient?
- What can cause false positives or missing evidence?
- What inputs are needed to reproduce the result?

## Safety and limitations

No live malware, cloud accounts, system modifications, or outbound traffic. This minimal model is not an exact platform implementation.
