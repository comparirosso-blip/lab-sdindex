# Schema Consistency Review
## SDIndex / CKV Dataset — v1.3

**Records reviewed:** KYT-20260226-A, KYT-20260118-A, TPE-20260308-A
**Schema version:** 1.3 (all three records)
**Reference documents:** CHANGELOG.md, schema_thinking conceptual note
**Review date:** 2026-03-10

---

## 1. Arithmetic Consistency

All three records pass arithmetic verification.

| Record | Sum | Stated | SDIndex | Stated | Status |
|--------|-----|--------|---------|--------|--------|
| KYT-20260226-A | 31.5 | 31.5 | 6.3 | 6.3 | OK |
| KYT-20260118-A | 38.0 | 38.0 | 7.6 | 7.6 | OK |
| TPE-20260308-A | 13.5 | 13.5 | 2.7 | 2.7 | OK |

No issues.

---

## 2. Field Completeness

### 2a. Structural field present in one record, absent in others

| Field | KYT-0226 | KYT-0118 | TPE-0308 | Issue |
|-------|----------|----------|----------|-------|
| `sdindex_computation.calibration_note` | MISSING KEY | MISSING KEY | null | **Schema drift** |

`calibration_note` exists only in TPE-20260308-A. The two Kyoto records don't have the key at all. This is a v1.3 field that was apparently added with the Taipei pilot but not backfilled.

**Recommendation:** Add `calibration_note: null` to both Kyoto records for structural uniformity. Decide whether this field is part of v1.3 spec — if yes, it must appear in every record even if null.

### 2b. Nullable fields — legitimate variation

| Field | KYT-0226 | KYT-0118 | TPE-0308 | Status |
|-------|----------|----------|----------|--------|
| `site.name_local` | 二年坂 | かつらりきゅう | null | Acceptable — Taipei sites may not have a distinct local name |
| `emotion_trajectory.turning_point` | present | present | null | Acceptable — `flat_positive` trajectory type logically has no turning point |
| `counterpoint.paired_record` | null | null | null | No pairs yet — expected at this sample size |

No action needed on these, but the schema spec should explicitly state that `turning_point` is nullable when `trajectory_type` does not involve a state change.

---

## 3. Value Vocabulary Audit

### 3a. Fields with defined allowed values (per changelog)

**`Vl_source`** — Changelog v1.2 lists: `natural_diffused / natural_direct / artificial_warm / artificial_neutral / mixed / candlelight_lantern`

| Record | Value | In spec? |
|--------|-------|----------|
| KYT-20260226-A | natural_diffused | Yes |
| KYT-20260118-A | natural_diffused | Yes |
| TPE-20260308-A | artificial_neutral | Yes |

Clean.

**`Vg_subtype`** — Changelog v1.2 lists: `enclosure_deep / enclosure_shallow / open_framed / open_unframed / layered_threshold / void_centred / geometric_strict / geometric_organic`

| Record | Value | In spec? |
|--------|-------|----------|
| KYT-20260226-A | open_unframed | Yes |
| KYT-20260118-A | open_framed | Yes |
| TPE-20260308-A | geometric_organic | Yes |

All values are in-spec. However, QC reviews flagged that KYT-20260226-A's `open_unframed` contradicts its field note (which describes anchoring and framing), and TPE-20260308-A's `geometric_organic` has weak support (curves are architectural, not organic). The vocabulary is consistent; the application is not always accurate. **This is a QC calibration issue, not a schema issue.**

**`sensory_resilience.level`** — Changelog v1.2 lists: `low / medium / high / exceptional`

| Record | Value | In spec? |
|--------|-------|----------|
| KYT-20260226-A | medium | Yes |
| KYT-20260118-A | exceptional | Yes |
| TPE-20260308-A | low | Yes |

Clean. Good spread across three levels.

### 3b. Fields WITHOUT defined allowed values in the changelog

These fields are in use across all three records but have no enumerated vocabulary in any schema document:

