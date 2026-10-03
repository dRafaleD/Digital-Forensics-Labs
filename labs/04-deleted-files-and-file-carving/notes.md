# Day 4 — Deleted Files, Filesystem Metadata and File Carving Foundations

## Goals
Understand what “delete” means at filesystem level, distinguish metadata-based recovery from file carving, work only on a disposable image, preserve evidence integrity with hashes, and document what your observations do and do not prove.

## 1. Deletion is not the same as secure erasure
Deleting a file often removes or changes filesystem metadata that points to its content. The underlying data blocks may remain until they are reused. Recovery therefore depends on filesystem behavior, later writes, fragmentation, storage technology and acquisition quality.

Never assume that a deleted file is recoverable, and never assume that a recovered byte sequence proves who created or deleted it.

## 2. Metadata-based recovery
Filesystems track information such as names, directory entries, inode/MFT-style records, allocation state, sizes and timestamps. If enough metadata survives, a forensic tool may associate recovered content with useful filesystem context.

On EXT filesystems, inodes describe file metadata and block references; directory entries associate names with inode numbers. Deletion changes these relationships and allocation state.

## 3. File carving
Carving searches raw data for recognizable file structures/signatures rather than relying on live filesystem metadata. For example, a carver may identify a known header and footer or use format-aware parsing.

Advantages:
- can find content when directory metadata is missing
- can operate on unallocated/raw regions

Limitations:
- filenames/paths may be lost
- timestamps may be unavailable
- fragmentation can break recovery
- signatures can create false positives
- recovered bytes alone have limited attribution value

## 4. Evidence workflow
Use this order:
1. create/acquire a disposable evidence image
2. calculate SHA-256
3. make a working copy
4. verify the working copy hash
5. analyze the copy
6. record commands and findings
7. hash the preserved source again if appropriate

## 5. Safe local lab setup
This lab creates a small image file, not a physical disk.

Requirements on Linux:
- `dd`
- `mkfs.ext4`
- `debugfs`
- `sha256sum`
- optionally `file`, `xxd`, `strings`

Create a 32 MiB image:
```bash
mkdir -p day4-lab
cd day4-lab
dd if=/dev/zero of=evidence.img bs=1M count=32 status=progress
mkfs.ext4 -F evidence.img
sha256sum evidence.img | tee evidence-before.sha256
cp evidence.img working.img
sha256sum working.img
```
The two hashes should initially match.

## 6. Put known test files into the image without mounting
Create harmless samples:
```bash
printf 'FORENSICS_DAY4_MARKER_A\nCase: training-only\n' > note-a.txt
printf 'FORENSICS_DAY4_MARKER_B\nDeleted sample\n' > note-b.txt
```

Use debugfs in write mode only on the **working image**:
```bash
debugfs -w working.img
```
Inside debugfs:
```text
mkdir /case
write note-a.txt /case/note-a.txt
write note-b.txt /case/note-b.txt
ls -l /case
stat /case/note-b.txt
rm /case/note-b.txt
ls -l /case
quit
```
Record the inode number shown before deletion if available.

Important: the original `evidence.img` remains untouched. This exercise intentionally modifies `working.img` to simulate an event.

## 7. Examine deletion artifacts
First inspect filesystem metadata:
```bash
debugfs -R 'ls -l /case' working.img
debugfs -R 'lsdel' working.img
```
Behavior can vary with filesystem/tool version. Treat `lsdel` output as an observation, not a guarantee of recovery.

Search for your unique marker in the working image:
```bash
grep -a -b 'FORENSICS_DAY4_MARKER_B' working.img
strings -a -t d working.img | grep 'FORENSICS_DAY4_MARKER'
```
If the marker remains, that demonstrates bytes are still discoverable in this controlled image; it does **not** by itself reconstruct the original filename, path, timestamp or actor.

## 8. Raw-byte inspection
If `grep -a -b` gives an offset, inspect a small region around it with a hex viewer such as `xxd`. Keep the read bounded and record the offset. This connects filesystem concepts with raw storage.

## 9. Metadata recovery vs carving
Write a comparison:
| Question | Metadata-based recovery | Carving |
|---|---|---|
| Uses filesystem records? | Usually yes | Not required |
| May preserve filename/path? | Sometimes | Usually no |
| Handles missing directory entry? | Sometimes | Potentially |
| Sensitive to fragmentation? | Yes | Often strongly |
| Attribution proof by itself? | No | No |

## 10. Integrity check
Verify that the preserved source has not changed:
```bash
sha256sum -c evidence-before.sha256
```
Then hash the modified working image:
```bash
sha256sum working.img
```
Its hash should differ because you intentionally changed the working copy. Explain why this is expected rather than an integrity failure of the preserved source.

## 11. Questions
1. Why can deleted data sometimes remain on disk?
2. What is the role of an inode and a directory entry in EXT filesystems?
3. Why can carving lose filenames and timestamps?
4. How does fragmentation affect carving?
5. Why is a unique string marker useful in a controlled lab?
6. What does a matching SHA-256 prove, and what does it not prove?
7. Why analyze a working copy instead of the original?
8. Why must conclusions distinguish “bytes were found” from “this exact file existed at this path at this time”?

## 12. Report template
Record:
- image name and size
- original SHA-256
- working-copy initial SHA-256
- commands used
- inode/metadata observations
- marker offsets
- recovered content, if any
- final working-copy SHA-256
- limitations
- conclusion with confidence level

## Takeaway
Deleted-file forensics is a combination of filesystem metadata, allocation state and raw bytes. Recovery is not magic: every conclusion should be tied to observable evidence, integrity checks and explicit limitations.
