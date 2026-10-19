# Day 12 — Evidence Manifests, Integrity Checking and Audit Limits

[English](notes.md) | [Türkçe](notes.tr.md)

## Objective and scope

Explore evidence manifests, integrity checking and audit limits with a local, harmless example. Identify trust boundaries, failure cases and environmental assumptions rather than memorizing output.

## Key observations

1. A cryptographic digest describes bytes, not custody history.
2. Preserve originals and inspect copies.
3. Record method, timestamps, tool versions and limitations.

## Practical exercise

Inspect `manifest_demo.py`, predict its behavior, then run the following commands from this directory:

```bash
python3 manifest_demo.py
```

```bash
python3 -m json.tool manifest.json
```

## Analysis tasks

1. Record baseline output and compare against your prediction.
2. Change one harmless input and repeat.
3. Verify a positive and negative scenario.
4. Describe two possible false-positive or false-negative explanations.
5. Propose an independent corroborating observation.
6. Report observations, uncertainty and a next step.

## Mini challenge

Turn the demonstration into a regression test with an assertion for the intended security property.

## Review questions

1. Where is the trust boundary?
2. Which claim is directly observed versus inferred?
3. What environmental changes affect the result?
4. How should the system handle failure?
5. Why is one finding not conclusive proof?
6. What does a regression test guarantee, and what does it not?

## Safety

Use only synthetic, local or expressly authorized targets. Training results are not proof of compromise or production readiness.
