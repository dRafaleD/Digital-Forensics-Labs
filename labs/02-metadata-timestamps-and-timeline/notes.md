# Day 2 — Metadata, Timestamps and Timeline Basics

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Goal

Learn how file metadata and timestamps can help reconstruct activity, while understanding that timestamps are evidence to interpret—not absolute truth.

This lab introduces:

- file metadata
- MACB-style timestamp terminology
- `stat`
- `touch`
- timestamp comparison
- simple timeline building
- timezone awareness
- metadata limitations
- documenting observations

## 1. What is metadata?

Metadata is data that describes other data.

For a file, metadata can include things such as:

- filename
- size
- ownership
- permissions
- timestamps
- filesystem identifiers
- extended attributes

Some file formats can also contain internal metadata, such as image EXIF data or document properties.

Filesystem metadata and file-format metadata are different sources of evidence.

## 2. Important timestamp concepts

On Linux filesystems, `stat` may show timestamps such as:

```text
Access
Modify
Change
Birth
```

A useful beginner mapping is:

- **Access time (atime):** when file content was last accessed, depending on mount/options.
- **Modify time (mtime):** when file content was last modified.
- **Change time (ctime):** when inode metadata/content-related status changed.
- **Birth/creation time:** when supported, when the filesystem object was created.

Important:

> Linux `ctime` is not "creation time".

It means inode **change** time.

## 3. Inspect metadata with stat

Use the harmless sample file:

```bash
stat evidence/timeline-sample.txt
```

Record:

- file size
- permissions
- owner/group
- Access time
- Modify time
- Change time
- Birth time, if available

Your filesystem may not expose every field.

## 4. Build a baseline

First calculate a hash:

```bash
sha256sum evidence/timeline-sample.txt
```

Then record metadata:

```bash
stat evidence/timeline-sample.txt > before-stat.txt
```

This gives you a baseline before performing a controlled change.

## 5. Modify a working copy

Create a copy:

```bash
cp evidence/timeline-sample.txt evidence/timeline-working.txt
```

Record metadata:

```bash
stat evidence/timeline-working.txt
```

Append a harmless line:

```bash
echo "Controlled modification" >> evidence/timeline-working.txt
```

Inspect again:

```bash
stat evidence/timeline-working.txt
sha256sum evidence/timeline-working.txt
```

Observe which timestamps changed.

## 6. Metadata-only changes

Change permissions on the working copy:

```bash
chmod 600 evidence/timeline-working.txt
```

Then:

```bash
stat evidence/timeline-working.txt
```

Ask:

- Did file content change?
- Did SHA-256 change?
- Did metadata timestamps change?

This is a useful demonstration that filesystem metadata can change even when file content does not.

## 7. touch and timestamps

The `touch` command can update timestamps.

Example on the working copy:

```bash
touch evidence/timeline-working.txt
stat evidence/timeline-working.txt
```

This matters in forensics because timestamps can be modified intentionally or as a side effect of normal system behavior.

Therefore:

> A timestamp is an observation to correlate with other evidence, not something to trust blindly.

## 8. Timezone awareness

A timeline can become misleading if timestamps from multiple systems are compared without considering timezone.

When recording findings, note:

- timezone
- UTC offset
- whether a tool displays local time or UTC
- whether timestamps came from different systems

Example:

```text
2026-09-29 10:00 UTC
2026-09-29 13:00 UTC+03
```

These can describe the same moment.

## 9. Create a simple forensic timeline

Create a small text table:

```text
Time                Event
------------------  ------------------------------
10:02:14            File copied
10:03:01            Working copy modified
10:03:20            SHA-256 recalculated
10:04:10            Permissions changed
```

For this lab, manually record actions as you perform them.

The goal is to practice ordering events, not to claim this is a complete forensic timeline.

## 10. File metadata vs content

Keep this distinction clear:

```text
content hash -> describes file bytes
metadata     -> describes filesystem/file attributes
```

Two files can have identical hashes but different:

- filenames
- paths
- owners
- permissions
- timestamps

This is common when files are copied.

## 11. Optional: file-format metadata

If `exiftool` is installed, inspect a harmless local file:

```bash
exiftool evidence/timeline-sample.txt
```

Text files may have little interesting format metadata. Later labs can use safe images or documents to study embedded metadata more meaningfully.

Do not assume embedded metadata is always accurate; it can be edited or stripped.

## 12. Metadata limitations

Timestamps and metadata can be affected by:

- copying
- extraction from archives
- filesystem behavior
- mount options
- backup/restore tools
- application behavior
- manual modification
- clock drift
- timezone differences

A forensic conclusion should therefore combine multiple evidence sources where possible.

## 13. Mini lab workflow

```text
1. Hash original sample
2. Record stat output
3. Create working copy
4. Modify working copy
5. Re-hash
6. Compare timestamps
7. Change permissions
8. Compare timestamps again
9. Build a small timeline
10. Document limitations
```

## 14. Questions

1. What is metadata?
2. What is the difference between mtime and ctime?
3. Why is Linux ctime not creation time?
4. Can metadata change without file content changing?
5. Can two files have the same SHA-256 but different timestamps?
6. Why is timezone important in timeline analysis?
7. Why should timestamps be correlated with other evidence?
8. What can `touch` demonstrate in a forensic lab?

## Main takeaway

A forensic timeline is built from evidence that must be interpreted carefully:

```text
metadata
   +
timestamps
   +
hashes
   +
documented actions
   ↓
better event reconstruction
```

Never treat one timestamp as the entire story.
