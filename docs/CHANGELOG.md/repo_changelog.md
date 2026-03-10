# CHANGELOG

All notable changes to this repository will be documented in this file.

This changelog is used to track structural, methodological, and schema-related changes in **Lab_SDIndex**.

The format is adapted for a research repository rather than a software release product.  
It records major updates to:

- repository structure
- data lifecycle design
- schema logic
- protocol documentation
- QC / audit practices
- Graph RAG preparation logic

---

## [Unreleased]

### Planned
- Add initial schema files under `schema/`
- Add protocol explanation documents under `docs/`
- Add first canonical SDIndex records
- Add QC / audit note examples
- Add research log index and naming conventions
- Add future Graph RAG alignment notes

---

## [0.1.0] - 2026-03-10

### Added
- Established the initial repository as **Lab_SDIndex**
- Defined root-level documentation files:
  - `README.md`
  - `REPO_STRUCTURE.md`
  - `DATA_LIFECYCLE.md`
- Created the first stable `data/` layer structure:
  - `data/raw/`
  - `data/canonical_records/`
  - `data/analysis/`
  - `data/qc_audit_notes/`
- Created supporting directories:
  - `schema/`
  - `docs/`
  - `tools/`
  - `research_log/`

### Defined
- Confirmed the repository as a **research-oriented SDIndex lab**, not a casual archive or generic JSON dump
- Confirmed the core repository logic:
  - human observation first
  - structured consistency second
  - graph connection later
- Defined the separation of data states across the repository lifecycle:
  - raw observation
  - canonical record
  - analysis output
  - QC / audit note

### Clarified
- Confirmed that `canonical_records/` refers to records recognized as the current protocol-consistent version, not merely “finished files”
- Confirmed that `analysis/` stores interpretation, comparison, and derivative reasoning rather than source observations
- Confirmed that `qc_audit_notes/` stores ambiguity flags, review logic, revision notes, and trust-trace materials
- Confirmed that not all raw records should automatically become canonical records

### Methodology
- Established the principle that source observation, interpretation, and audit logic must remain separated
- Established the principle that Graph RAG alignment is a later-stage integration goal, not the starting point of the repository
- Established the importance of preserving methodological integrity over premature scale

### Notes
- GitHub file display order was recognized as a UI sorting issue, not a repository design issue
- Repository naming discussion considered both stylistic and engineering-stable forms:
  - display identity: `Lab_SDIndex`
  - stable repo slug candidate: `lab-sdindex`

---

## Repository Changelog Policy

This file should record only meaningful changes, such as:

- structural changes to the repository
- folder renaming or lifecycle redesign
- schema revisions affecting record logic
- protocol changes affecting how records are created or interpreted
- QC standards or audit logic revisions
- changes in Graph RAG readiness assumptions

This file should **not** be used for:
- minor typo fixes
- casual note additions
- one-off drafting edits
- temporary experimentation with no lasting impact

---

## Versioning Logic

This repository uses lightweight semantic versioning adapted for research infrastructure:

- **MAJOR**: major restructuring of the SDIndex framework, lifecycle, or schema philosophy
- **MINOR**: meaningful additions such as new documentation layers, stable schema introduction, or important repository expansion
- **PATCH**: smaller but still notable corrections to repository logic, documentation, or folder policy

Example:

- `0.1.0` = first stable repository structure
- `0.2.0` = first stable schema package added
- `0.3.0` = first canonical dataset batch added
- `1.0.0` = repository reaches stable methodological baseline

---

## Maintainer

Sabrina Lin
