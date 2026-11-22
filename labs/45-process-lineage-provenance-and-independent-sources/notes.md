# Day 45 — Process-Lineage Provenance and Independent Sources

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python](lineage_provenance_demo.py)

## After Day 44
A process ancestry graph can contain cycles, missing ancestors and contradictory timestamps. Day 45 asks another forensic question: **do two supporting records really come from independent sources?**

## Model
The examiner—not the observed log text—maintains a mapping from collector IDs to their underlying **origin**. A forwarded copy from `relay-a` and the original `agent-a` both represent one origin. Therefore, forwarding does not double the corroboration count.

For a given child Process GUID, the synthetic classifier checks parent-before-child time, conflicting parent GUID claims, and independent origins:
- `SINGLE_ORIGIN`: one origin supports a parent hypothesis.
- `CORROBORATED_CONTEXT`: two or more **distinct registered origins** agree.
- `SOURCE_CONFLICT` / `CROSS_SOURCE_CONFLICT`: contradictory claims.
- `TIME_CONFLICT` / `UNKNOWN`: impossible timing or insufficient admissible records.

Corroboration is not proof of a human initiator; separate sensors can share upstream errors, clocks, or compromised data.

## Run
```bash
python3 labs/45-process-lineage-provenance-and-independent-sources/lineage_provenance_demo.py
```

## Questions
Why does a log relay not count as a second witness? Why must source identity be established by collection metadata? How could two sensors copy the same false root observation? How should contradictory process parent evidence be described?

## Limits
Only invented process events; no Windows hosts, process creation logs or live evidence are touched.
