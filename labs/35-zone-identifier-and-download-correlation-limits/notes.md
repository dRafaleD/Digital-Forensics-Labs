# Day 35 — Zone.Identifier and Browser Download Correlation Limits

[English](notes.md) · [Türkçe](notes.tr.md) · [Synthetic correlator](download_correlation_demo.py)

## Beyond process-file timing
Day 34 connected **USN-like file events** with invented process-file telemetry and showed why a close timestamp is not proof of causation. Here we add two common **Windows investigation concepts**: browser download history and the NTFS **Zone.Identifier** alternate data stream (ADS).

Some Windows applications add Mark-of-the-Web metadata to downloaded files. The Zone.Identifier stream may contain **ZoneId** (for example, ZoneId=3 for an Internet-zone association) and sometimes source URL fields. It is not guaranteed to exist: browsers, programs, filesystems, transfers, extraction and policy can affect whether this metadata is present or retained.

A browser history record may indicate that software recorded a download. Neither a browser event nor an ADS entry, even together, inherently identifies the human who initiated the action, proves an AI agent acted, or proves the downloaded file executed.

## Three kinds of evidence
1. **Download-history event:** reported target path, time and URL. Source semantics depend on the browser and collection method.
2. **Zone.Identifier-like observation:** file path, collection-related time and reported zone. Real Zone.Identifier metadata is not by itself an authoritative download timestamp; this fixture uses fabricated observation times.
3. **Potential link:** shared path and close timestamps may yield one, several, or no candidates. The correlation is a **hypothesis**, not confirmed actor attribution. Files can be renamed, replaced, copied or duplicated.

## Offline experiment
~~~bash
python3 download_correlation_demo.py
~~~

The script uses a ±2-second illustrative window and fictitious paths. Three zone observations yield: one candidate, multiple possible candidates and no candidate. It prints evidence IDs and always leaves **initiator unknown**.

## Exercises
1. Why can a missing Zone.Identifier stream fail to disprove a download?
2. What does an Internet-zone label tell you, and what does it not tell you?
3. Explain why matching just a filename is weaker than preserved object identity plus trustworthy timestamps.
4. Add an independent hash or file-reference field to the data; document what additional confidence it actually provides.
5. How might copying to a non-NTFS filesystem change available evidence?
6. What additional sources (browser database, process creation, USN, Prefetch, Sysmon, Zone.Identifier, web proxy logs) would you correlate for known-ground-truth research?

## Safety and limits
No real Windows history, ADS, NTFS journal or browser data is accessed. This is not an ADS parser or a forensic collection tool. Do not equate close timestamps with causation or automatically label an actor as human, automation, agent or malware.
