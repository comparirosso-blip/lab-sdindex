# QC Workflow

This document defines the standard quality-control workflow for SDIndex / CKV fieldwork records.

The goal of QC is not to produce more interpretation.  
The goal is to detect structural, semantic, and methodological instability before a record is elevated into `canonical_records/`.

QC is therefore a **governance process**, not a writing exercise.

---

## 1. Core Principle

Not every fieldwork record requires the same QC questions.

However, QC should not be improvised from scratch for each record.

The workflow therefore follows this logic:

1. run a **risk scan**
2. activate the relevant **QC modules**
3. generate a **focused question set**
4. perform a **primary QC review**
5. perform a **challenge review**
6. produce a **QC synthesis note**

This ensures both flexibility and consistency.

---

## 2. QC Objectives

QC exists to identify issues such as:

- field / vocabulary mismatch
- site typing errors
- score–subtype inconsistency
- dimension overlap
- Ve trigger ambiguity
- external narrative over-dependence
- observation / inference boundary instability
- emotion trajectory instability
- underdeveloped research finding
- underspecified ideal condition

QC does **not** exist to reward beautiful prose or to generate general praise.

---

## 3. Workflow Overview

```text
Fieldwork Record
  ↓
QC Intake Scan
  ↓
Risk Tags
  ↓
QC Module Activation
  ↓
Dynamic QC Question Set
  ↓
Primary QC Review
  ↓
Challenge QC Review
  ↓
QC Synthesis
  ↓
Decision:
- pass
- pass_with_notes
- hold_for_revision
- hold_for_qc_note_only
4. Role Architecture

The workflow uses differentiated LLM roles rather than parallel undirected review.

Role A — QC Intake Scanner

Purpose:

summarize the record type

detect top risk areas

assign QC risk tags

decide which QC modules to activate

This role does not do full QC.

Role B — Dynamic QC Question Designer

Purpose:

generate a record-specific QC question set

select only the relevant questions

organize questions by QC category

This role does not judge the record.

Role C — Primary QC Reviewer

Purpose:

answer the QC questions directly

identify confirmed and possible issues

recommend edits or note-only actions

This is the main reviewing role.

Role D — Challenge QC Reviewer

Purpose:

challenge the most questionable conclusions in the Primary QC Review

identify overreach, underreach, or weak evidence

refine the reliability of the QC result

This role is not a second full review.

Role E — QC Synthesis Editor

Purpose:

integrate all upstream QC outputs

convert them into one usable governance decision

produce final QC status and canonical recommendation

5. QC Risk Tags

The following tags are used during intake scan.

risk_site_typing

risk_vocab_mismatch

risk_score_subtype_misalignment

risk_dimension_overlap

risk_ve_trigger_ambiguity

risk_external_narrative_dependency

risk_inference_exceeds_observation

risk_emotion_trajectory_instability

risk_research_finding_underdeveloped

risk_ideal_condition_underspecified

Additional risk tags may be added later, but should be documented explicitly.

6. QC Modules

Each QC risk tag activates one or more QC modules.

M1 — Site Typing

Checks:

whether site.site_type matches the actual nature of the site

whether the chosen type will distort future classification or graph relations

M2 — Vocabulary Alignment

Checks:

whether values match controlled vocabularies

whether free-text values appear where a controlled term should be used

M3 — Score–Subtype Consistency

Checks:

whether score intensity and chosen subtype align

whether a high or low score conflicts with the explanatory subtype

M4 — Dimension Boundary

Checks:

whether Vt / Vl / Vr / Vg / Ve reasoning is sufficiently differentiated

whether multiple dimensions are collapsed into one field note

M5 — Ve Trigger Logic

Checks:

whether the assigned Ve_trigger matches the actual emotional turning point

whether dual-trigger conditions may be present

whether AI / human narrative supplementation altered attribution

M6 — Emotion Trajectory Logic

Checks:

whether entry / turning / exit states form a coherent progression

whether the turning point is sufficiently evidenced

M7 — Observation vs Inference

Checks:

whether the record clearly distinguishes direct observation from interpretive projection

whether historical, symbolic, or psychological claims exceed available evidence

M8 — AI Narrative Interference

Checks:

whether external AI supplementation changes post-observation framing

whether the record remains clear about what was felt onsite versus learned later

M9 — Research Finding Quality

Checks:

whether research_finding is analytically meaningful

whether it states a usable insight rather than a vague impression

M10 — Ideal Condition Quality

Checks:

whether ideal_condition reflects actual spatial conditions

whether it is useful for future comparison or Graph RAG parsing

7. QC Categories

All generated QC questions should be grouped into three categories.

A. Structural QC

Focus:

schema alignment

field usage

controlled vocabularies

obvious record structure issues

B. Semantic QC

Focus:

dimension logic

trigger logic

score interpretation

emotional coherence

C. Epistemic Boundary QC

Focus:

direct observation versus inference

post-hoc narrative supplementation

interpretive overreach

AI-mediated reframing

8. SOP Step-by-Step
Step 1 — Intake Scan

The Intake Scanner reads the record and outputs:

record type summary

top 3–5 risk tags

why each risk tag matters

which QC modules should be activated

This step should remain concise.

Intake Scan Prompt
Role: QC Intake Scanner for SDIndex / CKV fieldwork records

Task:
Read the following fieldwork record and identify its QC risk profile.

Do not perform full analysis.
Do not rewrite the record.
Do not give general praise.

Output only:

1. Record type summary
2. Top 3-5 QC risk tags
3. Why each risk tag matters
4. Which QC modules should be activated

Available risk tags include:
- risk_site_typing
- risk_vocab_mismatch
- risk_score_subtype_misalignment
- risk_dimension_overlap
- risk_ve_trigger_ambiguity
- risk_external_narrative_dependency
- risk_inference_exceeds_observation
- risk_emotion_trajectory_instability
- risk_research_finding_underdeveloped
- risk_ideal_condition_underspecified

Return concise and structured output.
Step 2 — Dynamic QC Question Set

The Question Designer generates only the questions necessary for this specific record.

Target range:

6 to 10 questions total

Each question should include:

question_id

question

target_field

qc_type

why_this_question_matters

Dynamic QC Question Designer Prompt
Role: Dynamic QC Question Designer for SDIndex / CKV records

Task:
Based on the QC risk profile, generate a focused QC question set for this specific record.

Instructions:
- Generate only questions that are necessary for this record.
- Group questions into:
  A. Structural QC
  B. Semantic QC
  C. Epistemic Boundary QC
- Avoid generic questions.
- Each question must target one clear issue.
- Prefer 6-10 questions total.
- Questions must be answerable from the record itself.

For each question, provide:
- question_id
- question
- target_field
- qc_type
- why_this_question_matters
Step 3 — Primary QC Review

The Primary QC Reviewer answers the generated QC questions.

For each question, the reviewer must state:

judgment

evidence from record

risk_level

recommended_action

Allowed judgments:

no_issue

minor_issue

moderate_issue

major_issue

unresolved

At the end, the reviewer must provide:

confirmed_issues

possible_issues

suggested_record_edits

suggested_qc_note_only_items

provisional_status

Primary QC Review Prompt
Role: Primary QC Reviewer for SDIndex / CKV records

Task:
Answer the following QC questions based only on the supplied fieldwork record.

Instructions:
- Be strict and evidence-based.
- Do not praise the writing.
- Do not expand into general interpretation.
- For each question, state:
  1. judgment
  2. evidence from the record
  3. risk level (low / medium / high)
  4. recommended action

Allowed judgments:
- no_issue
- minor_issue
- moderate_issue
- major_issue
- unresolved

At the end, provide:
- confirmed_issues
- possible_issues
- suggested_record_edits
- suggested_qc_note_only_items
- provisional_status
Step 4 — Challenge QC Review

The Challenge Reviewer does not repeat the full QC.

Instead, this role selects up to three conclusions in the Primary QC Review that may be:

too strong

too weak

insufficiently supported

Challenge QC Review Prompt
Role: Challenge QC Reviewer for SDIndex / CKV records

Task:
Review the Primary QC Review and challenge only the most questionable conclusions.

Instructions:
- Do not repeat the full QC.
- Select up to 3 conclusions from the Primary Review that may be too strong, too weak, or insufficiently supported.
- For each challenged point, explain:
  1. what you are challenging
  2. why the evidence may be insufficient or overextended
  3. your revised judgment

Focus on disagreement quality, not coverage.
Step 5 — QC Synthesis

The QC Synthesis Editor converts all prior outputs into one governance-ready note.

Output fields:

record_id

confirmed_issues

possible_issues

no_action_needed

edit_record_fields

create_qc_audit_note_for

final_qc_status

canonical_admission_recommendation

rationale

Allowed final_qc_status:

pass

pass_with_notes

hold_for_revision

hold_for_qc_note_only

QC Synthesis Prompt
Role: QC Synthesis Editor for SDIndex / CKV records

Task:
Synthesize the Intake Scan, QC Question Set, Primary QC Review, and Challenge QC Review into one final QC decision note.

Output format:
- record_id
- confirmed_issues
- possible_issues
- no_action_needed
- edit_record_fields
- create_qc_audit_note_for
- final_qc_status
- canonical_admission_recommendation
- rationale

Allowed final_qc_status:
- pass
- pass_with_notes
- hold_for_revision
- hold_for_qc_note_only
9. Final QC Status Logic
pass

Use when:

no meaningful structural or semantic instability is found

record is suitable for canonical admission

pass_with_notes

Use when:

record is broadly stable

minor issues exist

no immediate field edits are required

QC notes may still be useful

hold_for_revision

Use when:

specific fields should be corrected before canonical admission

issues materially affect downstream interpretation or classification

hold_for_qc_note_only

Use when:

the record may remain intact

but an explicit audit note must be attached

especially useful for interpretive ambiguity that should be documented rather than erased

10. Governance Principle

The purpose of QC is not to force all records into false certainty.

Some ambiguity should be documented rather than edited away.

Therefore:

use record edits when the issue is structural or clearly misaligned

use QC notes when the issue is interpretive, ambiguous, or epistemically valuable

11. Recommended Use by Project Stage
Early-stage repository

Recommended configuration:

one primary model for intake + question design + primary QC

one secondary model for challenge review

human final synthesis

Mid-stage repository

Recommended configuration:

one model per role

human oversight on canonical admission

High-value or Gold candidate records

Recommended configuration:

full workflow

explicit challenge review required

QC synthesis archived in data/qc_audit_notes/

12. Output Destination

Suggested repository destinations:

raw fieldwork record:

data/raw/

QC synthesis note:

data/qc_audit_notes/

record requiring revision:

remains in data/raw/ until revised

record approved for admission:

move or promote into data/canonical_records/

13. Final Rule

Do not ask one LLM to improvise all QC from scratch for every record.

Instead:

standardize the workflow

standardize the risk tags

standardize the QC modules

vary only the activated question set

This preserves methodological consistency while remaining record-sensitive.
