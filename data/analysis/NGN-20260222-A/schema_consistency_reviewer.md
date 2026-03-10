**record\_id:** NGN-20260222-A

**schema\_completeness:** Complete. All v1.3 required fields present. `calibration_note` key is absent (consistent with Kyoto records but inconsistent with TPE-20260308-A which includes it as null — this is a known dataset-level gap flagged in the schema consistency review, not a record-level issue). `turning_point` is "none" (string), which is the QuickForm default output for empty turning\_point — acceptable given `trajectory_type = ascending_resonance` with no discrete inflection event. `counterpoint.paired_record` is null — no issue, but this record would benefit from a future pairing with a harvest-season or European vineyard record when available.

**scoring\_consistency:** Clean. Vt(8) \+ Vl(9) \+ Vr(9) \+ Vg(8.5) \+ Ve(9) \= 43.5. Stated raw\_sum \= 43.5. SDIndex \= 43.5/50×10 \= 8.7. Stated sdindex\_score \= 8.7. No arithmetic error. Score range (8.0–9.0) is the narrowest in the dataset. All scores use 0.5 increments consistent with the QuickForm slider step size.

**subtype\_trigger\_consistency:**

| Field | Value | Supported? | Note |
| ----- | ----- | ----- | ----- |
| Vt\_subtype: agricultural\_terroir | Yes | Field note describes vineyard culture, wine heritage, Japanese cultural positioning — fits agricultural\_terroir cleanly. First use of this subtype in the dataset. |  |
| Vl\_source: natural\_direct | Yes | 「無雲藍天」「陽光底下」— clear sky, direct winter sun. Correct. |  |
| Vr\_source: existential\_permission | Mostly | Field note describes non-oppressive enclosure and openness. `existential_permission` is a better fit than the original `architectural_design` (corrected in revision). Minor gap: the note doesn't explicitly describe permission to pause or exist — it describes openness and absence of pressure, which is adjacent but not identical. Acceptable at current schema precision. |  |
| Vg\_subtype: open\_unframed | Weak | Field note describes 「平行延伸的行距」「整齊劃一的柱型支架」「梯田般的坡面疊層」— these are repetitive parallel structures with rhythmic ordering. This is framed geometry, not unframed. The current Vg\_subtype vocabulary lacks a label for agricultural/rhythmic geometry. `geometric_strict` is the closest existing option but implies architectural rigidity. Flagged as a vocabulary gap in QC; not blocking but should be addressed in v1.4 schema update. |  |
| Ve\_trigger: intrinsic\_spatial | Partially | The Ve note contains two layers: (1) direct spatial response (standing at the window, overlooking vineyard and mountain) and (2) cultural-interpretive projection (「可以想像日本葡萄酒莊辛苦要在世界葡萄酒市場站穩腳步的意圖」「帶著參與日本這個文化自信的視角」). The second layer is activated by `preloaded_knowledge_active = true`, not by the space itself. Pure `intrinsic_spatial` would mean the emotional response requires no prior knowledge. This record's Ve is a blend of intrinsic spatial response and preloaded knowledge activation. `intrinsic_spatial` captures the dominant layer but erases the secondary one. |  |

**fieldnote\_vector\_alignment:**

| Dimension | Score | Note alignment | Issue |
| ----- | ----- | ----- | ----- |
| Vt=8 | Adequate | Note describes cultural positioning and heritage fusion. Content supports high Vt but is more interpretive than observational — describes what the site represents rather than what heritage features are physically visible. Acceptable for agricultural\_terroir where cultural density is partly conceptual. |  |
| Vl=9 | Strong | 「無雲藍天」「淺間山的輪廓很清楚」「動態的光線在靜態的結構中流動」— specific light phenomena described with spatial referents. Best-supported Vl note in the dataset so far. |  |
| Vr=9 | Adequate | 「被群山包圍，但絲毫沒有壓迫感」「開闊性呈現」— captures the experiential quality but is relatively short for a 9\. Two observable features (mountain enclosure \+ openness) meet the minimum threshold. |  |
| Vg=8.5 | Strong | 「葡萄藤平行延伸的行距」「整齊劃一的柱型支架」「梯田般的坡面疊層」— three specific geometric features named. Note is well-placed in the correct field (lesson learned from earlier records where geometric descriptions drifted into Vr or Ve). |  |
| Ve=9 | Adequate | Describes a specific moment (standing at window with wine, overlooking vineyard and mountain) and a cultural projection. The note conflates bodily experience with interpretive projection without separating them. Preloaded knowledge influence is not marked. Functional but could be more precise about what makes this a 9 vs. an 8\. |  |

**asset\_class\_assessment:** Gold\_Sample designation is justified. The record has the dataset's highest SDIndex, introduces a new site\_type with clean dimensional logic, passes arithmetic verification, and has no major structural issues. The Vg\_subtype vocabulary gap and the Ve trigger blending are minor issues that don't compromise the record's analytical usability. The research\_finding is well-formed and dataset-functional. The record's primary value is as a portability proof and high-end anchor — both functions are served in current form.

**key\_risks:**

1. **Vg\_subtype vocabulary gap (low risk, schema-level).** `open_unframed` doesn't match the agricultural geometry described. This will recur with any future vineyard, orchard, or terraced landscape record. Needs a v1.4 vocabulary addition, not a record-level fix.

2. **Ve trigger blending (low risk, documentation-level).** Ve=9 is driven by both intrinsic spatial response and preloaded cultural knowledge. The current single-label trigger system can't capture this. Low risk because the Ve note itself documents both layers — the information is recoverable even if the label is reductive.

3. **Preloaded knowledge unmarked in field notes (low risk).** `preloaded_knowledge_active = true` is flagged but no field note identifies where this knowledge enters the observation. The Ve note is the obvious location. A single sentence marking the influence would close this gap.

**recommended\_action:**

* No structural revision required.  
* Optional: add one sentence to Ve note marking preloaded knowledge influence.  
* Schema-level: flag `Vg_subtype` vocabulary for v1.4 expansion (add agricultural/rhythmic geometry option).  
* Schema-level: consider whether `Ve_trigger` should support compound values or a secondary trigger field for records where multiple trigger types co-exist.

