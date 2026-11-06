"""Synthetic evidence manifest and integrity verification in a temporary directory."""
import hashlib
import json
import tempfile
from pathlib import Path

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()

with tempfile.TemporaryDirectory(prefix="forensics-demo-") as tmp:
    root = Path(tmp)
    files = {"artifact-a.txt": "synthetic log event A\n",
             "artifact-b.txt": "synthetic log event B\n"}
    for name, contents in files.items():
        (root / name).write_text(contents, encoding="utf-8")

    manifest = {name: sha256(root / name) for name in files}
    print("Initial manifest:", json.dumps(manifest, indent=2))
    assert all(sha256(root / name) == expected for name, expected in manifest.items())

    (root / "artifact-b.txt").write_text("synthetic log event B (changed)\n", encoding="utf-8")
    result = {name: sha256(root / name) == expected for name, expected in manifest.items()}
    assert result == {"artifact-a.txt": True, "artifact-b.txt": False}
    print("Verification after controlled change:", json.dumps(result, indent=2))
print("Temporary files removed. No real evidence was read.")
