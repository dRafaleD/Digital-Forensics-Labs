"""Order collection of synthetic evidence sources by volatility and value."""
SOURCES = [
    {"name": "RAM contents", "lifetime_s": 0, "value": 9},
    {"name": "Network connections", "lifetime_s": 60, "value": 8},
    {"name": "Running processes", "lifetime_s": 60, "value": 8},
    {"name": "Temp files", "lifetime_s": 86400, "value": 5},
    {"name": "Disk image", "lifetime_s": 10**9, "value": 9},
    {"name": "Offsite backups", "lifetime_s": 10**10, "value": 4},
]


def collection_order(sources):
    return sorted(sources, key=lambda s: (s["lifetime_s"], -s["value"]))


if __name__ == "__main__":
    order = [s["name"] for s in collection_order(SOURCES)]
    for i, name in enumerate(order, 1):
        print(i, name)
    assert order[0] == "RAM contents"
    assert order.index("Network connections") < order.index("Disk image")
    print("PASS: the most volatile evidence is collected first.")
    print("Review: collecting RAM alters the system; document every action you take.")
