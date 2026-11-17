# Day 40 — Timeline Provenance and Independent Corroboration

[English](notes.md) · [Türkçe](notes.tr.md) · [Python exercise](corroboration_demo.py)

## From Day 39
Timestamp **intervals** help distinguish possible from impossible event sequences. Yet two compatible logs might be copies of the *same upstream observation*. Day 40 combines timing, recorded file identity and producer provenance.

## Model
Each fictional event contains a producer, collector/relay, volume, file ID and `second ± uncertainty`. It correlates a candidate with the reference only when the recorded `(volume, file_id)` pair matches and the closest possible time gap is within five seconds.

The example groups matched events by **producer**, not by collector. Duplicate forwarded events contribute only one origin. Distinct producer labels offer stronger hypotheses but cannot guarantee real sensor independence: labels can be wrong or forged, file IDs can be reused and records can share a common upstream source.

## Reproduce
~~~bash
python3 labs/40-timeline-provenance-and-independent-corroboration/corroboration_demo.py
~~~

## Exercises
1. Why is a collector not necessarily the origin of an event?
2. What does `102 ± 3` mean when comparing timestamps?
3. Why is volume identity necessary beside numeric file ID?
4. What collection metadata would establish provenance more reliably than a text label?
5. Can corroboration establish who initiated a download or execution?

## Scope
Synthetic dictionaries only, no live Windows artifacts. This demo supports evidence questions, not causality or actor attribution.
