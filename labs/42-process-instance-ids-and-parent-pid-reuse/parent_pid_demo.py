#!/usr/bin/env python3
"""Synthetic process lineage: PID alone is not a process-instance identifier."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Process:
    event_id: str
    pid: int
    created: int
    parent_pid: int | None
    parent_created: int | None

EVENTS = [
    Process("p1", 400, 10, None, None),
    Process("p2", 500, 15, 400, 10),
    Process("p3", 400, 50, None, None),   # Numeric PID reused later.
    Process("p4", 600, 55, 400, 50),
    Process("p5", 700, 57, 400, None),   # Parent start missing.
    Process("p6", 800, 60, 400, 10),    # Implausible but recorded stale parent.
]

def parent_of(process: Process, events: list[Process]) -> tuple[str, str]:
    if process.parent_pid is None or process.parent_created is None:
        return "UNKNOWN", "parent instance details absent"
    candidates = [p for p in events
                  if p.pid == process.parent_pid
                  and p.created == process.parent_created
                  and p.created < process.created]
    if len(candidates) == 1:
        # A matching parent record supports a lineage HYPOTHESIS, not causation.
        return "CANDIDATE", candidates[0].event_id
    if not candidates:
        return "UNKNOWN", "no matching parent instance"
    return "AMBIGUOUS", "duplicate process records"

def main():
    cases = [
        ("early child", EVENTS[1], "CANDIDATE", "p1"),
        ("reused PID child", EVENTS[3], "CANDIDATE", "p3"),
        ("missing parent start", EVENTS[4], "UNKNOWN", "parent instance details absent"),
        ("stale parent details", EVENTS[5], "CANDIDATE", "p1"),
        ("unknown start", Process("x", 900, 100, 400, 99), "UNKNOWN", "no matching parent instance"),
        ("duplicate source records", EVENTS[1], "AMBIGUOUS", "duplicate process records"),
        ("parent after child", Process("y", 901, 8, 400, 10), "UNKNOWN", "no matching parent instance"),
    ]
    for name, item, expected, detail in cases:
        source = EVENTS + ([EVENTS[0]] if name == "duplicate source records" else [])
        label, reason = parent_of(item, source)
        assert (label, reason) == (expected, detail), (name, label, reason)
        print(f"{name:24} {label:10} {reason}")
    print(f"{len(cases)}/{len(cases)} toy process-parent cases passed")

if __name__ == "__main__":
    main()
