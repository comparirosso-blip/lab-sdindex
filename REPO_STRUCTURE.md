# Repository Structure

This document defines the structural logic, folder roles, and governance rules of this repository. It is intended to preserve dataset integrity, reduce version drift, and make the repository understandable to future collaborators, reviewers, and downstream AI systems.

## 1. Purpose

This repository is not a generic note archive. It is a research-grade dataset repository for structured sensory observation, annotation, analysis, and quality control.

The structure is designed to support:

- raw data preservation
- canonical record stability
- analysis traceability
- QC accountability
- schema consistency
- future reproducibility

The repository therefore separates source materials, official records, interpretive outputs, and audit documents into distinct layers.

## 2. Core Design Logic

The repository follows a layered data-governance model.

Each observation record may pass through the following stages:

`raw -> canonical_record -> analysis -> qc_audit_note`

These stages are not interchangeable.

- `raw` stores source materials and early-stage inputs.
- `canonical_record` stores the official structured JSON record for a sample.
- `analysis` stores interpretive outputs, model-assisted readings, and analytical notes.
- `qc_audit_note` stores review documents that evaluate record quality, annotation stability, cross-version conflicts, and training readiness.

This separation exists to prevent conceptual drift. A narrative analysis must not silently overwrite a record. A QC finding must not be confused with the record itself. A manuscript interpretation must not replace the canonical JSON.

## 3. Recommended Top-Level Structure

```text
repo_root/
├── README.md
├── REPO_STRUCTURE.md
├── DATA_LIFECYCLE.md
├── data/
│   ├── raw/
│   ├── canonical_records/
│   ├── analysis/
│   └── qc_audit_notes/
├── schema/
├── docs/
├── tools/
└── research_log/
```

## 4. Folder Definitions

### `data/raw/`

Purpose: immutable or near-immutable source materials.

This folder stores original observation inputs and supporting materials before they are normalized into official records.

Examples may include:

- field notes
- draft observation JSON
- transcription fragments
- raw annotation drafts
- supporting contextual files tied to a record ID

Rules:

- do not overwrite without clear justification
- do not treat files here as official benchmark-ready records
- if a raw record is reconstructed after the fact, mark it clearly as retrospective

This layer preserves provenance.

### `data/canonical_records/`

Purpose: official structured sample records.

This folder stores the single authoritative JSON record for each finalized observation sample.

Examples:

- `KYT-20260118-A.json`
- `KYT-20260226-A.json`

Rules:

- one canonical file per record ID
- this is the source of truth for structured sample-level values
- if a value changes, update through documented revision process
- manuscript text, charts, appendices, and downstream analysis should reference this layer, not ad hoc copies

This layer preserves record stability.

### `data/analysis/`

Purpose: interpretive and analytical outputs.

This folder stores analysis derived from a sample, including human notes, model-generated readings, methodological reflections, or comparative analyses.

Examples:

- model-assisted interpretation
- dimensional reading of Vs vectors
- narrative analysis of a site
- cross-sample comparison notes

Rules:

- analysis is not the record
- analysis may challenge or reinterpret the record, but must not silently replace it
- analysis files should be clearly named by record ID, author or model, and date

Recommended naming pattern:

```text
AN-KYT-20260118-A-gpt-20260309.md
AN-KYT-20260118-A-claude-20260308.md
AN-KYT-20260118-A-human-note-20260309.md
```

This layer preserves interpretive traceability.

### `data/qc_audit_notes/`

Purpose: structured review and quality control.

This folder stores audit notes that evaluate whether a record is internally consistent, theoretically coherent, benchmark-ready, or safe for LLM training.

Examples:

- trigger conflicts
- vector inconsistency checks
- manuscript-vs-record comparison
- annotation instability review
- training suitability review

Rules:

- QC notes do not replace the canonical record
- QC notes may downgrade confidence, flag conflicts, or recommend schema changes
- all critical review logic should be documented here rather than embedded informally in chat logs or manuscript prose

Recommended naming pattern:

```text
QC-KYT-20260118-A-20260309-EN-01.json
QC-KYT-20260118-A-20260310-EN-02.json
```

This layer preserves audit accountability.

## 5. Additional Repository Areas

### `schema/`

Purpose: formal schema definitions and structural constraints.

