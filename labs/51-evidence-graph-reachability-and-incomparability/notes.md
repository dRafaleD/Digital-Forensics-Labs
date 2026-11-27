# Day 51 — Evidence Graph Reachability and Incomparability

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](relations.py)

Day 50 grouped nodes into topological layers. Today determine whether a pair is actually ordered by a path in a valid directed acyclic evidence graph. A and D are related through B; C and D remain incomparable despite being on different layers. Predict nine cases; draw the graph and add C→D, then reconsider the pair. A reachable path represents supplied order hypotheses only, not causation or independently verified event times. Cyclic inputs are rejected globally. No real evidence.

## Run
```bash
python3 labs/51-evidence-graph-reachability-and-incomparability/relations.py
```
