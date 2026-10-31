# Day 26 — Report Redaction with Stable Pseudonyms

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Report Redaction with Stable Pseudonyms** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Replace identifiers such as usernames and addresses with stable pseudonyms so the story stays readable.
2. Use a keyed hash so people cannot reverse the pseudonyms by hashing guesses.
3. Keep the mapping key and the original evidence in controlled storage, outside the shared report.

## Important distinctions
- Pseudonyms protect identity but still allow correlation; that is both the benefit and the risk.
- Redaction must cover metadata, filenames and screenshots, not just body text.
- Test with synthetic data only.

## Hands-on lab
Read `redact_demo.py` before running the following from this lab folder:

~~~bash
python3 redact_demo.py
~~~


## Assignments
1. Predict the pseudonym for the repeated username.
2. Run the demo and confirm the original names are gone.
3. Change the key and describe what happens to the pseudonyms.
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
