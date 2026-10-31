# Day 24 — Email Header Hop Order and Timestamp Checks

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Email Header Hop Order and Timestamp Checks** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Each mail server adds a `Received` line on top, so reading from the bottom shows the path from sender to recipient.
2. Timestamps along the path should not decrease; a decrease means clock skew or a forged line.
3. Only the lines added by servers you trust are reliable; lower lines can be forged by the sender.

## Important distinctions
- Small negative gaps are usually skew between servers, not forgery.
- A valid hop chain does not prove the message content is genuine.
- Record the source of every header you analyze.

## Hands-on lab
Read `headers_demo.py` before running the following from this lab folder:

~~~bash
python3 headers_demo.py
~~~


## Assignments
1. Predict which hop pair is out of order.
2. Run the demo and compare the size of the gaps.
3. Change the tolerated skew to 5 seconds and describe the effect.
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