This folder stores JSON schemas, enums, and any structure-defining documents that govern record validity.

Examples:

- `CKV_schema_v1.3.json`
- `qc_audit_note.schema.json`
- `field_record_workflow.schema.json`

Rules:

- schema files define structure, not sample content
- schema versions should be explicit
- changes here should be tracked carefully because they affect all records

### `docs/`

Purpose: methodological and protocol documentation.

This folder stores human-readable documentation about how the dataset is built, scored, validated, and maintained.

Examples:

- scoring guide
- validation protocol
- pilot plan
- changelog
- methodological notes

Typical files:

- `SCORING_GUIDE.md`
- `VALIDATION_PROTOCOL.md`
- `TAIPEI_PILOT_PLAN.md`
- `CHANGELOG.md`

Rules:

- documents here explain how the system works
- they should not function as hidden data storage
- if a methodological change affects annotation logic, corresponding schema and QC implications should be reviewed

### `tools/`

Purpose: operational utilities and helper artifacts.

This folder stores tools used to generate, collect, or validate data.

Examples:

- quick entry forms
- helper scripts
- local interfaces
- templates used during collection

Typical files:

- `CKV_QuickForm_v1_3.html`

Rules:

- tools support the protocol but are not themselves the protocol
- avoid storing core methodology only inside tool files; the method should also be documented in `docs/`

### `research_log/`

Purpose: reflective and procedural log material.

This folder stores ongoing notes about research decisions, methodological reflections, unresolved questions, and development history.

Examples:

- reasoning logs
- pilot reflections
- schema design decisions
- conceptual notes

Rules:

- research logs may inform future analysis or protocol revisions
- they are not canonical records
- they should be treated as contextual memory, not benchmark data

## 6. Naming Logic

The repository should follow stable naming discipline.

### Record IDs

Each observation sample should keep a stable record ID such as:

- `KYT-20260118-A`
- `TPE-20260308-A`

This record ID should remain consistent across:

- canonical record
- analysis folder
- QC folder
- supporting documentation tied to the same sample

### File Prefixes

Recommended prefixes:

- `AN-` for analysis files
- `QC-` for QC audit files

Examples:

- `AN-KYT-20260118-A-gpt-20260309.md`
- `QC-KYT-20260118-A-20260309-EN-01.json`

This prevents confusion between record files and derivative documents.

## 7. Canonical Source Rule

For each sample, the canonical structured source must be the file in:

`data/canonical_records/`

If another document disagrees with that record, the disagreement must be documented through:

- a QC audit note
- a revision note
- or an explicit schema update process

Manuscripts, appendices, chat-derived outputs, and analytical summaries do not automatically override the canonical record.

This rule exists to prevent silent drift.

## 8. Revision Logic

When a record changes, the change should be governed rather than improvised.

Examples of legitimate revision triggers:

- annotation error discovered during QC
- schema migration
- trigger classification refinement
- conflict found between manuscript and record
- post-hoc downgrade of confidence or benchmark status

Recommended practice:

- preserve raw input
- revise canonical record deliberately
- log the reason in QC note or changelog
- avoid maintaining multiple “final” versions in parallel

A repository becomes unreliable when more than one file informally claims to be the truth.

## 9. What This Structure Prevents

This structure is specifically designed to prevent the following failure modes:

- raw material being overwritten by cleaned records
- analysis files being mistaken for source data
- QC concerns being lost in chat history
- manuscript claims drifting away from the actual dataset
- duplicate files with unclear authority
- sample records being used for LLM training without audit status

## 10. Practical Governance Notes

To maintain structural integrity:

- keep only one `README.md` at the authoritative location
- remove ambiguous duplicates such as `README (1).md`
- avoid vague folder names such as `samples/` if the actual role is `canonical_records`
- treat QC as a formal layer, not an informal afterthought
- prefer explicit status labels such as `Gold_Sample_Under_Review` when confidence is contested

## 11. Summary

This repository is built as a governed research system, not a casual archive.

Its structure separates:

- source material
- official record
- interpretation
- audit review
- schema logic
- protocol documentation
- research memory

That separation is essential because the project aims to support not only human reading, but also future validation, reproducibility, and machine-readable trust.

When in doubt, preserve provenance, protect the canonical record, and document disagreement instead of hiding it.
