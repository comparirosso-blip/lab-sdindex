## [v1.4] — 2026-03-14

### Added
- `Ve_valence` field (enum: positive / negative / ambivalent / neutral): Same Ve intensity can carry opposite emotional direction — Katsura's Ve is 寂寞 (loneliness) not 寂靜 (serenity). Required for training bucket differentiation.
- `phenomenology_mode` field (enum: pure / mediated / augmented): Classifies observation's phenomenological purity. Determines training bucket assignment: pure → core_sensory_ground_truth, mediated → mediated_phenomenology, augmented → augmented_phenomenology. Critical for preventing AI-augmented data from being misused as baseline sensory truth.
- `heritage_adaptive_reuse` added to `site_type` enum: Covers repurposed historical buildings (industrial conversions, warehouse galleries, etc.) — needed for September Europe sampling.
- `active_information_retrieval` added to `Ve_trigger` enum: Observer actively uses AI to retrieve contextual knowledge during visit, distinct from passive AI narration (`external_narrative_AI`) or pure spatial response (`intrinsic_spatial`). Identified from Katsura Ve mechanism ambiguity.
- `industrial_heritage` added to `site_type` enum.
- `industrial_historical` added to `Vt_subtype` enum.
- `commercial_flow_control` and `natural_topography` added to `Vr_source` enum.
- `asset_class` updated to three-tier gold system: `gold_sample_pure` / `gold_sample_mediated` / `gold_sample_augmented` + `reference_baseline` / `exploratory` / `conditional`.

### Changed
- `sensory_resilience` (single field) → `resilience` (object with two independent dimensions):
  - `formal_aesthetic_resilience`: Space's intrinsic capacity to maintain perceptual richness under stress. Measures architecture/design properties ONLY. Invariant under access system changes.
  - `phenomenological_access_freedom`: Degree of freedom observer has to self-pace attention, movement, and temporal exploration. Measures access system/institutional structure ONLY. Invariant under space aesthetic quality changes.
  - `resilience_note`: Optional text explaining divergence between the two dimensions.
- `schema_version` updated to `"1.4"`.

### Rationale
Three diagnostic sessions (Katsura deep dive, LaLaport cross-domain analysis, Ninenzaka QC review) revealed:
1. Ve mechanism ambiguity requires explicit trigger + valence separation (Katsura: same high Ve score encoded opposite emotional meanings depending on interpretation).
2. Resilience conflates space quality with observer freedom — Katsura has exceptional formal resilience but medium-low access freedom due to guided-tour pacing. These must be independent measurements.
3. Phenomenology mode is the missing variable for responsible AI training — without it, AI-augmented observations contaminate baseline sensory truth datasets.
4. September Europe trip will encounter heritage adaptive reuse sites (Gasometer Vienna, Tate Modern, etc.) not covered by existing site_type enum.

### QuickForm
- `CKV_QuickForm_v1.4.1.html`: Updated to match all schema v1.4 changes. Step 2 (標註) now includes Ve valence buttons, split resilience with hint text, and phenomenology mode selector. Output summary shows FAR/PAF split.

### Migration Note
Records created with v1.3 remain valid. The `sensory_resilience` field in v1.3 records maps approximately to `formal_aesthetic_resilience` in v1.4; `phenomenological_access_freedom` was not captured in v1.3 and should be retrospectively assessed during the dataset stratification audit.
