# Day 42 — Process Instance IDs and Parent PID Reuse

[English](notes.md) · [Türkçe](notes.tr.md) · [Python exercise](parent_pid_demo.py)

## After Day 41
Day 41 used process and scheduling telemetry only to suggest an **initiator context**, abstaining when evidence was missing. Day 42 introduces another reason to abstain: **PID reuse**. A numeric process ID may belong to different processes at different times.

## Synthetic lineage
Each toy event records PID, process creation time, parent PID and *claimed* parent creation time. The pair `(PID, creation time)` is a better **toy process-instance key** than PID alone. A parent can be reported as a **CANDIDATE** only if the exact pair matches a previously created process. Missing or duplicated source records produce `UNKNOWN` or `AMBIGUOUS`.

The exercise also includes a stale but structurally matching parent reference: the simplified classifier returns a candidate. That is a reminder that **internal consistency is not independent verification**. An actual examiner must check trustworthy event provenance, process lifetimes, source accuracy, PID rollover and available process GUIDs.

## Run
```bash
python3 labs/42-process-instance-ids-and-parent-pid-reuse/parent_pid_demo.py
```

## Questions
1. Why is PID 400 at time 10 not necessarily the same process as PID 400 at time 50?
2. Why does a parent/child relationship not prove a human actor?
3. Which Sysmon and Windows process telemetry can corroborate the relationship?
4. What extra evidence is needed to challenge a stale parent pointer?
5. Why should duplicate or missing observations remain ambiguous?

## Scope
Only fictional dictionaries; no Windows event log, host or personal data is accessed.
