from pathlib import Path
import hashlib,shutil
src=Path("synthetic_original.txt");dst=Path("working_copy.txt")
src.write_text("safe lab evidence\n",encoding="utf-8")
shutil.copy2(src,dst)
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
print("copy matches",digest(src)==digest(dst))
dst.write_text("modified working copy\n",encoding="utf-8")
print("after change",digest(src)==digest(dst))
