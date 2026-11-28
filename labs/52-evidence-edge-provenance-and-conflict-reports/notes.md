# Day 52 — Evidence Edge Provenance and Conflict Reports

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](edge_review.py)

Day 51 explored reachability and incomparable events. Today retain the source identifiers attached to ordering claims and report directly reversed edges without choosing a winner. Repeated rows from the same source are deduplicated. Eight cases include competing observations, self-edges and a three-node cycle that this intentionally limited direct-conflict checker does not detect. Practice: draw the final cycle and apply the cycle checker from Day 50. Explain why source labels do not prove independence, and why NO_DIRECT_CONFLICT does not mean an ordering graph is consistent. All events and sources are invented.

## Run
```bash
python3 labs/52-evidence-edge-provenance-and-conflict-reports/edge_review.py
```
