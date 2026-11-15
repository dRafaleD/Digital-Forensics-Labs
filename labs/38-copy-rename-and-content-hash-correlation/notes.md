# Day 38 — Copy, Rename and Content-Hash Correlation

[English](notes.md) · [Türkçe](notes.tr.md) · [Python fixture](identity_hash_demo.py)

## Continuation of Day 37
File identity is not the same as a filename. **Content hashing** adds a third signal: two different files can contain identical bytes, but that alone does not prove one was copied from the other.

## Decision model
Each fictional artifact has a time, volume label, file ID, path and SHA-256 digest.
- **SAME_IDENTITY:** same volume and ID (including a renamed path).
- **CONTENT_MATCH_ONLY:** distinct identity and path, but the same content hash; consistent with a copy, not proof of it.
- **PATH_REUSED:** same path now belongs to another object; avoid merging records solely by filename.
- **TIME_REVERSED:** observation precedes the source in this toy causal timeline.
- **NO_MATCH:** none of those relationships.

Priority matters: path reuse outranks a content match in this simple classifier. A production examiner would report **both signals**, plus file-ID reuse risk, collection method and clock uncertainty. SHA-256 evidence must be tied to actual collected bytes and custody records.

## Run
~~~bash
python3 labs/38-copy-rename-and-content-hash-correlation/identity_hash_demo.py
~~~

## Exercises
1. Why do equal hashes not prove that a copy operation happened?
2. How would a different volume affect file identity?
3. Can a process access a file after it is renamed?
4. What additional USN Journal, file-system and process evidence can distinguish rename from copy?
5. Why must time-source offsets and possible file-ID reuse be recorded?

## Scope
All events are synthetic. No disks, user files or real evidence are read. The classifier is not a forensic conclusion engine.
