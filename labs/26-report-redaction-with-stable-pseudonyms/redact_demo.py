"""Replace identifiers in a synthetic report with keyed, stable pseudonyms."""
import hashlib
import hmac
import re

KEY = b"demo-key-not-a-secret"   # keep a real key outside the shared report


def pseudo(kind, value):
    return f"{kind}-" + hmac.new(KEY, value.encode(), hashlib.sha256).hexdigest()[:6]


def redact(text, users, ips):
    for u in users:
        text = re.sub(rf"\b{re.escape(u)}\b", pseudo("USER", u), text)
    for ip in ips:
        text = text.replace(ip, pseudo("HOST", ip))
    return text


if __name__ == "__main__":
    report = "alice logged on from 192.0.2.10; later alice and bob used 192.0.2.10 again."
    out = redact(report, ["alice", "bob"], ["192.0.2.10"])
    print(out)
    assert "alice" not in out and "bob" not in out and "192.0.2.10" not in out
    assert out.count(pseudo("USER", "alice")) == 2, "same input must keep the same pseudonym"
    assert pseudo("USER", "alice") != pseudo("USER", "bob")
    print("PASS: identifiers are replaced consistently, so the narrative still correlates.")
    print("Review: redact metadata and screenshots too, and keep the key out of the report.")
