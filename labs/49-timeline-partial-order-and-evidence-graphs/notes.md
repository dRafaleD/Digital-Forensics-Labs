# Day 49 — Timeline Partial Order and Evidence Graphs

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](partial_order.py)

Day 48 compared pairs of uncertain timestamps. Day 49 builds a directed graph of only definite chronological relations. An edge A → B exists only when A's latest possible time is strictly earlier than B's earliest. Overlap or touching boundaries produces no edge, rather than an arbitrary ordering.

Worked example: A=[0,2], B=[1,4], C=[5,7], D=[7,9]. Four edges: A→C, A→D, B→C, B→D. A/B and C/D remain uncertain. Input ordering does not change the graph.

**Practice:** draw the graph, predict what changes if D starts at 8, add an event spanning all four, and explain why definite temporal order is not proof of causation. Expected final line: 9 partial-order checks passed. Fictional evidence only; the model assumes valid uncertainty bounds and does not determine an initiator.

## Run
```bash
python3 labs/49-timeline-partial-order-and-evidence-graphs/partial_order.py
```
