# Day 33 — NTFS USN Journal: File Changes vs. Actor Attribution

[English](notes.md) · [Türkçe](notes.tr.md) · [Synthetic timeline](usn_timeline_demo.py)

## A file change is not an actor identity
Day 32 showed that two sources can disagree about the same artifact. Today we study a **Windows NTFS change-journal concept** relevant to that problem. The NTFS `$UsnJrnl` records change notifications for files and directories on a volume. An entry can help establish that a filesystem object changed; it does **not** by itself identify the user, process or application that initiated the operation.

## Read the fields carefully
A USN record can contain a file reference, parent reference, change-reason flags, filename and timestamp. The **USN** is a journal position/order value within a particular journal, **not** a timestamp and **not** necessarily a consecutive event counter. Real reason flags are bitfields and may accumulate across operations. A filename is not a stable unique identifier: different file objects can have the same name at different points.

Journal records may be missing because of retention/rotation, disabled journaling, collection scope or other causes. **A gap in numbers alone is not proof of deletion or tampering.** Collection integrity and the volume/journal context matter.

## Harmless simulation
The included script builds fictional records for a file called `model.bin`, groups them by a simplified file reference ID, and orders events by USN. A second file object intentionally shares the same filename, illustrating why filename-only correlation is unsafe. The report explicitly labels the **initiator as unknown**.

```bash
python3 usn_timeline_demo.py
```
This is an offline simulation; it does not read `$UsnJrnl`, parse NTFS or access a Windows disk.

## Investigation
1. Which observations concern the same file reference? Which do not?
2. Why is an event with a larger USN not proof that it has a later wall-clock timestamp?
3. Can `FILE_CREATE` establish a **download**? What other sources would you check?
4. Suggest correlations with Sysmon process activity, browser download history, `Zone.Identifier` or Windows Event Logs, noting any limitations.
5. What could a journal rollover hide? How would you report that uncertainty?
6. Draw a table separating **observed artifact**, **hypothesis**, **corroboration required**, and **attribution confidence**.

## Forensic boundary
Do not claim “human”, “agent”, “automation”, or “malware” solely from a USN event. Real acquisition requires authorized access, a defensible collection method, volume context and evidence hashing. This lab is not a forensic parser or an accuracy benchmark.
