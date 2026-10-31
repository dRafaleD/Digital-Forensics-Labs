# Day 25 — Windows Logon Types and Remote Logon Triage

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Windows Logon Types and Remote Logon Triage** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Logon events carry a logon type: 2 is interactive, 3 is network, 10 is remote interactive (RDP).
2. Type 10 from an external address, or at an unusual hour, is a strong lead for review.
3. Pair successful logons with the preceding failures and the source address to see the whole story.

## Important distinctions
- Administrators legitimately use RDP; context decides.
- Logon types are only as complete as the audit policy that produced them.
- Missing events may mean logging was off, not that nothing happened.

## Hands-on lab
Read `logon_types_demo.py` before running the following from this lab folder:

~~~bash
python3 logon_types_demo.py
~~~


## Assignments
1. Predict which events are flagged.
2. Run the demo and record each reason.
3. Add an internal admin RDP logon and explain why it is not flagged.
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
