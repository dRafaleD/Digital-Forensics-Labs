#!/usr/bin/env python3
"""Synthetic DFIR: missing telemetry is not evidence a parent did not exist."""
from dataclasses import dataclass

# Examiner-maintained origin registry (not accepted from record text).
ORIGIN = {"agent-a": "source-a", "relay-a": "source-a",
          "agent-b": "source-b", "agent-c": "source-c"}

@dataclass(frozen=True)
class Observation:
    collector: str
    child: str
    parent: str
    child_time: int
    parent_time: int

def classify(target: str, when: int, rows: list[Observation],
             coverage: dict[str, bool]) -> str:
    parents: dict[str, set[str]] = {}
    for row in rows:
        source = ORIGIN.get(row.collector)
        if row.child != target or source is None:
            continue
        if not coverage.get(source, False):  # Claim not in a covered interval.
            continue
        if row.child_time != when or row.parent_time >= row.child_time:
            return "TIMING_CONFLICT"
        parents.setdefault(source, set()).add(row.parent)
    if any(len(values) > 1 for values in parents.values()):
        return "SOURCE_CONFLICT"
    claims = {next(iter(values)) for values in parents.values()}
    if len(claims) > 1:
        return "CROSS_SOURCE_CONFLICT"
    if len(parents) >= 2:
        return "CORROBORATED_CONTEXT"
    if not parents:
        return "NO_POSITIVE_EVIDENCE"
    if any(not coverage.get(src, False) for src in {"source-a","source-b","source-c"}):
        return "LIMITED_COVERAGE"
    return "SINGLE_ORIGIN"

def main():
    a = Observation("agent-a","child-1","parent-x",50,10)
    relay = Observation("relay-a","child-1","parent-x",50,10)
    b = Observation("agent-b","child-1","parent-x",50,10)
    disagree = Observation("agent-b","child-1","parent-y",50,15)
    full = {"source-a": True, "source-b": True, "source-c": True}
    partial = {"source-a": True, "source-b": False, "source-c": False}
    tests = [
        ("single covered source", [a], full, "SINGLE_ORIGIN"),
        ("relay duplicates same origin", [a,relay], full, "SINGLE_ORIGIN"),
        ("two independent origins", [a,b], full, "CORROBORATED_CONTEXT"),
        ("other source lacks coverage", [a], partial, "LIMITED_COVERAGE"),
        ("no records but covered", [], full, "NO_POSITIVE_EVIDENCE"),
        ("uncovered record ignored", [a], {"source-a":False}, "NO_POSITIVE_EVIDENCE"),
        ("independent sources contradict", [a,disagree], full, "CROSS_SOURCE_CONFLICT"),
        ("same origin contradicts", [a,Observation("relay-a","child-1","parent-y",50,12)], full, "SOURCE_CONFLICT"),
        ("impossible parent order", [Observation("agent-a","child-1","parent-x",50,55)], full, "TIMING_CONFLICT"),
        ("unknown collector", [Observation("outside","child-1","parent-x",50,10)], full, "NO_POSITIVE_EVIDENCE"),
    ]
    for label, observations, covered, expected in tests:
        actual = classify("child-1", 50, observations, covered)
        assert actual == expected, (label, actual)
        print(f"{label:37} {actual}")
    print(f"{len(tests)}/{len(tests)} synthetic source-coverage checks passed")

if __name__ == "__main__":
    main()
