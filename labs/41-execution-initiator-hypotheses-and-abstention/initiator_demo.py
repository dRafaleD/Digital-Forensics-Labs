#!/usr/bin/env python3
"""Synthetic DFIR initiator hypotheses: ambiguous evidence should remain UNKNOWN."""

def attribute(event: dict) -> tuple[str, str]:
    if not isinstance(event, dict) or not isinstance(event.get("event_id"), str):
        return "UNKNOWN", "missing event identity"
    if not isinstance(event.get("process_logged"), bool) or not event["process_logged"]:
        return "UNKNOWN", "process start not corroborated"
    # Observations are only toy evidence, not verified OS records.
    interactive = event.get("interactive_session") is True
    scheduled = event.get("task_event") is True
    service = event.get("service_event") is True
    if interactive and (scheduled or service):
        return "AMBIGUOUS", "conflicting interactive/automation indicators"
    if scheduled and service:
        return "AMBIGUOUS", "multiple automation indicators"
    if interactive:
        return "INTERACTIVE_CONTEXT", "session indicator; human action unproven"
    if scheduled:
        return "SCHEDULED_CONTEXT", "task indicator; scheduler initiator unproven"
    if service:
        return "SERVICE_CONTEXT", "service indicator; service identity unproven"
    return "UNKNOWN", "no supporting initiator context"

def main():
    base = {"event_id": "proc-01", "process_logged": True}
    cases = [
        ("interactive", {**base, "interactive_session": True}, "INTERACTIVE_CONTEXT"),
        ("task", {**base, "task_event": True}, "SCHEDULED_CONTEXT"),
        ("service", {**base, "service_event": True}, "SERVICE_CONTEXT"),
        ("conflicting", {**base, "interactive_session": True, "task_event": True}, "AMBIGUOUS"),
        ("two automation", {**base, "task_event": True, "service_event": True}, "AMBIGUOUS"),
        ("no context", base, "UNKNOWN"),
        ("missing process", {**base, "process_logged": False, "task_event": True}, "UNKNOWN"),
        ("missing event id", {"process_logged": True, "task_event": True}, "UNKNOWN"),
    ]
    for label, event, expected in cases:
        verdict, reason = attribute(event)
        assert verdict == expected, (label, verdict)
        print(f"{label:19} {verdict:20} {reason}")
    print("8/8 synthetic attribution-abstention checks passed")

if __name__ == "__main__":
    main()
