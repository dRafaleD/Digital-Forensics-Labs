# Day 27 — Download History and File Creation Correlation

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Download History and File Creation Correlation** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. A file created in the download folder should have a browser download record within a few seconds.
2. A file with no matching record may have arrived by another route, such as a copy, an archive or another program.
3. Join on path and time window, and keep the tolerance explicit.

## Important distinctions
- A missing record may reflect cleared history, not a different origin.
- Clock differences between sources widen the tolerance you need.
- Document both matched and unmatched files.

## Hands-on lab
Read `download_demo.py` before running the following from this lab folder:

~~~bash
python3 download_demo.py
~~~


## Assignments
1. Predict which files have no download record.
2. Run the demo and record the matches.
3. Reduce the tolerance to 1 second and describe the effect.
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
