# CKE Sensory Index (SDIndex) 

**Schema Version:** v1.4.1
**Author:** Sabrina
**License:** CC-BY-4.0

## Overview
The Cultural Knowledge Engine (CKE) and its core framework, the Sensory Density Index (SDIndex), constitute a phenomenological data collection system. This repository archives the baseline dataset, translating human embodied perception of architectural and natural spaces into a computable, machine-readable format (JSON). 

The primary dataset (`/data/kyoto_2026/`) focuses on establishing the phenomenological baseline of Asian spatial configurations, specifically analyzing the structural utilization of time, impermanence, and material decay in Kyoto, Japan.

## 1. Sensory Vectors ($V_s$)
A 5-dimensional continuous vector scoring system (0.0 - 10.0), evaluating physical and spatial phenomena independent of subjective preference.

| Vector | Dimension | Definition & Physical Anchors |
| :--- | :--- | :--- |
| **Vt** | Haptic & Cultural Materiality | 0 = Synthetic/Smooth ; 10 = Extreme natural weathering or dense traditional craftsmanship. |
| **Vl** | Optical & Illuminative Quality | 0 = Uniform, shadowless illumination ; 10 = Extreme shadow dominance or minimal candlelight. |
| **Vr** | Rhythmic & Social Restraint | 0 = Chaotic, unguided, high decibel ; 10 = Extreme physical or social constraint forcing slow/silent movement. |
| **Vg** | Geometric & Spatial Scale | 0 = Boundless horizontal extension (e.g., ocean) ; 10 = Extreme structural enclosure or geometric compression. |
| **Ve** | Temporal Phenomenon | 0 = Erased temporal cues (windowless/static) ; 10 = Drastic environmental dynamics or historical compression. |

## 2. Semantic Tags (Phenomenological Dictionary)
A controlled vocabulary of 18 keywords used to capture the phenomenological atmosphere. 
*Methodological Note (The Null Protocol): If no tag accurately describes the spatial experience, the array is intentionally left empty `[]` to indicate an Out-of-Distribution (OOD) sensory state.*

### Group 1: Spatial (空間視覺)
* `axis_pull`: Strong perspective, symmetry, or visual terminus forcing bodily movement.
* `sky_ratio_low`: Sky visibility < 20% at a 45-degree upward angle (deep eaves/dense canopy).
* `threshold_multiplied`: Requiring physical crossing of 3+ boundaries to reach the core.
* `diffused_clarity`: Absence of direct light; secondary+ diffused filtering yielding high visual resolution.
* `scale_dissonance`: Extreme macro (sublime) or micro (bonsai) scales causing failure of everyday distance judgment.
* `curated_wildness`: High human intervention deliberately mimicking unpolished natural states.

### Group 2: Temporal (時間物候)
* `anticipatory_decay`: Aesthetic value established on the ongoing process of material death/oxidation.
* `ephemeral_density`: Extremely brief natural phenomena (fog/falling petals) dominating sensory input.
* `off_season_clarity`: Underlying geometric structure revealed due to the absence of seasonal decoration (flowers/leaves).
* `golden_hour_compression`: Rapid light/shadow displacement within 1 hr of sunrise/sunset, accelerating perceived time.
* `crowd_rhythm_mismatch`: The space's designed slow rhythm is violently disrupted by fast-moving tourist crowds.
* `inhabitation_trace`: Irreversible micro-marks (wear/indentations) left by previous human physical activity.

### Group 3: Haptic (材質環境)
* `patina_gradient`: Gradient historical record on a single material formed by varying frequencies of human touch.
* `thermal_inertia`: Massive material thermal capacity resisting external climate, creating an independent microclimate.
* `canopy_filter`: Dense upper vegetation simultaneously filtering light, muffling sound, and trapping moisture.
* `moisture_presence`: Moisture transitioning to a tangible state, altering spatial scent (petrichor) and material reflectivity.
* `acoustic_void`: Anomalous blocking of background noise, isolating internal breath or micro-environmental sounds.
* `material_contrast_sharp`: Direct juxtaposition of extreme material opposites (e.g., modern glass embedded in weathered wood).

## 3. Relational Graph Nodes (Graph-RAG Preparation)
Used to construct topological relationships between isolated data points.

* `temporal_variant_of`: Re-measurement of the exact physical coordinates under different temporal/climatic conditions.
* `counterpoint_of`: Two spaces exhibiting completely opposing vectors and tags, forming a structural dialectic.
* `sensory_mirror_of`: Spaces with different physical/cultural coordinates triggering highly overlapping phenomenological scores.

## 4. JSON Structure Example
Each observation is exported as a single JSON file.

```json
{
  "record_id": "KYT-20260319-A",
  "schema_version": "1.4.1",
  "vs_vector": { "Vt": 8.0, "Vl": 9.0, "Vr": 7.5, "Vg": 6.0, "Ve": 8.5 },
  "ve_valence": 1,
  "sdindex_computation": { "sdindex_score": 7.8 },
  "free_keywords": [
    "diffused_clarity",
    "anticipatory_decay",
    "acoustic_void"
  ],
  "emotion_trajectory": {
    "trajectory_type": "expectation_collapse_reframe"
  },
  "asset_class": "Gold_Sample",
  "usable_for_llm_training": true
}
