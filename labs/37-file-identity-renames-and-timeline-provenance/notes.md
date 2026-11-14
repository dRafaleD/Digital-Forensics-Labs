# Day 37 — File Identity, Rename Events and Timeline Provenance

[English](notes.md) · [Türkçe](notes.tr.md) · [Python fixture](identity_timeline.py)

## Follow-up to Day 36
Download/execution correlation based only on **path and time** can fail if a file is renamed. This exercise compares a fictional pair `(volume, file_id)` with a file path across download, rename and execution records.

A path can change while an object's identity stays the same. Another object may later reuse the old path. The same numeric file ID on a **different volume** is not the same identity.

## Local practice
```bash
python3 labs/37-file-identity-renames-and-timeline-provenance/identity_timeline.py
```
Seven assertions check same-volume identity, cross-volume collisions and path reuse. Records are synthetic and deliberately simple: genuine filesystem identity values can be reused over time, affected by copies, and not present in every log.

## Questions
1. Which evidence is lost with path-only matching?
2. Why include a volume identifier?
3. What happens to identity under a copy instead of a rename?
4. How might hash, USN, file reference and process telemetry independently corroborate a claim?
5. Does matching file identity prove who initiated execution?

## Limits
An illustrative correlation exercise, not a Windows forensic parser. Provenance, collection integrity, actor identity and causation remain unproven.
