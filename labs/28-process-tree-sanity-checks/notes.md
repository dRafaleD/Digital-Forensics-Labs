# Day 28 — Process Tree Sanity Checks

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Process Tree Sanity Checks** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Well-known system processes have expected parents; a different parent is a lead worth checking.
2. A process whose parent PID is missing from the list may be an orphan whose parent exited.
3. Check parent, path and start time together instead of the name alone.

## Important distinctions
- Orphans are normal after a launcher exits.
- PIDs are reused, so match on PID plus start time in real data.
- A memory snapshot is a point in time and misses processes that already ended.

## Hands-on lab
Read `proctree_demo.py` before running the following from this lab folder:

~~~bash
python3 proctree_demo.py
~~~


## Assignments
1. Predict which processes are flagged.
2. Run the demo and record the reason for each flag.
3. Add a legitimate orphan and explain how you would clear it.
4. Add an assertion for one security property.
5. Describe a negative case and a potential false positive.
6. Propose an independent corroboration method.

## Knowledge check
1. Where does the input originate, and who controls it?
2. What was directly observed, as opposed to inferred?
3. What assumptions might fail in production?
4. Which evidence would be insufficient on its own?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
