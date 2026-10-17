# Day 10 — Multi-Source Artifact Correlation and Confidence Reporting

[English](notes.md) · [Türkçe](notes.tr.md)

## Goal
Understand multi-source artifact correlation and confidence reporting through a fully local, harmless experiment. Keep observation separate from inference.

## Core concepts
1. **event timestamps and UTC normalization** — document the boundary, expected behavior and limitations.
2. **joining across request IDs** — document the boundary, expected behavior and limitations.
3. **source integrity hashes** — document the boundary, expected behavior and limitations.
4. **positive versus missing evidence** — document the boundary, expected behavior and limitations.
5. **corroboration versus causation** — document the boundary, expected behavior and limitations.
6. **confidence and uncertainty statements** — document the boundary, expected behavior and limitations.

## Procedure
The included `correlate.py` is a synthetic training example. From the lab directory:

```bash
python3 correlate.py
```

**Expected:** Events are normalized into UTC and sorted; only the first two share a correlation ID.

## Observations to record
Write down the machine/tool versions, exact command, input, actual output, unexpected behavior, and interpretation. Explain which results are facts and which remain hypotheses.

## Exercises
1. Run the baseline and save the observed output.
2. Change one harmless input and predict what happens before running.
3. Add a negative test and distinguish a rejection from a failure to observe.
4. Restore the original, rerun it, and explain why regression tests matter.
5. Identify two realistic false-positive explanations.
6. Identify a useful independent corroborating observation.
7. Draft a short report stating limitations explicitly.

## Review questions
1. What does event timestamps and UTC normalization mean, why does it matter, and what does it not guarantee?
2. What does joining across request IDs mean, why does it matter, and what does it not guarantee?
3. What does source integrity hashes mean, why does it matter, and what does it not guarantee?
4. What does positive versus missing evidence mean, why does it matter, and what does it not guarantee?
5. What does corroboration versus causation mean, why does it matter, and what does it not guarantee?
6. What does confidence and uncertainty statements mean, why does it matter, and what does it not guarantee?
7. What would improve the confidence of your result?
8. Which regression test should be automated first?

## Ethics and scope
Use only locally generated data and infrastructure you own or are authorized to study. Findings from an individual signal are not proof of an incident.
