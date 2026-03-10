# SDIndex Scoring Guide

**Version:** 1.0  
**Applies to:** CKV Schema v1.2  
**Author:** Sabrina  

---

## The Five Dimensions at a Glance

| Dimension | Core Question | One Word |
|-----------|--------------|----------|
| Vt — 傳統文化密度 | How many layers of time are perceptible in this space? | **Depth** |
| Vl — 光線質感 | Is light active or passive? Does it create layers? | **Layers** |
| Vr — 空間克制度 | How much has this space refused to include? | **Intention** |
| Vg — 空間幾何結構感 | Does the geometry tell your body where it is? | **Structure** |
| Ve — 時間感 | Does the space change the felt speed of time? | **Weight** |

**Memory anchor:** Depth · Layers · Intention · Structure · Weight

---

## Epistemological Position

SDIndex does not claim objectivity. It claims **trained consistency** — the same observer, applying the same standards, producing repeatable scores across time and location. This is the same epistemic status as a wine sommelier's score or an architectural critic's rating.

The framework is a **single-observer design** by intention. Cross-observer reliability testing is reserved for a future version. All 150 Gold Samples are scored by the same observer (Sabrina) under the same schema version.

---

## Vt — 傳統文化密度 (Traditional Cultural Density)

**Core question:** *How many layers of time are perceptible in this space?*

Vt measures the space's own historical and cultural density — not its external reputation or fame. A well-known site can have low Vt if it has been heavily commercialised. An obscure corner can have high Vt if its materials and spatial logic point to a longer history.

### Scoring Anchors

**Low (1–3): The space exists entirely in the present.**  
Materials are new, forms are generic, nothing points to origin or history. No layer of time is visible or sensed.  
*Reference sites:* Convenience store interior, airport transit corridor, standard hotel room.

**Mid (4–6): Cultural signals are present but surface-level.**  
You know there is tradition here, but you cannot feel its weight. The cultural content is decorative or communicated through signage rather than embodied in the space itself.  
*Reference sites:* Touristified shrine approach street, modern café with added wood panelling, museum lobby.

**High (7–10): The space is a container of time.**  
Materials, craft, and spatial logic all point toward a history longer than your own presence. You can sense the depth without reading a plaque. The cultural density is structural, not ornamental.  
*Reference sites:* Daitokuji sub-temple interior, old machiya tōma, Sugimoto Residence.

### Known Bias Risk
**Do not conflate with fame.** Kinkakuji is famous; its current Vt may be moderate due to reconstruction and tourist infrastructure. Vt scores the space in front of you, not the historical record behind it.

---

## Vl — 光線質感 (Light Quality)

**Core question:** *Is light active or passive? Does it create layers?*

Vl measures the structural role of light in the space — not brightness, not pleasantness, but whether light and shadow together form a composition. A dark space can score high if the darkness is structured. A bright space can score low if the light is uniform and directionless.

Note: Vl score must always be read together with `Vl_source` subtype. The same score under `natural_diffused` and `artificial_warm` means different things for Graph RAG retrieval.

### Scoring Anchors

**Low (1–3): Light is functional. It exists to eliminate shadow.**  
Uniform illumination, no directionality, no gradation. The goal of the lighting is clarity and efficiency. Light itself is invisible — you see through it, not with it.  
*Reference sites:* Fluorescent-lit office, convenience store, underground shopping mall corridor.

**Mid (4–6): Light has a source and direction, but limited layering.**  
Natural light enters through a window; warm artificial light suggests intention. But the relationship between light and shadow is simple — one zone bright, one zone dark, no complex gradation.  
*Reference sites:* Café with side window, traditional building with large openings, well-lit machiya with modern renovation.

**High (7–10): Light and shadow co-author the space.**  
Shadow is not the absence of light — it is light's other form. You notice light accumulating on a surface, pooling in a corner, moving slowly across a material. The composition of light and dark is as deliberate as the architecture.  
*Reference sites:* Katsura Rikyu interior, shoji screen back-light, Pontocho lantern-lit stone path at night, candlelit tea room.

