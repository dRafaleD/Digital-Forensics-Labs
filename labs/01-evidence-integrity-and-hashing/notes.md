# Day 1 — Digital Evidence, Integrity and Hashing

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Goal

Learn the first forensic habit: **preserve evidence before analyzing it**.

This lab introduces:

- digital evidence
- original vs working copy
- acquisition vs analysis
- evidence integrity
- cryptographic hashes
- SHA-256
- chain of custody as a documentation concept
- repeatable verification

## 1. What is digital evidence?

Digital evidence is information stored or transmitted in digital form that can help answer an investigative question.

Examples include:

- files
- logs
- disk images
- memory captures
- browser artifacts
- network captures
- metadata
- timestamps

Not every file is automatically evidence. It becomes relevant when it is connected to an investigation or question.

## 2. Preserve first, analyze second

A core forensic principle is to avoid changing the original material unnecessarily.

A simple mental model:

```text
original evidence
      ↓
preserve
      ↓
create working copy
      ↓
verify copy
      ↓
analyze copy
```

In professional workflows, acquisition can involve specialized tools and procedures. For this beginner lab, we use a harmless text file so the integrity concept is easy to observe.

## 3. Original vs working copy

For this lab:

```text
evidence/original.txt
```

acts as our original evidence.

Create a working copy:

```bash
cp evidence/original.txt evidence/working-copy.txt
```

Do your experiments on the working copy rather than intentionally modifying the original.

## 4. What is a cryptographic hash?

A hash function takes input data and produces a fixed-size digest.

Conceptually:

```text
file bytes
   ↓
SHA-256
   ↓
digest
```

If the file changes, the digest will normally change as well.

Hashes are useful for checking whether two byte streams are identical.

## 5. Calculate SHA-256

Linux:

```bash
sha256sum evidence/original.txt
sha256sum evidence/working-copy.txt
```

If both files are exact copies, the SHA-256 values should match.

You can also generate a verification file:

```bash
sha256sum evidence/original.txt > hashes.sha256
```

Verify later:

```bash
sha256sum -c hashes.sha256
```

Expected result:

```text
evidence/original.txt: OK
```

## 6. Integrity experiment

First record the hashes:

```bash
sha256sum evidence/original.txt evidence/working-copy.txt
```

Then modify **only the working copy**:

```bash
echo "Training modification" >> evidence/working-copy.txt
```

Hash again:

```bash
sha256sum evidence/original.txt evidence/working-copy.txt
```

The digests should now differ.

This demonstrates an important principle:

> A hash can help show that the bytes changed.

It does not explain **why** the file changed or **who** changed it.

## 7. Hashes are not filenames

These two files can have different names but identical content:

```text
original.txt
copy.txt
```

If the bytes are identical, their SHA-256 hashes are identical.

Likewise, two files with the same filename can have different content and therefore different hashes.

Forensics cares about the data itself, not only the filename.

## 8. Acquisition vs analysis

These are different stages.

### Acquisition

Acquisition means obtaining a forensic copy or capture of the data to be examined.

### Analysis

Analysis means examining that acquired data to answer investigative questions.

Keeping these stages conceptually separate helps protect the source material and makes the workflow easier to document.

## 9. Chain of custody

Chain of custody is the record of how evidence was collected, transferred, stored, and handled.

A simplified training log may record:

```text
Evidence ID:
Description:
Collected by:
Date/time:
Source:
Hash:
Copy created:
Analysis notes:
```

The point is traceability.

A hash is useful evidence-integrity information, but it does not replace documentation.

## 10. Create a simple evidence log

Create:

```text
evidence-log.txt
```

Example:

```text
Evidence ID: DF-LAB-001
Description: Harmless training text file
Source: Local lab repository
Original file: evidence/original.txt
Hash algorithm: SHA-256
Original SHA-256: <paste your result>
Working copy: evidence/working-copy.txt
Notes: Working copy used for modification experiment
```

Do not copy someone else's hash result. Generate yours locally.

## 11. Why SHA-256?

SHA-256 is widely available and appropriate for integrity verification in this learning context.

Older hash functions such as MD5 and SHA-1 may still appear in forensic tooling and historical datasets, but they have known collision weaknesses and should not be treated as modern collision-resistant choices.

For this repository, SHA-256 will be the default unless a lab specifically studies something else.

## 12. Useful commands

Inspect file metadata:

```bash
stat evidence/original.txt
```

Compare files byte-for-byte:

```bash
cmp evidence/original.txt evidence/working-copy.txt
```

If there is no output, `cmp` found no difference.

After modifying the working copy, run it again.

## 13. Mini lab workflow

Perform this sequence:

```text
1. Inspect original
2. Hash original
3. Copy original
4. Hash copy
5. Confirm hashes match
6. Record information
7. Modify only the copy
8. Hash again
9. Observe the difference
10. Keep the original unchanged
```

## 14. Questions

1. Why should the original evidence be preserved?
2. What is the difference between acquisition and analysis?
3. What does a matching SHA-256 hash tell you?
4. Does a hash prove who changed a file?
5. Why should experiments be performed on a working copy?
6. Why are filenames alone not enough to establish file identity?
7. What is the purpose of chain-of-custody documentation?
8. Why are MD5 and SHA-1 not preferred as modern collision-resistant hashes?

## Main takeaway

The first forensic habit is not "open the file and start clicking."

It is:

```text
preserve
   ↓
copy
   ↓
hash
   ↓
verify
   ↓
document
   ↓
analyze
```

A good forensic workflow protects the original data and makes your actions repeatable and explainable.
