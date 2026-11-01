"""Carve synthetic 'files' from a byte blob using made-up header/footer markers."""
HEADER = b"\xDE\xAD\x01TRAIN"
FOOTER = b"END\x01\xBE\xEF"

BLOB = b"junk" * 3 + HEADER + b"payload-one" + FOOTER + b"gap" + HEADER + b"payload-two-no-footer"

def carve(blob):
    results, pos = [], 0
    while (start := blob.find(HEADER, pos)) != -1:
        end = blob.find(FOOTER, start)
        if end == -1:
            results.append((start, None, "header without footer"))
            break
        results.append((start, end + len(FOOTER), "complete"))
        pos = end + len(FOOTER)
    return results

if __name__ == "__main__":
    for start, end, status in carve(BLOB):
        print(f"offset={start} end={end} {status}")
    assert len(carve(BLOB)) == 2
    print("Note: carving recovers byte ranges, not provenance; a carved range still needs validation and context.")
