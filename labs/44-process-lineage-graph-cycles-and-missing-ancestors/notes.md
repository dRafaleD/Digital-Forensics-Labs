# Day 44 — Process Lineage Graphs, Cycles and Missing Ancestors

[English](notes.md) · [Türkçe](notes.tr.md) · [Python exercise](lineage_graph.py)

## After Day 43
Day 43 checked a claimed parent process GUID against PID and start time. Day 44 extends a single parent-child relationship into a **lineage graph**—and shows why a chain must not be accepted blindly.

## Model
Each fictional process record has a process GUID, start time and claimed parent GUID. The evaluator walks upward, classifying:
- **CHAIN_CANDIDATE:** a complete, time-consistent chain to a recorded root.
- **MISSING_ANCESTOR:** an intermediate parent record is unavailable.
- **AMBIGUOUS_GUID:** duplicated process GUID records prevent unique identification.
- **TIME_ORDER_CONFLICT:** a parent does not precede the child.
- **CYCLE:** a path loops back to a previously visited process ID.

Even `CHAIN_CANDIDATE` is only a structured hypothesis: timestamps might be skewed, a source might be falsified, and an apparent process parent does **not** identify the human or automated actor responsible for execution.

## Run
```bash
python3 labs/44-process-lineage-graph-cycles-and-missing-ancestors/lineage_graph.py
```

## Questions
1. Why can an absent parent record be a collection gap, not evidence of a process with no parent?
2. How would a falsified process GUID appear in this graph?
3. Why are cycles and same-time parents suspicious but not proof of wrongdoing?
4. What independent Sysmon, Security 4688 and process-creation evidence could corroborate the links?
5. Why is timeline uncertainty important even for a structurally complete chain?

## Scope
No access to real processes, hosts, files or logs. Synthetic graph traversal only; no actor attribution.
