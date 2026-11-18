# Day 41 — Execution Initiator Hypotheses and Abstention

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python exercise](initiator_demo.py)

## Follow-up to Day 40
Correlated timestamps and multiple log origins still do not prove **who initiated a process**. Day 41 builds a tiny classifier that deliberately refuses to guess when attribution evidence is missing or conflicting.

## Vocabulary
- **Initiator hypothesis:** a proposed explanation of what triggered an event.
- **Interactive context:** an event appears associated with an interactive session; a human action is *not* necessarily proven.
- **Scheduled/service context:** an event appears associated with task scheduler or service telemetry; this is not proof of which actor authored or scheduled it.
- **Abstention:** returning `UNKNOWN` or `AMBIGUOUS` rather than forcing a category.

Eight synthetic cases include one contextual indicator, contradictory indicators, missing process records, and missing event IDs. The code labels only **contexts**, not culprit identities. Even a scheduled job can be set up by a human, another automation system, or unauthorized activity.

## Reproduce
~~~bash
python3 labs/41-execution-initiator-hypotheses-and-abstention/initiator_demo.py
~~~

## Investigative questions
1. Why can a user session not prove a physical person clicked an executable?
2. Why does a scheduled task event not identify who created the task?
3. What independent process-parent, task-definition, logon or file-system records might test the hypothesis?
4. How should a report describe contradictory telemetry and clock skew?
5. Why is `UNKNOWN` sometimes the most accurate outcome?

## Limits
Only in-memory dictionaries, not Windows log parsing, evidence acquisition, or actor attribution. No claims about real incidents.
