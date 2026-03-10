# SDIndex Validation Protocol

**Version:** 1.0  
**Applies to:** CKV Schema v1.2 · N=150 Gold Samples  
**Author:** Sabrina  

---

## Overview

Validation runs in three layers, executed in sequence. Layers 1 and 2 can begin before all 150 records are complete. Layer 3 requires the full dataset.

| Layer | Name | Who | When |
|-------|------|-----|------|
| 1 | Internal Consistency | Sabrina (solo) | After final record; also spot-check at N=50, N=100 |
| 2 | Cluster Validation | Daniel | At N=50, N=100, N=150 |
| 3 | Graph RAG Retrieval Test | Sabrina + Daniel | After N=150 only |

---

## Layer 1 — Internal Consistency

**Goal:** Confirm that scoring standards have not drifted between the first and last records.

### 1.1 Anchor Re-scoring

Before beginning fieldwork, designate at least **4 anchor sites**:

| Anchor Type | Example | Expected SDIndex range |
|-------------|---------|----------------------|
| Low-end (modern, sterile) | Convenience store, hotel corridor | 1.0 – 2.5 |
| Low-mid (functional public) | Kyoto Station concourse | 2.5 – 4.0 |
| High-mid (quality traditional) | Philosopher's Path (off-peak) | 6.0 – 7.5 |
| High-end (peak sensory density) | Ryoanji early morning, Katsura Rikyu | 8.0 – 9.5 |

**Procedure:**
1. Record anchor sites as early as possible (ideally within the first 10 records).
2. After completing all 150 records, revisit and re-score each anchor site independently — do not look at the original scores first.
3. Compare original vs. re-score.

**Pass criteria:** Difference ≤ 0.5 per dimension (Vt, Vl, Vr, Vg, Ve).  
**If drift > 0.5:** Identify when the drift began (review records chronologically) and apply a correction note to affected records. Do not silently overwrite — add a `calibration_note` field to the relevant JSON records.

### 1.2 Dimension Stability Check

For each of the five dimensions, calculate:
- Mean score across all 150 records
- Standard deviation

**Flag for review if:**
- Any dimension mean is above 8.5 or below 2.0 (possible ceiling/floor effect — scoring range may be too compressed)
- Vg standard deviation is below 1.0 (Vg is the most abstract dimension and should show natural spread)

### 1.3 Resilience Calibration Check

Cross-tabulate `sensory_resilience` level against `sdindex_score` ranges:

Expected pattern:
- `exceptional` resilience sites should maintain SDIndex ≥ 6.0 even when `crowd_density` = high
- `low` resilience sites should show SDIndex drop > 2.0 between empty and crowded conditions (if you have paired records)

If this pattern does not hold, the resilience scale needs recalibration before Layer 3.

---

## Layer 2 — Cluster Validation

**Goal:** Confirm that the Vs vector produces meaningful groupings that match expert intuition. Run at N=50, N=100, N=150.

**Handled by:** Daniel  
**Input:** `data/samples/*.json` → extract `vs_vector` fields  
**Method:** k-means clustering (k=5 to start; test k=4 and k=6)

### 2.1 Expected Cluster Profiles

These are hypothesis clusters. The test is whether the algorithm recovers something close to these groupings without being told:

| Cluster | Expected members | Dominant dimensions |
|---------|-----------------|-------------------|
| A — Wabi-sabi enclosure | Zen gardens, moss temples, dark machiya interiors | High Vr, High Vg (enclosure_deep), High Ve |
| B — Imperial geometry | Katsura Rikyu, Nijo Castle grand rooms | High Vg (geometric_strict), High Vl (natural_diffused) |
| C — Living tradition | Nishiki Market, Fushimi Inari torii paths | High Vt, High Vl (mixed), Low Vr |
| D — Modern neutral | Stations, hotels, commercial corridors | Low across all dimensions |
| E — Transitional / hybrid | Philosopher's Path, urban shrines | Mid-range, high Ve |

### 2.2 Cross-domain Resonance Test

