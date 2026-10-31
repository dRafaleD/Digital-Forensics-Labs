# Day 23 — Program Execution Artifacts and Unusual Paths

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Program Execution Artifacts and Unusual Paths** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Execution artifacts record which program ran, how often and when, which helps to build a timeline.
2. Unusual locations such as temp or download folders deserve a closer look, especially for rarely run files.
3. An artifact proves a program was launched, not what it did or who launched it.

## Important distinctions
- Software installers and updates legitimately run from temp paths.
- Artifacts can be deleted or age out, so absence is weak evidence.
- Correlate with logs and file system times before concluding.

## Hands-on lab
Read `execution_demo.py` before running the following from this lab folder:

~~~bash
python3 execution_demo.py
~~~


## Assignments
1. Predict which synthetic entries are flagged.
2. Run the demo and record the reason for each flag.
3. Add a legitimate installer in a temp path and explain how you would clear it.
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
