# Day 6 — Incident Triage, Artifact Correlation and Evidence Integrity

[English](notes.md) · [Türkçe](notes.tr.md)

**Goal:** extend Day 5 log timelines with process/network/file artifact correlation and verifiable evidence preservation.

**Scope:** No live host inspection; scripts create synthetic JSONL artifacts and a SHA-256 manifest.

## 1. Triage and scoping

Digital forensic triage is a focused first pass: determine what artifacts exist, preserve original evidence and identify which additional collection is justified. A triage finding is not a final incident conclusion.

## 2. Multiple evidence sources

Process snapshots can show PID, parent PID and command name; network logs show connections; file records describe observed file events. Each source is partial. A process name appearing in a log is not proof of which person executed it.

## 3. Hashes and source integrity

SHA-256 hashes describe a byte-for-byte baseline. Verify before interpretation, and stop on mismatch. The generated manifest records expected values. Hash equality supports integrity against the baseline, not the authenticity of a collector or truth of recorded events.

## 4. Chain of custody

Real cases need acquisition details, collector identity, custody transfers, timestamps, tools and hash records. This lab starts at synthetic evidence creation; it cannot demonstrate a real-world chain of custody. Record every transformation separately.

## 5. Timestamp normalization

Mixed timezone data cannot be reliably compared by lexicographically sorting raw timestamps. Keep original strings and normalize to aware UTC datetime for correlation. Also consider clock skew, timestamp precision and missing records.

## 6. PID correlation and reuse

A PID can link process, network and file records within a scoped time window. It can also be reused after process termination; stable correlation may need start time, executable identity, host ID, session or other evidence. Never join unrelated hosts by PID alone.

## 7. Network evidence boundaries

An outbound connection record identifies a tuple seen by one sensor; it does not prove data exfiltration or user intent. Our synthetic destination uses documentation address 192.0.2.55 and is never contacted. Payload is not present.

## 8. File metadata and causation

A file creation entry and process connection close together in time may be relevant, but correlation does not establish a causal chain. Seek file hashes, process handles, EDR or filesystem journals when authorized.

## 9. Confidence and reporting

Write each finding as source observation, time, corroborating evidence, inference, limitations and confidence. Distinguish “log records X” from “person X definitely performed Y.” Confidence should reflect source quality and coverage.

## 10. Safety and privacy

Collect live process/network data only on authorized assets; logs may contain private names and identifiers. Work on copies and avoid exposing real evidence in GitHub. This lab intentionally creates fake metadata rather than inspecting the host.

## Hands-on workflow

In the lab directory:

```bash
python3 generate_case.py
python3 analyze_case.py
```

The generator creates:
- `evidence/processes.jsonl`: synthetic parent PID 4102, child 4103, exit.
- `evidence/connections.jsonl`: fake network connect and close attributed to PID 4103.
- `evidence/files.jsonl`: synthetic file create/read metadata.
- `manifest.sha256.json`: SHA-256 manifest for the three artifacts.

The analyzer **verifies all three digests before interpretation**, then normalizes timestamps to UTC and correlates records using PID. It performs no live process collection, network traffic or real filesystem triage.

### Integrity experiment

On a **working copy**, add one blank character to `evidence/files.jsonl` and run `python3 analyze_case.py`. The analysis should stop with a hash mismatch. Regenerate the reproducible synthetic baseline using `python3 generate_case.py`. In a real case, do **not** overwrite original evidence; this regeneration is specific to fabricated training data.

### Mini challenges

1. Reconstruct all synthetic PID 4103 events in one timeline.
2. Use start/exit times to explain PID reuse risk.
3. Explain why the present data cannot prove that the network request caused file creation.
4. Create an evidence worksheet: source, hash, timezone, observation, inference and limitation.

### Exercises

1. Generate fixtures.
2. Inspect manifest digests.
3. Verify evidence integrity.
4. Read the timeline.
5. Interpret normalized UTC times.
6. Draw the parent/child tree.
7. Explain PID scoping.
8. Identify network tuple.
9. Inspect file event order.
10. Simulate integrity failure.
11. Separate observations from inferences.
12. Write an eight-sentence triage report.

### Review questions

1. What is forensic triage?
2. Acquisition versus analysis?
3. What does hashing support?
4. What doesn't hashing prove?
5. What is chain of custody?
6. Why normalize time zones?
7. How does clock skew affect timelines?
8. What is PID reuse?
9. Does process name prove human identity?
10. Does connection evidence prove exfiltration?
11. Is timing correlation causation?
12. What is evidence scope?
13. Why preserve originals?
14. What if a manifest digest fails?
15. What limitations belong in triage findings?

**Takeaway:** Preserve evidence, verify integrity, correlate carefully across sources and clearly separate observations from inferences.
