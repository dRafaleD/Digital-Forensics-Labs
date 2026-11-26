# Day 50 — Evidence Graph Topological Layers and Ambiguous Order

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](graph_layers.py)

Day 49 modeled partial ordering. Here Kahn-style graph layers display currently unconstrained nodes together, instead of claiming a unique timeline. Edges are supplied ordering hypotheses; duplicates do not add weight. Cycles and unknown nodes are explicit errors. The nine cases include a chain, independent observations, a join, duplicate edges and cycles. Practice: draw a diamond graph, predict its layers, then add a contradictory edge. Nodes in different layers need not be directly comparable; a layer is not a timestamp or proof of causality. No real evidence collection.

## Run
```bash
python3 labs/50-evidence-graph-topological-layers/graph_layers.py
```