| Field | Values observed | Risk |
|-------|----------------|------|
| `site_type` | urban_public_space, zen_temple_garden, commercial_district | **HIGH** — no controlled vocabulary. KYT-0118's `zen_temple_garden` is factually wrong for Katsura (imperial villa). Without a defined list, misclassification is undetectable at the schema level. |
| `Vt_subtype` | architectural_heritage, corporate_constructed | **MEDIUM** — only 2 values so far, but no enumerated list. What other types exist? Religious? Natural landscape? Living cultural practice? |
| `Vr_source` | invited_openness, architectural_design, cognitive_compression | **HIGH** — 3 records, 3 different values, no defined vocabulary. `invited_openness` and `cognitive_compression` are not in any changelog. These appear to be observer-generated ad hoc labels. |
| `Ve_trigger` | external_narrative_human, self_time_projection | **MEDIUM** — 2 values observed but no spec. KYT-0118 QC showed that `self_time_projection` was inaccurate (AI was involved). Without a defined list, trigger labels drift toward whatever fits the observer's narrative in the moment. |
| `visit_mode` | couple_free, guided_tour | Low risk at current N, but needs definition before the vocabulary expands. |
| `crowd_density` | high, very_low | Low risk — appears to use a simple ordinal scale. Needs enumeration (e.g., very_low / low / medium / high / very_high). |
| `trajectory_type` | ascending_resonance, expectation_collapse_reframe, flat_positive | **MEDIUM** — 3 records, 3 different types. Creative and descriptive, but no controlled list. Will fragment quickly at higher N. |

**Core finding:** The changelog defines allowed values for Vl_source, Vg_subtype, and sensory_resilience — the fields added in v1.2. But the fields added in v1.1 (Vt_subtype, Vr_source, Ve_trigger, trajectory_type) and the fields present since v1.0 (site_type, visit_mode, crowd_density) have **no defined vocabulary**. This is the schema's primary consistency gap.

---

## 4. Scoring Scale Behavior

### 4a. Cross-record score comparison

| Dimension | KYT-0226 (Ninenzaka) | KYT-0118 (Katsura) | TPE-0308 (LaLaport) |
|-----------|----------------------|---------------------|----------------------|
| Vt | 8 | 9 | 2.5 |
| Vl | 6 | 8.5 | 2.0 |
| Vr | 7 | 6 | 2.5 |
| Vg | 8 | 9 | 4.0 |
| Ve | 2.5 | 5.5 | 2.5 |

The spread is wide (2.0 to 9.0), which is healthy for a dataset that includes both heritage sites and commercial anchors. The LaLaport record functions as an effective low-end reference.

### 4b. Scale stability concern: Vg=9 at Katsura

Katsura's Vg=9 is the highest geometry score in the dataset, but its field note — 「無庸置疑，這個項目是絕對的高分」— contains zero geometric description. Compare with Ninenzaka's Vg=8, which describes a specific mechanism (stairway elevation shifts creating pagoda angle variation). The scoring scale is consistent (9 > 8 is plausible for Katsura vs. Ninenzaka), but the **justification standard is inconsistent**. At the high end of the scale, field notes must provide proportionally stronger evidence. A score of 9 with no description is a calibration risk — it teaches future scoring that assertion alone is sufficient.

**Recommendation:** Establish a minimum documentation threshold for scores ≥ 8: at least two specific observable features must be named in the field note.

### 4c. Scale stability concern: Ve across records

| Record | Ve | Ve_trigger | What the note actually describes |
|--------|-----|------------|----------------------------------|
| KYT-0226 | 2.5 | external_narrative_human | Ambient tolerance, no strong emotion, mild temporal-overlay from kimono |
| KYT-0118 | 5.5 | self_time_projection | Complex trajectory: aesthetic distance → AI-mediated empathic identification |
| TPE-0308 | 2.5 | self_time_projection | Escape fantasy, no engagement, desire to be elsewhere |

KYT-0226 and TPE-0308 both score Ve=2.5, but for different reasons: one is "neutral tolerance in a pleasant crowd," the other is "active disengagement from a hostile sensory environment." The same number encodes qualitatively different states. This is not necessarily a problem — Ve may legitimately measure intensity regardless of valence — but the schema should declare whether Ve is **intensity-only** or **valence-sensitive**. Currently it is ambiguous, and at higher N this ambiguity will produce false equivalences in clustering.

---

## 5. Subtype Label Consistency

### 5a. Labels that match field notes across records

| Subtype field | Consistent? | Notes |
|---------------|------------|-------|
| Vt_subtype | **Yes** | `architectural_heritage` used twice for heritage sites, `corporate_constructed` for commercial — clean distinction. |
| Vl_source | **Yes** | `natural_diffused` for outdoor overcast/sunny, `artificial_neutral` for indoor commercial — accurate. |
| Vg_subtype | **No** | KYT-0226: `open_unframed` contradicts "anchor" language in note. TPE-0308: `geometric_organic` has no organic evidence. KYT-0118: `open_framed` is plausible but undocumented. 1 of 3 clean. |
| Vr_source | **No** | All three labels appear to be ad hoc. No two records use the same value. No changelog definition exists. |
| Ve_trigger | **Partially** | `self_time_projection` used twice but means different things (escape fantasy vs. empathic historical projection + AI). `external_narrative_human` has no human narrative source documented. |

