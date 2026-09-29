# Day 3 — Filesystem and Disk Image Fundamentals

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Goal

Learn what a filesystem image is, why forensic analysis usually works from an acquired image instead of directly modifying original media, and how to inspect a small harmless EXT4 image while preserving its integrity.

This lab introduces:

- block devices and filesystems
- logical files vs raw storage
- disk/filesystem images
- acquisition vs analysis
- image hashing
- EXT4 basics
- read-only examination
- `file`, `dumpe2fs`, and `debugfs`
- evidence integrity before and after analysis

The lab creates a tiny image file locally. It does **not** require imaging a real disk.

## 1. Storage layers

A beginner-friendly model:

```text
physical / virtual storage
          ↓
partition
          ↓
filesystem
          ↓
directories and files
          ↓
application data
```

These layers are related but not identical.

A disk can contain a partition table. A partition can contain a filesystem. The filesystem organizes files, directories, metadata and allocation information.

## 2. What is a filesystem?

A filesystem defines how data and metadata are organized on storage.

Examples include:

- EXT4
- NTFS
- FAT32
- exFAT
- XFS

A filesystem tracks more than filenames. Depending on the filesystem it may store:

- directory structure
- timestamps
- ownership
- permissions
- allocation information
- filesystem-specific metadata

This is why filesystem analysis can reveal information that is not visible by simply opening a folder in a file manager.

## 3. What is a disk image?

A forensic image is a representation of storage acquired for examination.

Conceptually:

```text
source media
     ↓ acquisition
image file
     ↓ verification
working analysis
```

Depending on acquisition method and format, an image can represent an entire device, a partition, or another storage scope.

This lab uses a small raw filesystem image created specifically for training.

## 4. Logical copy vs image

A normal file copy focuses on selected files:

```text
folder/file -> copied file
```

An image can preserve lower-level filesystem/storage structures within the acquired scope.

Therefore:

```text
logical copy != raw/filesystem image
```

Neither is universally “better”; the correct acquisition method depends on the investigation, authority, system state and evidence requirements.

## 5. Create harmless seed data

Create a lab directory:

```bash
mkdir -p lab03-work/seed
cd lab03-work
```

Create two harmless files:

```bash
printf "Digital Forensics Lab 03\nEvidence: harmless training file\n" > seed/note.txt
printf "case_id=DF-LAB-003\nstatus=training\n" > seed/case.txt
```

Inspect them:

```bash
ls -l seed
sha256sum seed/*
```

## 6. Create a small EXT4 image

Create a 32 MiB regular file:

```bash
truncate -s 32M lab-disk.img
```

Format that **regular file** as EXT4 and populate it from the seed directory:

```bash
mkfs.ext4 -q -L DF_LAB03 -d seed lab-disk.img
```

Important safety rule:

> Use the command only with the lab image file you created. Do not replace `lab-disk.img` with a real disk or partition.

Formatting the wrong target can destroy data.

## 7. Establish image integrity

Once the training image is created, treat it as your evidence image.

Calculate its SHA-256:

```bash
sha256sum lab-disk.img
```

Save the result:

```bash
sha256sum lab-disk.img > lab-disk.sha256
```

From this point onward, avoid modifying the image.

This connects directly to Day 1:

```text
create/acquire
     ↓
hash
     ↓
preserve
     ↓
analyze
     ↓
verify again
```

## 8. Identify the image

Run:

```bash
file lab-disk.img
```

The output should identify an EXT filesystem.

This is a first identification step, not a complete forensic conclusion.

## 9. Inspect EXT4 metadata

If `dumpe2fs` is available:

```bash
dumpe2fs -h lab-disk.img
```

Look for fields such as:

- filesystem volume name
- filesystem UUID
- filesystem features
- block size
- inode count
- block count
- creation information

Do not try to memorize every field. First learn what kinds of metadata a filesystem exposes.

## 10. Block and inode idea

EXT filesystems divide storage into blocks and use inode structures to describe filesystem objects.

A simplified mental model:

```text
directory entry
     ↓
inode
     ↓
metadata + references to file data
     ↓
data blocks
```

An inode is not simply “the filename.” Directory entries associate names with inode numbers.

This distinction becomes important later when studying deleted files and filesystem artifacts.

## 11. Examine without mounting

`debugfs` can inspect an EXT filesystem image directly.

