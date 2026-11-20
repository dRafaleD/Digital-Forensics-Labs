# Day 43 — Process GUID Correlation and Conflicting Parent Evidence

[English](notes.md) · [Türkçe](notes.tr.md) · [Python exercise](process_guid_demo.py)

## From Day 42
A numeric PID can be reused. A process **GUID** recorded by a telemetry source can help distinguish instances—but it must be treated as observed evidence rather than an unquestionable identity guarantee.

## Model
Every fictional process has a GUID, PID and start time. Each child observation claims a parent GUID and numeric parent PID. The classifier looks for a **single** matching parent GUID and verifies that its PID agrees and its start precedes the child's start.

Outcomes: `PARENT_CANDIDATE`, `CONFLICTING_EVIDENCE` (PID mismatch), `IMPOSSIBLE_ORDER`, `UNKNOWN`, or `AMBIGUOUS` (duplicate source records).

## Run
```bash
python3 labs/43-process-guid-correlation-and-parent-evidence-conflicts/process_guid_demo.py
```

## Questions
1. Why does a GUID help distinguish separate uses of PID 400?
2. Can a forged or malformed telemetry source supply a misleading GUID?
3. Why must a parent start before the child event?
4. Which Sysmon process creation and other independently acquired artifacts could corroborate a lineage?
5. Why is a parent-process relation not proof of a human initiator?

## Boundaries
A small in-memory decision aid, not a parser for real Windows records. Actual GUID provenance, timestamp uncertainty, process lifetime and collection gaps require careful forensic validation.