### Known Bias Risk
**Do not let weather override structure.** An overcast day does not automatically lower Vl. Diffused natural light on a cloudy day can still create layered relationships with surface texture. Assess the structural logic of light, not its intensity. Record the weather and `Vl_source` — let those fields carry the context.

---

## Vr — 空間克制度 (Spatial Restraint)

**Core question:** *How much has this space refused to include?*

Vr measures conscious subtraction — the evidence of a decision not to fill, not to add, not to explain. Empty space scores high only when the emptiness is intentional. A vacant lot is not restrained; a karesansui garden is. The difference is the presence of a designing intelligence that chose the void.

### Scoring Anchors

**Low (1–3): The space operates on a filling logic.**  
Every available surface, volume, and interval is used. Information density and object density are at or near maximum. Nothing has been left out.  
*Reference sites:* Nishiki Market at peak, department store food hall, pachinko parlour.

**Mid (4–6): Order is present, but restraint is functional rather than aesthetic.**  
The space is not crowded, but the emptiness is incidental — a result of budget, use, or efficiency rather than a deliberate design choice. Tidiness without intentionality.  
*Reference sites:* Standard quality garden, clean commercial space, functional traditional building without aesthetic programme.

**High (7–10): Restraint is the primary design language.**  
The empty portions are the subject of the design, not its remainder. You can sense that decisions were made to exclude. The space communicates through what is absent as much as through what is present.  
*Reference sites:* Ryoanji stone garden, tokonoma alcove with single hanging scroll, contemporary Japanese minimal interior, Urasenke tea room.

### Known Bias Risk
**Do not conflate with emptiness.** A car park is empty; it does not score high on Vr. The criterion is **intentional subtraction**, not spatial density. If you cannot sense the designing intelligence behind the void, the score should not be high.

---

## Vg — 空間幾何結構感 (Geometric Spatial Character)

**Core question:** *Does the geometry tell your body where it is?*

Vg is the most abstract dimension and the one most prone to scoring drift. It measures whether the geometric logic of a space — its proportions, axes, thresholds, openings — produces a specific bodily awareness. A high Vg space makes you feel, without thinking, that you are in a particular kind of place, that you should move or stop in a particular way.

Note: Always record `Vg_subtype`. Vg scores mean different things depending on whether the geometry is enclosing or open, strict or organic. Two spaces with Vg = 7.5 but different subtypes are not similar for retrieval purposes.

### Scoring Anchors

**Low (1–3): Geometry is generic or incidental.**  
The space has no strong structural logic. Its proportions do not produce a specific bodily response. You could be in many places at once.  
*Reference sites:* Standard rectangular room, generic office floor plate, undifferentiated public plaza.

**Mid (4–6): A recognisable geometric logic, but not strongly felt.**  
You can identify an axis, a centre, a threshold. The space was designed with spatial intention, but the geometry does not dominate your experience.  
*Reference sites:* Tidy traditional garden with clear path, traditional building with evident but undemanding layout.

**High (7–10): Geometry is the primary experience.**  
The proportions, axes, thresholds, and openings produce a specific and undeniable bodily awareness. You know exactly where you are, where to go, or where to stop — without signage, without instruction. The geometry is acting on you.  
*Reference sites:* Katsura Rikyu path sequencing, Noh stage perfect square, karesansui stone grouping ratios, Ando Tadao's Church of Light.

### Known Bias Risk
**This is the dimension most likely to drift across 150 records.** Vg requires architectural sensitivity that is harder to maintain consistently than sensory perception. Mitigation: in Layer 2 cluster validation, Vg standard deviation below 1.0 is a flag for recalibration. When uncertain in the field, default to the `Vg_subtype` selection as an anchor before assigning the score.

