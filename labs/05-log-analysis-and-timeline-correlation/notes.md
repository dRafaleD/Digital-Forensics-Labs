# Day 5 — Log Analysis, Timeline Correlation and Event Reconstruction

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Goal

Learn how forensic analysts combine multiple logs into a single timeline and reconstruct a sequence of events without claiming more than the evidence supports.

This day combines log structure, timestamps, time zones, normalization, clock skew, event correlation, request IDs, missing-event awareness, hashing, and evidence-based reporting.

## 1. One log is only one viewpoint

Authentication, web, operating-system, firewall, database, and cloud logs may all describe different parts of the same incident.

A useful model is:

~~~
auth log
web log
system log
   ↓
normalize timestamps
   ↓
merge timeline
   ↓
correlate related events
   ↓
separate observation from inference
~~~

The goal is not simply to sort text. It is to understand what each source can actually prove.

## 2. Direct observation vs inference

If a log says:

~~~
LOGIN user=eren status=success
~~~

a careful statement is:

> The authentication log records a successful login for account eren.

That does not automatically prove which physical person was at the keyboard.

Forensic reporting should separate direct observations from broader interpretations.

## 3. Timestamps and time zones

This lab uses ISO 8601 timestamps such as:

~~~
2026-10-06T08:20:10+03:00
~~~

The +03:00 is a UTC offset.

When sources use different zones, normalize them for comparison, but preserve the original timestamp too.

Useful event-table fields:

- original timestamp
- normalized timestamp
- source
- event type
- account
- object
- result
- request ID
- notes

## 4. Clock skew

Two systems can disagree about time.

For example, one host may be two minutes fast.

That can make events look out of order.

Potential evidence for clock skew includes:

- NTP logs
- repeated request/response pairs
- known synchronization points
- stable offsets across many events

Do not silently correct timestamps. Document the basis for any adjustment.

## 5. Generate synthetic evidence

Run:

~~~bash
python3 create_log_evidence.py
~~~

It creates:

~~~
evidence/auth.log
evidence/web.log
evidence/system.log
~~~

These are harmless training logs.

Hash them before analysis:

~~~bash
sha256sum evidence/*.log
~~~

Save the baseline:

~~~bash
sha256sum evidence/*.log > evidence_hashes.sha256
~~~

## 6. Understand each source first

Inspect each file separately.

auth.log records authentication events.

web.log records application requests and request IDs.

system.log records service/file events.

Before merging, ask:

- What does this source record?
- What does it not record?
- What identity does it represent?
- What timestamp format does it use?

## 7. Build the timeline

Run:

~~~bash
python3 timeline.py
~~~

The script parses timestamps and sorts all events.

This gives a combined sequence such as:

~~~
service start
login success
web request
download request
file creation
logout
service stop
~~~

The script orders supplied timestamps. It does not prove causation.

## 8. Correlation vs causation

Suppose a successful login is followed by a report request and then a file creation.

You can say:

> These events occurred close together and share related context.

You cannot automatically say:

> The login caused the file creation.

Temporal proximity is correlation, not proof of causation.

## 9. Request IDs

The synthetic logs include request IDs such as req-18.

These can connect a web request to a system-side event more strongly than timestamp proximity alone.

Conceptually:

~~~
web.log: request_id=req-18
        ↓
system.log: request_id=req-18
~~~

Still verify scope and meaning. Identifiers are useful evidence, not magic truth.

## 10. Missing logs are ambiguous

No log entry can mean:

- event did not happen
- source does not record it
- logging was disabled
- collection missed it
- log rotation removed it
- data was deleted
- parser failed

Therefore:

~~~
no log entry != proof that an event never happened
~~~

## 11. Duplicate events

Repeated entries may represent:

- retries
- reconnects
- duplicate collection
- multiple layers logging one action

Do not equate line count with number of unique human actions.

## 12. Identity caution

A username identifies an account/context recorded by a system.

Prefer:

> Account eren requested /download.

over:

> Eren definitely downloaded the file personally.

Attribution needs additional evidence.

## 13. Hash and preserve

After analysis:

~~~bash
sha256sum -c evidence_hashes.sha256
~~~

If hashes still match, your source logs remain identical to the baseline.

This connects directly to Day 1 evidence-integrity practice.

## 14. Mini challenge — event table

Create at least six rows with:

~~~
Original Time
Normalized Time
Source
Event
Account
Request ID
Result
Observation
Inference
~~~

Leave fields blank when the evidence does not support them. Do not fill gaps with guesses.

## 15. Mini challenge — clock skew

Make a working copy of one log and shift every timestamp by +2 minutes.

Then merge again.

Answer:

- Which sequence becomes misleading?
- How could you detect the offset?
- How would you document the correction?
- Why should the original evidence remain unchanged?

## 16. Mini challenge — case summary

Using only the synthetic evidence, write a short case summary containing:

1. direct observations,
2. one or two supported inferences,
3. explicit limitations,
4. hashes of the source logs.

## 17. Reporting language

Good wording:

> The web log records a GET request for /download?id=17 at 08:21:32+03:00 with request_id=req-18.

Supported inference:

> A system log event with the same request ID records report17.txt creation shortly afterward.

Unsupported:

> The account owner intentionally created and downloaded the report.

The last statement goes beyond the evidence provided.

## 18. Workflow

~~~
preserve
  ↓
hash
  ↓
understand each log source
  ↓
parse timestamps
  ↓
normalize carefully
  ↓
merge timeline
  ↓
correlate IDs/events
  ↓
separate observation from inference
  ↓
report limitations
~~~

## Exercises

1. Generate the synthetic logs.
2. Hash all three.
3. Inspect each source separately.
4. Run the timeline script.
5. Build a six-row event table.
6. Correlate req-18 across sources.
7. Write three direct observations.
8. Write two supported inferences.
9. Identify two things the logs cannot prove.
10. Perform the clock-skew challenge.
11. Verify hashes after analysis.
12. Write a short case summary.

## Questions

1. Why combine multiple log sources?
2. Why preserve original timestamps?
3. What does timezone normalization solve?
4. What is clock skew?
5. Why is correlation not causation?
6. What can request IDs help with?
7. Why can missing logs be ambiguous?
8. Why is a username not proof of physical identity?
9. What does hashing add to log analysis?
10. Why should reports separate observation from inference?

## Main takeaway

Timeline analysis is not just sorting rows by time.

It is:

~~~
multiple partial sources
        ↓
time normalization
        ↓
correlation
        ↓
careful reasoning
        ↓
evidence-based reporting
~~~
