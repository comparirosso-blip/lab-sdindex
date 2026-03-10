# Schema Consistency Review Disposition Note
## Date: 2026-03-10
## Scope: 3 raw fieldwork records reviewed under CKV / SDIndex v1.3

This note records the immediate disposition following the first cross-record schema consistency review.

It is **not** a schema revision decision.  
It is a temporary governance note to preserve current judgment until a larger sample size is available.

---

## 1. Current Position

At 3 records, the dataset is large enough to reveal meaningful consistency issues, but still too small to justify a full schema revision.

Therefore:

- no immediate upgrade to v1.4
- no large-scale retroactive rewriting of raw records
- only small corrective actions and provisional watchlist creation

---

## 2. Immediate Actions

The following items may be addressed now:

- fix the trailing comma in `KYT-20260226-A.site.name_en`
- decide whether `calibration_note` is a formal v1.3 field
  - if yes, backfill missing records with `null`
  - if no, remove it from future record expectations

---

## 3. Issues Deferred for Later Schema Review

The following fields are now identified as **priority vocabulary / schema candidates**, but revision is deferred until more records are accumulated:

- `site_type`
- `Vt_subtype`
- `Vr_source`
- `Ve_trigger`
- `trajectory_type`
- `visit_mode`
- `crowd_density`

These fields appear important for cross-record comparison and should be revisited after a larger raw dataset exists.

---

## 4. Issues to Absorb into QC Rather Than Schema

The following issues are currently treated as **QC / calibration issues**, not schema defects:

- weak evidence support for very high scores
- mismatch between assigned subtype and actual field-note evidence
- field-note overlap between dimensions, especially `Vr`, `Vg`, and `Ve`
- `research_finding` phrased as an open question rather than a finding

These should be handled through review discipline and prompt design before they are handled through schema expansion.

---

## 5. Ideas Not Adopted Yet

The following proposals are considered valuable, but are deferred for now:

- adding `Ve_valence`
- splitting `research_question` from `research_finding`
- splitting `observation_layer` from `inference_layer`
- adding `ai_source` or `ai_interaction_log`

These remain future design candidates, not current implementation tasks.

---

## 6. QC Rules Worth Absorbing Now

The following provisional QC rules are useful immediately:

- scores of 8 or above should require stronger descriptive evidence
- `research_finding` should be written as a finding whenever possible, not as an unresolved question

These may be added to QC workflow documentation without triggering a schema revision.

---

## 7. Revisit Threshold

A more formal schema revision discussion should be reopened after:

- 5 to 10 total raw records are accumulated
- at least several records across more than one site type are available
- recurring issues can be confirmed as pattern-level rather than record-level

Until then, this review functions as a watchlist rather than a change order.

---

## 8. Summary

Current disposition:

- make only minimal corrections now
- preserve raw records as historical field evidence
- treat major structure changes as deferred
- use QC workflow to absorb instability where possible
- revisit schema expansion after more records accumulate
