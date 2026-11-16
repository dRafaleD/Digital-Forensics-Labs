# Day 39 — Timestamp Intervals and File-Evidence Ambiguity

[English](notes.md) · [Türkçe](notes.tr.md) · [Python exercise](uncertain_timeline.py)

## Continuing Day 38
Day 38 compared copy and rename hypotheses using paths, file IDs and SHA-256 hashes. Now we add **timestamp uncertainty**. A timestamp is an observation, not necessarily an exact moment: collection lag, filesystem resolution, clock skew and timezone mistakes all affect a timeline.

## Two independent questions
1. **Relationship:** do events share a recorded volume/file ID, a pathname, only the content hash, or none of these?
2. **Time order:** with `time ± uncertainty`, was the origin definitely earlier, the observation definitely earlier, or do the intervals overlap?

`SAME_RECORDED_ID` is deliberately not called `SAME_FILE`: file IDs may be reused and must be interpreted with volume context and record provenance. Equal hashes do not prove a copy took place. Overlapping intervals prevent a defensible claim of strict order.

## Reproduce
~~~bash
python3 labs/39-timestamp-intervals-and-file-evidence-ambiguity/uncertain_timeline.py
~~~
Eight checks cover rename, copy candidate, overlapping time windows, cross-volume identity, path reuse, apparent reverse order, unrelated artifacts and invalid uncertainty.

## Exercises
1. What does `100 ± 2 seconds` mean for an event at `102 ± 3`?
2. Why should collection time not be silently substituted for event time?
3. When could equal content hashes arise without a copy from the claimed source?
4. Which USN Journal, process and file-reference records would help challenge a hypothesis?
5. How do you report an unresolved timeline without inventing an actor?

## Scope
Only synthetic event dictionaries. No real disk, host, malware or forensic image is examined. The model is an evidence-labeling aid, not a causation test.