### 5b. Root cause

The v1.2 changelog defined Vl_source and Vg_subtype vocabularies. No equivalent definition exists for Vr_source, Ve_trigger, or trajectory_type. These three fields are currently **open-text fields masquerading as categorical labels**. The observer generates a new value for each record, producing a vocabulary that grows linearly with N.

---

## 6. Structural / Naming Issues

### 6a. `site.name_en` trailing comma

KYT-20260226-A has `"name_en": "Ninenzaka,"` — trailing comma in the string value. Minor but will cause issues in string matching and display.

### 6b. `companion` field inconsistency

| Record | Value |
|--------|-------|
| KYT-0226 | husband |
| KYT-0118 | Solo |
| TPE-0308 | 老公 |

Three formats: English common noun, English proper-case label, Chinese. `husband` and `老公` mean the same thing. `Solo` is capitalized inconsistently (should it be `solo`?). This field needs either a controlled vocabulary (solo / companion / group) or a language convention.

### 6c. `observation.weather` mixed language

| Record | Value |
|--------|-------|
| KYT-0226 | 陰 |
| KYT-0118 | 晴 |
| TPE-0308 | 雨 |

All Chinese, which is internally consistent. But if non-Chinese-reading collaborators or LLM pipelines need to parse this, consider adding an English-key equivalent or switching to a controlled vocabulary (overcast / clear / rain / snow / etc.).

---

## 7. Schema Gaps Identified

These are fields or conventions that don't yet exist but whose absence has caused issues across the three reviewed records:

| Gap | Evidence | Impact |
|-----|----------|--------|
| No `research_question` field separate from `research_finding` | KYT-0226 has a question in the finding field | Conflates hypothesis with output |
| No `observation_layer` vs `inference_layer` marker within emotion_trajectory | KYT-0118 mixes pre-AI and post-AI interpretation in turning_point | Epistemic provenance unclear |
| No `ai_source` or `ai_interaction_log` field | KYT-0118 references Google AI but records only a boolean flag | AI influence is documented in narrative but not structured |
| No `Ve_valence` field | Two records score Ve=2.5 for qualitatively opposite states | Intensity and direction are conflated |
| No minimum documentation standard for high scores | KYT-0118 Vg=9 has no description | Assertion-only scoring at high end |

---

## 8. Summary of Findings

### What is working well

- **Arithmetic is clean.** All sums and SDIndex scores verify.
- **Schema version is consistent.** All records are v1.3.
- **v1.2-defined vocabularies (Vl_source, Vg_subtype, sensory_resilience) are being used correctly.**
- **Score range shows healthy spread.** Low anchor (TPE, SDIndex=2.7) to high (KYT-0118, SDIndex=7.6).
- **TPE-0308's research_finding is a model** for how that field should be used.

### What needs attention

| Priority | Issue | Fix type |
|----------|-------|----------|
| **P1** | Vr_source, Ve_trigger, trajectory_type, site_type have no controlled vocabulary | Schema definition needed |
| **P1** | Vt_subtype has only 2 observed values and no enumerated list | Schema definition needed |
| **P2** | Vg_subtype labels are in-spec but frequently misapplied | Observer calibration / QC protocol |
| **P2** | Ve has no valence indicator — same score encodes opposite states | Schema addition (Ve_valence field) |
| **P2** | High scores (≥8) have no minimum documentation standard | QC protocol addition |
| **P3** | `companion` field uses mixed language and format | Controlled vocabulary or convention |
| **P3** | `calibration_note` field missing from Kyoto records | Backfill or remove from spec |
| **P3** | `name_en` has trailing comma in KYT-0226 | Data fix |
| **P3** | `weather` field is Chinese-only | Convention decision needed for multilingual dataset |

### Recommended next step

The highest-leverage action is to **define controlled vocabularies for the five undefined categorical fields**: `site_type`, `Vt_subtype`, `Vr_source`, `Ve_trigger`, and `trajectory_type`. This can be done inductively — start from the values already observed, project what's needed for the next 10–20 records, and publish a v1.4 changelog entry with the enumerated lists. Without this, vocabulary will fragment and cross-record comparison will degrade as N grows.

I can draft these vocabularies if you want to move to that step next.
