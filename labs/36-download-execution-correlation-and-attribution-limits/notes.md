# Day 36 — Download-to-Execution Correlation and Attribution Limits

[English](notes.md) · [Türkçe](notes.tr.md) · [Python fixture](attribution_demo.py)

## Connection to Day 35
Day 35 compared browser download records with `Zone.Identifier`. Day 36 adds **synthetic process telemetry** to the timeline. Matching paths and nearby timestamps can support a *hypothesis*, but they do **not** establish that a download caused execution or identify the person/process that initiated it.

## Three evidence sources
- **Browser history:** a possible download event, with timestamp and recorded path.
- **Zone.Identifier:** a possible origin marker; the alternate data stream may be missing, copied, modified or not applicable.
- **Process telemetry:** a claimed executable path and launch time. Process events need a trustworthy source and careful timestamp normalization.

The example uses UTC offsets and a ±5-second illustrative matching window. For downloads, the process event must not precede the download in the synthetic timeline. A real investigation must record time skew, collection gaps, path normalization and copied/renamed files. Our strings are not evidence of actual execution.

## Synthetic outcomes
- **CORRELATED:** one matching download and one matching Zone observation within the window.
- **AMBIGUOUS:** two candidate downloads share the same file path near a process event.
- **INSUFFICIENT:** a process record has no matching download or Zone observation.

These labels measure **candidate linkage**, not confidence scores or actor identity. Correlated records are still compatible with alternative explanations.

## Reproduce
~~~bash
python3 labs/36-download-execution-correlation-and-attribution-limits/attribution_demo.py
~~~

## Investigative questions
1. Why does a matching file path not identify the process initiator?
2. What could make two correct clocks appear to disagree?
3. What is lost when an artifact is renamed between download and execution?
4. Which additional records (process parent, command line, file identity, hashes) could help challenge a hypothesis?
5. How would you record a case where one of the evidence sources is missing?

## Limits and ethics
Entirely synthetic read-only Python; no disk image or actual host is interrogated. Do not claim causation or attribution based only on temporal proximity.
