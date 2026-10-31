# Day 22 — Timestamp Anomalies and Stomping Indicators

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Timestamp Anomalies and Stomping Indicators** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Timestamps can be edited, so look for internal contradictions rather than trusting a single value.
2. Red flags include a creation time later than the modification time, zero sub-second precision, and a time before the OS release.
3. Compare two independent time sources, such as the filesystem and the journal or log, before concluding.

## Important distinctions
- A copy operation legitimately yields creation later than modification; this is a lead, not proof of tampering.
- Zero nanoseconds can come from a tool or filesystem that stores coarse time.
- Document each anomaly with the rule that raised it and the data it was based on.

## Hands-on lab
Read `stomp_demo.py` before running the following from this lab folder:

~~~bash
python3 stomp_demo.py
~~~


## Assignments
1. Predict which synthetic records raise a flag and for which reason.
2. Run the demo and record the flags per file.
3. Add a record produced by a normal copy and explain why it is flagged.
4. Add an assertion that a clean record raises no flags.
5. Describe how you would tell a legitimate copy from stomping.
6. Name an independent source (journal, event log, backup) that would corroborate a timestamp.

## Knowledge check
1. Where does the input originate, and who controls it?
2. What was directly observed, as opposed to inferred?
3. What assumptions might fail in production?
4. Which evidence would be insufficient on its own?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
