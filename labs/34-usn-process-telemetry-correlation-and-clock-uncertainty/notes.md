# Day 34 — Correlating USN and Process-File Telemetry with Clock Uncertainty

[English](notes.md) · [Türkçe](notes.tr.md) · [Synthetic correlator](correlate_demo.py)

## Why correlation is harder than matching timestamps
Day 33 studied NTFS `$UsnJrnl` change records, which describe filesystem activity but **do not directly identify the initiating process or actor**. A defender might also collect process/file-operation telemetry. Can two records close in time be linked? Possibly—but **temporal proximity alone is not causation**.

## Treat each source as separate evidence
Our invented dataset has:
- **USN-like records:** file reference, timestamp, change reason and evidence ID. No actor field.
- **Process-file telemetry:** separate event IDs, a claimed process label and a **fabricated common file reference**. Real tools may instead expose a path, process GUID, hash or other fields; your correlation method must reflect actual source semantics.
- **Clock tolerance:** `±2 seconds` is an illustrative uncertainty window. Real offsets should be estimated from time synchronization and acquisition evidence, not chosen merely to force a match.

The code searches for process-file candidates that share the synthetic object reference and fall within the chosen time window. It explicitly distinguishes:
- **No candidate** — records do not establish an initiator.
- **One candidate** — a possible association, **not a proven actor**.
- **Multiple candidates** — ambiguous; preserve conflicting possibilities.

## Run locally
```bash
python3 correlate_demo.py
```
The dataset produces one ambiguous correlation, one record without a candidate, and one single temporal candidate. Assertions verify all three. The script neither reads a Windows volume nor collects actual logs.

## Investigation
1. Why should `USN` order not be treated as a wall-clock timestamp?
2. What would happen if one device's clock were 90 seconds ahead?
3. What additional evidence could connect a process to a particular file write rather than merely a nearby event?
4. Explain why `filename` alone is a weaker join key than a properly scoped file identifier.
5. Design a report with source ID, original timestamp, normalized time, observed fields, hypothesis and unresolved contradictions.
6. Why must accuracy/recall claims use known ground truth and a controlled evaluation, not just a correlation script?

## Research and evidentiary limits
This is a **teaching model**, not an NTFS or Sysmon parser. A real file reference has volume and lifecycle context; identifiers can be reused, clocks drift, logs may omit events, and reported process identity is not necessarily human/automation attribution. All events here are fictional.
