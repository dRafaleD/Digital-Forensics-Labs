# Day 32 — Conflicting Artifacts and Source Provenance

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline lab](conflicts_demo.py)

## Objective
A digital investigation often combines file-system metadata, operating-system logs and application audit records. Different sources can refer to the **same event** while disagreeing about important details. Good forensic reporting must preserve that contradiction rather than silently choosing a convenient story.

## Evidence is not the same as interpretation
A record's **source ID**, original timestamp, collection time and reported field values should survive normalization. When two sources report different initiating actors, the discrepancy is itself a finding. It does not automatically mean evidence was forged, that either source is incorrect or that a specific actor is malicious.

## Example dataset
The example has three fabricated observations about `artifact-01`:
- A file-operation source labels the initiator `automation`.
- An application audit source labels it `user`.
- A storage source records the artifact without an initiator.

The same artifact identifier lets the investigator correlate records, but **cannot adjudicate actor identity**. The program keeps all three entries intact and returns `inconclusive` when competing nonempty actor labels exist.

## Practice
```bash
python3 conflicts_demo.py
```

Study the `report` structure: it includes evidence IDs, reported actor labels and an explicit uncertainty statement. No real log or disk is read.

## Exercises
1. Replace an actor with `unknown`: does that settle the conflicting testimony?
2. Explain why log provenance, field meaning and timestamp uncertainty must be checked before correlation.
3. Add a fourth record collected later; do not overwrite any original record.
4. Define what independent corroboration might resolve the attribution question.
5. Write a short report that distinguishes **observed**, **reported**, **inferred** and **unresolved**.

## Research limitations
Synthetic strings are not an NTFS, Sysmon or Windows Event Log parser. No actor attribution metric or accuracy claim is implied. Real-case analysis needs documented acquisition, preservation and source semantics.
