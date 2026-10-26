# Day 19 — Order of Volatility and Evidence Collection Priority

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Order of Volatility and Evidence Collection Priority** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Evidence disappears at different speeds: memory and network state first, disk later, backups last.
2. Collect the most volatile sources first, using value as a tie-breaker.
3. Every collection action changes the system, so record what you did, when, and with which tool.

## Important distinctions
- Volatility is about how fast evidence is lost; value is about how much it helps the case.
- A strict order is a default, not a law: legal or safety constraints can change it.
- A collected artifact is only useful if its provenance and hash are recorded.

## Hands-on lab
Read `volatility_demo.py` before running the following from this lab folder:

~~~bash
python3 volatility_demo.py
~~~


## Assignments
1. Predict the collection order before running the demo.
2. Run it and compare the output with your prediction.
3. Add a source called `Cloud audit logs` with a 90-day retention and decide where it belongs.
4. Add an assertion that a source with a shorter lifetime is never collected after a longer one of equal value.
5. Describe a case where a lower-volatility source must be collected first, and why.
6. Write the note you would put in the case log after collecting RAM.

## Knowledge check
1. Where does the input originate, and who controls it?
2. What was directly observed, as opposed to inferred?
3. What assumptions might fail in production?
4. Which evidence would be insufficient on its own?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
