# Day 30 — Shell History Artifacts and Command Timeline

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Shell History Artifacts and Command Timeline** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. A shell history file can record commands, and with timestamps it becomes a timeline of what was typed.
2. Look for sequences rather than single commands, such as fetching a file, making it executable and running it.
3. History is written by the user's own shell, so it can be missing, edited or never saved.

## Important distinctions
- A sequence is a lead; administrators and developers run it legitimately.
- Absence of history is weak evidence, not proof of nothing happening.
- Convert epoch timestamps to UTC before building a timeline.

## Hands-on lab
Read `history_demo.py` before running the following from this lab folder:

~~~bash
python3 history_demo.py
~~~


## Assignments
1. Predict which window of commands is flagged.
2. Run the demo and record the timestamps of the flagged sequence.
3. Widen the window to 10 minutes and describe the effect.
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