List the root directory:

```bash
debugfs -R "ls -l /" lab-disk.img
```

Read the harmless training file:

```bash
debugfs -R "cat /note.txt" lab-disk.img
```

Read the second file:

```bash
debugfs -R "cat /case.txt" lab-disk.img
```

This demonstrates that files can be examined from a filesystem image without browsing it like a normal mounted directory.

## 12. Optional read-only mount

On a Linux lab machine, you can optionally mount the image read-only:

```bash
mkdir -p mountpoint
sudo mount -o loop,ro lab-disk.img mountpoint
ls -la mountpoint
cat mountpoint/note.txt
sudo umount mountpoint
```

The important option is:

```text
ro = read-only
```

For forensic work, reducing unnecessary writes is a core habit.

A software read-only mount is useful for training, but professional acquisition workflows may also use hardware/software write blockers and specialized tools.

## 13. Verify after examination

After analysis:

```bash
sha256sum -c lab-disk.sha256
```

Expected result:

```text
lab-disk.img: OK
```

If the hash is unchanged, the image bytes match the baseline hash.

Remember the limitation from Day 1: a hash can show that bytes match a known baseline; it does not explain who handled the evidence or whether acquisition itself was correct.

## 14. Why read-only matters

Opening evidence through normal tools can sometimes cause writes, depending on operating system, filesystem, mount mode and application behavior.

Potential changes can include metadata or application-generated files.

The forensic mindset is therefore:

```text
do not ask only:
"Can I open it?"

also ask:
"Will this action modify evidence?"
```

## 15. Acquisition vs analysis

Keep the phases separate:

### Acquisition
Obtain the evidence representation while minimizing alteration and documenting the process.

### Verification
Use hashes and records to confirm the evidence being analyzed matches the acquired baseline.

### Analysis
Examine the verified copy/image using appropriate tools.

### Reporting
Document what was observed, how it was observed and the limitations.

## 16. Evidence notes

Use `image-analysis-template.txt` from this lab to record:

- image name
- image size
- SHA-256
- filesystem type
- volume label
- tools used
- read-only status
- observations
- final verification result

This is intentionally simple. Later labs can use more formal case documentation.

## 17. What this lab does not prove

Finding `note.txt` inside the image proves only what the examination supports.

It does not automatically prove:

- who created the file,
- who used the computer,
- why the file exists,
- whether a timestamp represents human activity,
- whether the original acquisition was legally/procedurally valid.

Forensics requires careful wording.

Prefer:

> “The examined image contained a file named note.txt.”

over unsupported claims about a person or intent.

## 18. Security/forensics connection

Filesystem images are useful because analysts can inspect:

- files and directories
- filesystem metadata
- allocation structures
- timestamps
- deleted-file artifacts in later labs
- filesystem-specific evidence

without treating the original storage as a normal working disk.

## Mini lab workflow

```text
create harmless seed files
        ↓
create EXT4 training image
        ↓
calculate SHA-256 baseline
        ↓
identify filesystem
        ↓
inspect metadata
        ↓
read files with debugfs
        ↓
optional read-only mount
        ↓
verify SHA-256 again
        ↓
document observations
```

## Exercises

1. Create the 32 MiB training image.
2. Record its SHA-256.
3. Identify the filesystem with `file`.
4. Find the volume label with `dumpe2fs -h`.
5. List the root directory using `debugfs`.
6. Read `note.txt` without mounting the image.
7. Record an inode number shown by `debugfs`.
8. Optionally mount the image read-only and inspect it.
9. Verify the original image hash after analysis.
10. Explain why a logical file copy and filesystem image are different.

## Questions

1. What is a filesystem?
2. What is a filesystem/disk image?
3. Why should an evidence image be hashed?
4. What does read-only examination try to prevent?
5. What is the basic role of an inode in EXT filesystems?
6. Is an inode the same thing as a filename?
7. Why is acquisition different from analysis?
8. What does an unchanged SHA-256 prove—and what does it not prove?
9. Why should you avoid formatting or writing to real devices during this lab?
10. Why should forensic conclusions use careful wording?

## Main takeaway

```text
storage
   ↓
filesystem
   ↓
forensic image
   ↓
hash + preserve
   ↓
read-only examination
   ↓
verify + document
```

The most important habit is not the command syntax. It is preserving the evidence and knowing what your observations actually support.