After clustering, check: do any **non-spatial** records (wineries, tastings, material samples if included) fall inside spatial clusters?

This is the most important test. If a wine tasting record clusters with Cluster A (wabi-sabi enclosure) based purely on Vs vector similarity, the cross-modal retrieval hypothesis is validated.

### 2.3 Stability Across N

Compare cluster membership between N=50, N=100, N=150 runs. If clusters shift dramatically between runs, the dataset has sampling bias (too many records of one type). Address by diversifying remaining records before completing N=150.

---

## Layer 3 — Graph RAG Retrieval Test

**Goal:** Confirm that SDIndex-weighted Graph RAG produces meaningfully better results than unweighted retrieval. Requires full N=150 dataset.

Run three query types. For each, compare:
- **Control:** Standard Graph RAG, no SDIndex weighting
- **Test:** SDIndex re-ranked results (SDIndex score as node weight)

### Query Type 1 — Semantic Trap

These queries have obvious keyword matches that should be *overridden* by sensory data.

Example queries:
- "京都靜謐的寺院" (quiet Kyoto temple)
- "適合沉思的空間" (space for contemplation)

**Pass criteria:** Test results exclude high-crowd-density records of well-known temples during peak season. Control results include them. The divergence between control and test outputs should be explainable by `crowd_density` + `sensory_resilience` data.

### Query Type 2 — Cross-modal / Synesthetic Query

Queries that have no direct keyword match in the dataset — only Vs vector similarity can answer them.

Example queries:
- "像老威士忌木質尾韻的空間" (a space with the quality of aged whisky's woody finish)
- "低頻的、有重量感的靜默" (low-frequency, weighted silence)
- "觸感粗糙但視覺簡潔的場所" (tactile roughness with visual simplicity)

**Pass criteria:** System returns at least 3 records with explainable Vs vector matches (e.g., high Vt + high Vg enclosure + low Vl for the whisky query). Control returns nothing meaningful or returns by keyword coincidence only.

### Query Type 3 — Temporal / Resilience Split

Same site, different temporal parameters.

Example: Query "龍安寺" with:
- Context A: `season=early_spring, crowd_density=very_low`
- Context B: `season=autumn, crowd_density=crowded`

**Pass criteria:** SDIndex-weighted system returns meaningfully different recommendations or confidence scores for the same site under the two contexts. Control returns the same result regardless of temporal context.

---

## Recording Validation Results

After completing each layer, create a record in `data/validation/`:

```
data/
└── validation/
    ├── L1_consistency_report.md      ← narrative + anchor re-score table
    ├── L2_cluster_N50.json           ← cluster assignments at N=50
    ├── L2_cluster_N100.json
    ├── L2_cluster_N150.json
    ├── L2_analysis.md                ← cross-domain resonance findings
    └── L3_retrieval_test.md          ← query results, control vs. test comparison
```

---

## Pass / Fail Summary

| Check | Pass condition | Action if fail |
|-------|---------------|----------------|
| L1 anchor drift | ≤ 0.5 per dimension | Add calibration_note to affected records, re-anchor |
| L1 dimension range | No ceiling/floor effect | Recalibrate scoring scale for that dimension |
| L2 cluster recovery | ≥ 3 of 5 expected clusters emerge | Review sampling diversity; add missing site types |
| L2 cross-domain hit | At least 1 non-spatial record in spatial cluster | Partial pass; document and continue to L3 |
| L3 semantic trap | Test ≠ Control for at least 2 of 3 queries | Review node weight formula; adjust SDIndex scaling |
| L3 cross-modal | ≥ 3 explainable Vs matches returned | Review edge definition; check Vs distance formula |
| L3 temporal split | Different outputs for same site under different context | Check C-factor / resilience integration in pipeline |

---

## Notes

- Validation is not pass/fail for the entire framework. Each layer produces findings that inform the next schema version (v1.3).
- A "fail" in any single check is a data point, not a rejection. Document everything.
- The goal of N=150 is statistical significance for the Vs vector distribution, not perfection of every record.
