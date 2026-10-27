"""Tamper-evident chain-of-custody log using a SHA-256 hash chain (synthetic entries)."""
import hashlib
import json

def entry_hash(prev, record):
    payload = prev + json.dumps(record, sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()

def build(records):
    chain, prev = [], "0" * 64
    for record in records:
        prev = entry_hash(prev, record)
        chain.append({"record": record, "hash": prev})
    return chain

def verify(chain):
    prev = "0" * 64
    for index, item in enumerate(chain):
        prev = entry_hash(prev, item["record"])
        if prev != item["hash"]:
            return index
    return None

if __name__ == "__main__":
    log = build([
        {"item": "disk-01", "action": "acquired", "by": "analyst-a"},
        {"item": "disk-01", "action": "transferred", "by": "analyst-b"},
        {"item": "disk-01", "action": "stored", "by": "analyst-b"},
    ])
    print("intact chain, first bad entry:", verify(log))
    log[1]["record"]["by"] = "analyst-x"
    print("after edit, first bad entry:", verify(log))
    assert verify(log) == 1
    print("Note: a hash chain detects edits but not who made them; anchor the latest hash somewhere you trust.")
