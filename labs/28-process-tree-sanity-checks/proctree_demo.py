"""Sanity-check a synthetic process list for unexpected parents and orphans."""
PROCS = [
    {"pid": 4, "ppid": 0, "name": "system"},
    {"pid": 400, "ppid": 4, "name": "smss.exe"},
    {"pid": 600, "ppid": 400, "name": "services.exe"},
    {"pid": 700, "ppid": 600, "name": "svchost.exe"},
    {"pid": 1200, "ppid": 4242, "name": "helper.exe"},          # parent not in the list
    {"pid": 1300, "ppid": 1200, "name": "svchost.exe"},         # svchost with a user-level parent
]
EXPECTED_PARENT = {"svchost.exe": "services.exe"}


def findings(procs):
    by_pid = {p["pid"]: p for p in procs}
    out = []
    for p in procs:
        parent = by_pid.get(p["ppid"])
        if parent is None and p["ppid"] != 0:
            out.append(f"{p['name']} ({p['pid']}): parent {p['ppid']} not in snapshot (orphan or exited)")
        want = EXPECTED_PARENT.get(p["name"])
        if want and parent and parent["name"] != want:
            out.append(f"{p['name']} ({p['pid']}): parent is {parent['name']}, expected {want}")
    return out


if __name__ == "__main__":
    out = findings(PROCS)
    for line in out:
        print(line)
    assert len(out) == 2
    print("PASS: unexpected parents and orphans are surfaced as leads.")
    print("Review: PIDs are reused and a snapshot misses processes that already ended.")
