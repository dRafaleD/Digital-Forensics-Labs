"""Triage synthetic files against a known-good hash set, keeping the limits explicit."""
import hashlib

FILES = {
    "readme.txt": b"hello training data\n",
    "notes.txt": b"meeting notes\n",
    "readme_copy.txt": b"hello training data\n",
    "renamed.dat": b"meeting notes \n",  # one trailing space: different bytes, different hash
}
KNOWN_GOOD = {hashlib.sha256(b"hello training data\n").hexdigest()}

def triage(files, known):
    rows = []
    for name, data in files.items():
        digest = hashlib.sha256(data).hexdigest()
        rows.append((name, digest[:12], "known-good" if digest in known else "needs review"))
    return rows

if __name__ == "__main__":
    for name, short, status in triage(FILES, KNOWN_GOOD):
        print(f"{name:16} {short} {status}")
    print("Note: a hash match only shows identical bytes; it says nothing about how the file was used or where it was found.")
