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
