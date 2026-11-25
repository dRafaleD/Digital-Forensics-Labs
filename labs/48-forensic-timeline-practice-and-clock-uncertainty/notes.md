# Day 48 — Practice Day: Timeline Reconstruction and Clock Uncertainty

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](timeline.py)

A fictional download observation is timestamped 10:00:00 UTC with ±2 seconds uncertainty. Normalize other timezone-aware observations to UTC and compare their possible time intervals. An event is definitely BEFORE another only if its latest possible time precedes the other's earliest time. Overlapping boundaries remain ORDER_UNCERTAIN.

| Other observation | Expected relation of download |
|---|---|
| 10:00:10 UTC | BEFORE |
| 09:59:50 UTC | AFTER |
| 13:00:00 +03:00 | ORDER_UNCERTAIN |
| 10:00:04 UTC ±2 s | ORDER_UNCERTAIN |
| 10:00:05 UTC ±2 s | BEFORE |
| No timezone | INVALID_TIME |

**Exercises:** Predict 12 cases, normalize three timestamps by hand, increase uncertainty from 2 to 5 seconds and reassess the boundary cases, then write a short chronology with explicit uncertainty. Do not infer an initiator from temporal order.

Expected final line: 12/12 timeline cases passed. No real logs, acquisition or system access. This teaching model assumes supplied uncertainty bounds are meaningful.

## Run
```bash
python3 labs/48-forensic-timeline-practice-and-clock-uncertainty/timeline.py
```
