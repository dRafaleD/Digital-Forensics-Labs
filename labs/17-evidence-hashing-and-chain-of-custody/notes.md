# Day 17 — Evidence Hashing, Chain of Custody and Verification

[English](notes.md) · [Türkçe](notes.tr.md)

## Objective
Build a reproducible evidence manifest for harmless local files. Understand SHA-256 integrity checks and the difference between **integrity**, **authenticity** and **chain of custody**.

## Concepts
- A cryptographic hash helps detect changes to bytes; it cannot establish who created a file or whether its contents were true.
- Chain of custody documents collection, transfer, storage and access; a checksum is just one part of that record.
- Acquire evidence with appropriate permissions and document original path, capture time, tool version, operator and time zone.
- Protect the manifest itself. A modified file and a modified manifest could appear consistent.
- File metadata and timestamps are potentially mutable; do not treat them as sole proof of attribution.

## Hands-on
```bash
python3 evidence_manifest_demo.py
```
The demo uses a temporary directory, creates two harmless text samples, saves their hashes and then shows a hash mismatch after changing one sample. No real user file is touched.

## Tasks
1. Explain why a matching hash alone does not prove authenticity.
2. Note which details a real custody log would need.
3. Compare SHA-256 before and after a controlled modification.
4. Identify risks if both evidence and manifest can be edited.
5. Propose a second independent acquisition/validation method.

## Safety
Only ephemeral synthetic data. The output is an educational manifest, not courtroom-ready evidence.
