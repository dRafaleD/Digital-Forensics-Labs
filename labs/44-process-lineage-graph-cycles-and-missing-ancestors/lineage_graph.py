#!/usr/bin/env python3
"""Synthetic process-parent graph: classify incomplete or contradictory lineage."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Process:
    guid: str
    started: int
    parent_guid: str | None

def trace(start_guid: str, events: list[Process]) -> tuple[str, list[str]]:
    index: dict[str, list[Process]] = {}
    for event in events:
        index.setdefault(event.guid, []).append(event)
    visited: set[str] = set()
    chain: list[str] = []
    current_id = start_guid
    while True:
        if current_id in visited:
            return "CYCLE", chain
        visited.add(current_id)
        matches = index.get(current_id, [])
        if not matches:
            return "MISSING_ANCESTOR", chain
        if len(matches) > 1:
            return "AMBIGUOUS_GUID", chain
        current = matches[0]
        chain.append(current_id)
        if current.parent_guid is None:
            return ("ROOT_ONLY" if len(chain) == 1 else "CHAIN_CANDIDATE"), chain
        if current.parent_guid in visited:
            return "CYCLE", chain
        parents = index.get(current.parent_guid, [])
        if not parents:
            return "MISSING_ANCESTOR", chain
        if len(parents) != 1:
            return "AMBIGUOUS_GUID", chain
        if parents[0].started >= current.started:
            return "TIME_ORDER_CONFLICT", chain
        current_id = current.parent_guid

def main():
    root = Process("root", 10, None)
    middle = Process("middle", 20, "root")
    child = Process("child", 30, "middle")
    cases = [
        ("normal chain", "child", [root, middle, child], "CHAIN_CANDIDATE"),
        ("root only", "root", [root], "ROOT_ONLY"),
        ("missing grandparent", "child", [middle, child], "MISSING_ANCESTOR"),
        ("missing immediate parent", "child", [child], "MISSING_ANCESTOR"),
        ("duplicate parent GUID", "child", [root, middle, middle, child], "AMBIGUOUS_GUID"),
        ("child before parent", "child", [root, middle, Process("child", 15, "middle")], "TIME_ORDER_CONFLICT"),
        ("same start timestamp", "child", [root, middle, Process("child", 20, "middle")], "TIME_ORDER_CONFLICT"),
        ("self parent cycle", "child", [Process("child", 30, "child")], "CYCLE"),
        ("two node cycle", "a", [Process("a", 30, "b"), Process("b", 20, "a")], "CYCLE"),
    ]
    for label, guid, events, expected in cases:
        actual, path = trace(guid, events)
        assert actual == expected, (label, actual, path)
        print(f"{label:29} {actual:23} {path}")
    print(f"{len(cases)}/{len(cases)} synthetic lineage graph checks passed")

if __name__ == "__main__":
    main()
