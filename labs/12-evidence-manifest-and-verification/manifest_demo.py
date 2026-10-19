from pathlib import Path
import hashlib,json
p=Path("synthetic-evidence.txt")
p.write_bytes(b"harmless forensic example\n")
h=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
record={"filename":p.name,"sha256":h(p),"source":"synthetic"}
Path("manifest.json").write_text(json.dumps(record,indent=2))
assert h(p)==record["sha256"]
print("verified",record)
