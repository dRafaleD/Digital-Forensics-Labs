#!/usr/bin/env python3
"""Synthetic process-lineage checks: GUIDs help, but source conflicts require abstention."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Process:
    guid: str
    pid: int
    started: int

@dataclass(frozen=True)
class Observation:
    child_guid: str
    child_started: int
    parent_guid: str | None
    parent_pid: int | None

PROCESSES = [
    Process("a-old", 400, 10),
    Process("b-child", 500, 20),
    Process("a-new", 400, 60),  # Reused numeric PID.
    Process("c-child", 600, 65),
]

def resolve(obs: Observation, processes: list[Process]) -> str:
    if not obs.parent_guid or obs.parent_pid is None:
        return "UNKNOWN"
    matching_guid = [p for p in processes if p.guid == obs.parent_guid]
    if len(matching_guid) > 1:
        return "AMBIGUOUS"
    if not matching_guid:
        return "UNKNOWN"
    parent = matching_guid[0]
    if parent.pid != obs.parent_pid:
        return "CONFLICTING_EVIDENCE"
    if parent.started >= obs.child_started:
        return "IMPOSSIBLE_ORDER"
    return "PARENT_CANDIDATE"

def main():
    cases = [
        ("early process parent", Observation("b-child",20,"a-old",400), PROCESSES, "PARENT_CANDIDATE"),
        ("reused PID, newer parent", Observation("c-child",65,"a-new",400), PROCESSES, "PARENT_CANDIDATE"),
        ("GUID disagrees with PID", Observation("c-child",65,"a-old",900), PROCESSES, "CONFLICTING_EVIDENCE"),
        ("no parent GUID", Observation("c-child",65,None,400), PROCESSES, "UNKNOWN"),
        ("unknown parent", Observation("c-child",65,"missing",400), PROCESSES, "UNKNOWN"),
        ("parent started later", Observation("b-child",20,"a-new",400), PROCESSES, "IMPOSSIBLE_ORDER"),
        ("duplicate GUID records", Observation("b-child",20,"a-old",400), PROCESSES+[PROCESSES[0]], "AMBIGUOUS"),
        ("numeric PID alone", Observation("c-child",65,None,400), PROCESSES, "UNKNOWN"),
    ]
    for label, obs, data, expected in cases:
        answer = resolve(obs, data)
        assert answer == expected, (label, answer)
        print(f"{label:27} {answer}")
    print(f"{len(cases)}/{len(cases)} fictional process-correlation checks passed")

if __name__ == "__main__":
    main()
