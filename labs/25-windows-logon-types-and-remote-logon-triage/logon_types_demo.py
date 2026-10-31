"""Triage synthetic Windows logon events by type, source and hour."""
INTERNAL_PREFIX = "10."
EVENTS = [
    {"user": "alice", "type": 2, "src": "-", "hour": 9},
    {"user": "svc-backup", "type": 3, "src": "10.0.0.5", "hour": 2},
    {"user": "bob", "type": 10, "src": "10.0.0.20", "hour": 10},
    {"user": "admin", "type": 10, "src": "203.0.113.9", "hour": 3},
]


def reasons(e):
    found = []
    if e["type"] == 10 and not e["src"].startswith(INTERNAL_PREFIX):
        found.append("remote interactive logon from an external address")
    if e["type"] == 10 and (e["hour"] < 6 or e["hour"] > 22):
        found.append("remote interactive logon at an unusual hour")
    return found


if __name__ == "__main__":
    for e in EVENTS:
        print(f"{e['user']:11} type={e['type']:<3} {reasons(e)}")
    assert reasons(EVENTS[0]) == [] and reasons(EVENTS[2]) == []
    assert len(reasons(EVENTS[3])) == 2
    print("PASS: type 10 from outside the network at night is the strongest lead.")
    print("Review: admins legitimately use RDP; check failures before the logon and the audit policy.")
