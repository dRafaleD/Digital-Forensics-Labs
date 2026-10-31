"""Check synthetic Received-header hops (oldest first) for timestamp order and skew."""
HOPS = [
    ("mx-out.sender.test", 1000),
    ("relay1.example.test", 1004),
    ("relay2.example.test", 1002),   # 2 s backwards: probably skew
    ("mx-in.recipient.test", 1500),  # 498 s forward: slow queue
    ("mailbox.recipient.test", 900),  # 600 s backwards: suspicious
]


def check(hops, skew_tolerance=3):
    findings = []
    for (a, ta), (b, tb) in zip(hops, hops[1:]):
        delta = tb - ta
        if delta < -skew_tolerance:
            findings.append(f"{a} -> {b}: goes back {-delta}s (forged line or large skew)")
        elif delta < 0:
            findings.append(f"{a} -> {b}: goes back {-delta}s (within tolerated skew)")
    return findings


if __name__ == "__main__":
    out = check(HOPS)
    for f in out:
        print(f)
    assert len(out) == 2
    assert "tolerated" in out[0] and "forged" in out[1]
    print("PASS: small reversals are treated as skew; large ones are leads for forgery.")
    print("Review: only lines added by servers you trust are reliable evidence.")
