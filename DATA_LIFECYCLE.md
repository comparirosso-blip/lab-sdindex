# Data Lifecycle

This document defines the standard lifecycle of a field observation record from initial generation to long-term repository governance.

The goal is to ensure that every record moves through a consistent, reviewable, and auditable workflow.

## 1. Lifecycle Overview

Each field record follows the pipeline below:

`quickform_generation -> raw_storage -> human_review -> canonicalization -> analysis -> qc_review_if_needed -> canonical_revision_if_required -> research_log_escalation -> git_sync`

Not every record will require QC escalation, but every record should have a clear path from initial generation to canonical storage.

## 2. Stage Definitions

### Stage 1: QuickForm Generation

A record begins when the observation is entered through the QuickForm or equivalent structured intake tool.

Output status: `draft_generated`

Expected output:

- initial JSON draft
- basic metadata
- preliminary Vs scores
- initial notes and trigger selections

Storage location:

`data/raw/<RECORD_ID>/`

Recommended filename:

`<RECORD_ID>.quickform.v1.json`

This file is the first structured capture of the observation, not yet the official record.

### Stage 2: Raw Storage

The draft output is preserved in the raw layer.

Purpose:

- preserve provenance
- retain the original generated structure
- allow future backtracking if canonical values are revised

Rules:

- avoid overwriting raw files
- if a second reviewed draft is created, keep it as a separate named file
- raw is allowed to be messy; canonical is not

Optional reviewed raw filename:

`<RECORD_ID>.reviewed.v1.json`

### Stage 3: Human Review

The observer manually reviews the generated JSON.

Minimum review checklist:

- record ID correctness
- date and location accuracy
- observation mode accuracy
- Vs vector completeness
- subtype and trigger plausibility
- field notes adequacy
- emotion trajectory coherence
- research finding clarity

Output status: `reviewed_draft`

This stage is where human judgment stabilizes the output before canonicalization.

### Stage 4: Canonicalization

The reviewed record is promoted to the canonical layer.

Storage location:

`data/canonical_records/`

Filename rule:

`<RECORD_ID>.json`

Output status: `canonical_record_active`

Rules:

- only one canonical file per record ID
- canonical record is the structured source of truth
- do not create multiple parallel final files
- all downstream analysis should reference this file

### Stage 5: Analysis Attachment

Interpretive work begins only after the canonical record exists.

Storage location:

`data/analysis/<RECORD_ID>/`

Examples:

- model-assisted interpretations
- dimensional analyses
- narrative readings
- comparison notes
- human reflection notes tied to the sample

Recommended naming examples:

- `AN-<RECORD_ID>-gpt-YYYYMMDD-en.md`
- `AN-<RECORD_ID>-claude-YYYYMMDD-en.md`
- `AN-<RECORD_ID>-human-note-YYYYMMDD.md`

Output status: `analysis_attached`

Analysis is derivative, not authoritative.

### Stage 6: QC Review If Needed

A QC audit note is created only when the record presents a material issue.

Typical triggers for QC escalation:

- vector inconsistency
- trigger contradiction
- score-note mismatch
- manuscript conflict
- theoretical instability
- training suitability uncertainty
- benchmark-readiness concern

Storage location:

`data/qc_audit_notes/<RECORD_ID>/`

Recommended filename:

`QC-<RECORD_ID>-YYYYMMDD-EN-01.json`

Output status: `qc_under_review`

QC notes do not replace the canonical record. They evaluate it.

### Stage 7: Canonical Revision If Required

If QC identifies a true record-level problem, the canonical record may be revised.

Examples:

- incorrect trigger assignment
- unstable Ve interpretation
- misclassified subtype
- status downgrade from `Gold_Sample` to `Gold_Sample_Under_Review`

Output status: `canonical_record_revised`

Rules:

- revise deliberately
- preserve traceability through Git history
- document the reason in QC or changelog
- avoid silent correction with no review trail

### Stage 8: Research Log Escalation

If a single record reveals a broader methodological insight, that insight should be logged separately.

Storage location:

`research_log/`

Typical escalation themes:

- AI augmentation alters sensory interpretation
- guided tours suppress experienced rhythm
- trigger logic requires primary-secondary model
- annotation drift pattern discovered across records

Output status: `methodological_memory_updated`

This stage captures system learning, not just sample handling.

### Stage 9: Git Commit and Sync

All relevant files are committed to the repository with a meaningful commit message.

Recommended commit message pattern:

`[record:<RECORD_ID>] add canonical record / analysis / QC updates`

Output status: `repo_synced`

This stage preserves repository history and revision traceability.

## 3. Lifecycle Status Vocabulary

Suggested statuses:

- `draft_generated`
- `reviewed_draft`
- `canonical_record_active`
- `analysis_attached`
- `qc_under_review`
- `canonical_record_revised`
- `methodological_memory_updated`
- `repo_synced`

These statuses may be used in workflow documentation, dashboards, or future automation.

## 4. Governance Principles

The lifecycle is governed by the following principles:

### Preserve provenance

The original observation draft should remain available in the raw layer.

### Protect the canonical record

Only one canonical record should exist per sample ID.

### Separate interpretation from source

Analysis must never be mistaken for source data.

### Make QC formal

When instability is detected, document it as a structured audit note.

### Treat revision as traceable

Changes should be reviewable through Git and supporting documents.

### Escalate methodology when needed

A record-level issue may reveal a system-level insight. That insight belongs in research memory.

## 5. Minimum Per-Record Expectations

Minimum required:

- one canonical record in `data/canonical_records/`

Recommended:

- one raw intake JSON
- one or more analysis files
- one QC note if instability is present
- one research-log entry if the case changes the protocol

## 6. Summary

A field record is not complete when the QuickForm finishes. It becomes complete only when:

- provenance is preserved
- the canonical record is stabilized
- interpretation is separated
- QC is documented when necessary
- revisions are traceable
- methodological insights are retained

This lifecycle turns a personal field note into a governed research asset.