---

## Ve — 時間感 (Temporal Depth)

**Core question:** *Does the space change the felt speed of time?*

Ve measures whether the space produces a physical — not merely cognitive — sense of time. It is not triggered by reading a history plaque or remembering a fact. It is the sensation of time compressed (centuries in a moss texture) or extended (ten minutes feeling like an hour). It must be felt in the body, not thought in the mind.

### Scoring Anchors

**Low (1–3): Time is linear and uniform.**  
You are fully in the present tense. Nothing in the space causes time to compress, extend, or accumulate. Efficiency and throughput are the temporal logic.  
*Reference sites:* Fast food restaurant, transport hub, functional commercial space.

**Mid (4–6): Temporal awareness is present but cognitively triggered.**  
Something prompts you to think about history or duration — a plaque, a view, a photograph. But the feeling is intellectual rather than somatic. It does not change the felt pace of your experience.  
*Reference sites:* Average historical site with good interpretation, scenic viewpoint, quality museum gallery.

**High (7–10): The space has temporal mass.**  
Time feels physically different here. You may experience compression — the sense that centuries are present in a single detail — or extension — the sense that your own duration has slowed or deepened. This is produced by the space itself, not by your prior knowledge of it.  
*Reference sites:* Saihoji (Kokedera) moss carpet, old machiya with visible wear on threshold stone, Noh performance ma (間), late afternoon light on a centuries-old wooden column.

### Known Bias Risk
**Ve is the dimension most vulnerable to observer state.** If `preloaded_knowledge_active` or `sensory_saturation_effect` flags are checked, Ve scores should be treated with caution and noted for review. High Ve scored on a day when both flags are active requires a revisit to confirm. This is why observer_flags exist — they do not invalidate the record, they contextualise it.

---

## Field Calibration: Quick Reference

Use these questions in the field when uncertain:

| Dimension | Fast calibration question |
|-----------|--------------------------|
| Vt | If I removed every sign and label, would I still sense the history? |
| Vl | Is the shadow doing something, or just sitting there? |
| Vr | What did the designer choose NOT to include here? |
| Vg | Does my body know where to go without being told? |
| Ve | Am I in the present tense, or has time shifted? |

---

## Scoring Do's and Don'ts

**Do:**
- Score what you perceive in the space right now, not what you know about it
- Use the full range (1–10); avoid clustering scores between 5–7
- Record field notes even for mid-range scores — the note is often more valuable than the number
- Flag observer state honestly in observer_flags

**Don't:**
- Score Vt by a site's reputation or UNESCO status
- Let weather determine Vl without assessing light structure
- Score Vr high just because a space is uncrowded or empty
- Score Ve high because you read something interesting about the history
- Leave Vg_subtype unselected — it is required for Graph RAG edge computation

---

## Anchor Sites (Kyoto Reference Set)

These sites serve as calibration references across the 150-record dataset. Re-score these sites after completing all records to check for drift (see VALIDATION_PROTOCOL.md Layer 1).

| Site | Vt | Vl | Vr | Vg | Ve | Notes |
|------|----|----|----|----|----|-------|
| Convenience store | 1.0 | 1.5 | 1.5 | 2.0 | 1.0 | Low-end anchor |
| Kyoto Station concourse | 2.5 | 3.0 | 2.0 | 4.0 | 2.0 | Low-mid anchor |
| Ryoanji (early morning, off-peak) | 8.5 | 7.5 | 9.5 | 9.0 | 8.5 | High-end anchor |
| Katsura Rikyu (interior) | 9.0 | 9.0 | 8.5 | 9.5 | 9.0 | Ceiling reference |

*Note: These are approximate reference values established at the start of sampling. They are not fixed truths — if re-scoring reveals consistent drift, adjust with a calibration note rather than silently editing.*

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-08 | Initial release. Five dimension standards, bias risks, field calibration guide, anchor site table. |
