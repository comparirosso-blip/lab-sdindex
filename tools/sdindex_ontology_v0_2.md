# SDIndex Fieldwork — Ontology v0.2

**Sabrina's Pause · CKE Lab**
Based on CKV Schema v1.4 · QuickForm v1.4
March 2026 · Taipei / Kyoto

> Supersedes Ontology v0.1. Changes marked with `[v0.2]`.

---

## 一、系統目的 Purpose

建立一套跨文本與跨場域的結構化知識系統，讓「AI共寫文本」與「人類田野感知紀錄」能被標定、互相連接、可檢索、可推理、可比較。

This ontology defines the data architecture for the SDIndex fieldwork corpus (FieldRecord) and its future integration with the Article/Library corpus. It serves as the shared language for all AI agents working with this archive.

---

## 二、節點類型 Node Types

| 節點 | 說明 | 資料來源 |
| :---- | :---- | :---- |
| FieldRecord | 田野觀測紀錄，含五向量標註 | CKV QuickForm v1.4 / JSON |
| Article | 思想文本，含8維標註 | Notion Library / Journal |
| Space | 具體場域（地點實體） | FieldRecord 的 location 欄位 |
| Concept | 跨corpus核心概念 | free_keywords 升格候選 + 固定概念如 BadFaith™、Ve activation |
| Book | 五本書稿 | Archive / GitHub JSON |
| Person | 作者、引用思想家 | 如 Lynch、Whyte、Perec、Akiko Freeman |
| SensoryEvent | 餐酒會、音樂會、茶道等事件型場域 | field_type: sensory_event 的 FieldRecord |

---

## 三、FieldRecord 完整欄位 Schema

### 3.1 基本資訊 Meta

| 欄位 | 類型 | 說明 / 選項 |
| :---- | :---- | :---- |
| site_name_zh | text | 地名（中文） |
| site_name_en | text | 地名（英文） |
| site_name_local | text | 地名（當地語言，optional） |
| city | text | 城市，如 Kyoto / Taipei |
| region | text | 地區代碼，如 KYT / TPE |
| country | text | 國家代碼，如 JP / TW |
| date | date | 田野日期，格式 YYYY-MM-DD |
| site_type | select | 見 3.2 |
| visit_mode | select | 見 3.3 |
| companion | text | 同行者，如 solo / 老公 |
| weather | text | 晴、陰、雨... |
| season | select | winter / early_spring / spring / summer / autumn / late_autumn |
| time_of_day | select | morning / midday / afternoon / evening / night / full_day |
| crowd_density | select | empty / very_low / low / moderate / high / crowded |
| field_type | select | architectural / sensory_event |

### 3.2 場域類型 site_type

| 值 | 說明 | 版本 |
| :---- | :---- | :---- |
| zen_temple_garden | 禪宗寺院庭園 | v1.0 |
| imperial_garden | 皇家園林 | v1.0 |
| urban_public_space | 城市公共空間 | v1.0 |
| agricultural_terroir | 農業風土場域 | v1.0 |
| winery_vineyard | 酒莊葡萄園 | v1.0 |
| immersive_overnight | 沉浸式過夜體驗 | v1.0 |
| natural_landscape | 自然景觀 | v1.0 |
| commercial_district | 商業區 | v1.0 |
| interview_accompanied | 訪談陪同型 | v1.0 |
| **heritage_adaptive_reuse** | **歷史建築轉型為現代功能，歷史層仍可感知** | **[v0.2] v1.4 NEW** |
| other | 其他 | v1.0 |

**heritage_adaptive_reuse 使用準則：**
- ✓ 使用：歷史建築被轉化為餐廳、旅館、商業空間、展覽空間，且再利用本身構成感知的一部分
- ✗ 不使用：純寺院、純庭園、純遺址（用既有類型）；單純現代仿古空間

### 3.3 參訪模式 visit_mode

| 值 | 說明 |
| :---- | :---- |
| solo_free | 獨自自由參訪 |
| couple_free | 雙人自由參訪 |
| guided_tour | 導覽參觀 |
| interview_accompanied | 訪談陪同 |
| immersive_overnight | 沉浸過夜 |
| repeat_visit | 重複參訪 |

---

## 四、五感向量 Five Sensory Vectors

所有向量評分範圍：0.0 – 10.0（步進 0.5）。每個向量附有 field note 文字欄位。

| 向量 | 中文標籤 | 測量對象 |
| :---- | :---- | :---- |
| Vt | 傳統文化密度 | 場域中傳統文化符號、歷史積澱、儀式感的濃度 |
| Vl | 光線質感 | 光源類型、光線方向性、明暗對比、漫射程度 |
| Vr | 材質與觸感 | 人體與環境之間的物理介面：建築材料、器皿、溫度、質地 |
| Vg | 空間幾何結構感 | 空間的幾何秩序、視覺引導、層次感、邊界清晰度 |
| Ve | 時間感（強度） | 場域誘發的時間感知強度：壓縮、延展、凝止、分層 |

### 4.1 向量子類型 Subtypes

**Vt 子類型**

| 值 | 說明 |
| :---- | :---- |
| architectural_heritage | 建築遺產型 |
| agricultural_terroir | 農業風土型 |
| biographical_founder | 創始人傳記型 |
| intangible_practice | 非物質文化實踐型 |
| corporate_constructed | 企業建構型 |
| non_intervention_natural | 無干預自然型 |

**Vl 光源類型**

| 值 | 說明 |
| :---- | :---- |
| natural_diffused | 自然漫射光 |
| natural_direct | 自然直射光 |
| artificial_warm | 人工暖光 |
| artificial_neutral | 人工中性光 |
| mixed | 混合光源 |
| candlelight_lantern | 燭光 / 燈籠 |

**Vr 來源**

| 值 | 說明 |
| :---- | :---- |
| architectural_design | 建築設計本身的材質選擇 |
| social_protocol | 社會禮儀約定產生的克制感 |
| invited_openness | 邀請式開放感 |
| cognitive_compression | 認知壓縮型 |
| existential_permission | 存在許可型 |
| guided_tour_managed | 導覽管理型 |

**Vg 幾何子類型**

| 值 | 說明 | 版本 |
| :---- | :---- | :---- |
| enclosure_deep | 深度圍合 | v1.0 |
| enclosure_shallow | 淺度圍合 | v1.0 |
| open_framed | 有框開放 | v1.0 |
| open_unframed | 無框開放 | v1.0 |
| layered_threshold | 層疊門檻 | v1.0 |
| void_centred | 虛空中心 | v1.0 |
| geometric_strict | 幾何嚴謹 | v1.0 |
| geometric_organic | 幾何有機 | v1.0 |
| **agricultural_rhythmic** | **農業排列形成的幾何節奏（葡萄藤行距/茶田階梯/牧場圍欄）** | **[v0.2] v1.4 NEW** |

**agricultural_rhythmic 使用準則：**
- ✓ 使用：空間秩序來自重複性農業邏輯；幾何是土地使用節律而非建築軸線
- ✗ 不使用：只是自然景觀的無序開放（用 open_unframed）；幾何主導來自建築 enclosure

**Ve 啟動機制**

| 值 | 說明 | 版本 |
| :---- | :---- | :---- |
| external_narrative_AI | 外部敘事介入（AI） | v1.0 |
| external_narrative_human | 外部敘事介入（人類） | v1.0 |
| preloaded_knowledge | 預載知識激活（進場前已知） | v1.0 |
| intrinsic_spatial | 空間本身固有誘發 | v1.0 |
| self_time_projection | 自我時間投射 | v1.0 |
| **active_information_retrieval** | **體驗中主動查詢（AI/Google/官網）使時間感發生轉折** | **[v0.2] v1.4 NEW** |
| none | 無明確啟動機制 | v1.0 |

**active_information_retrieval 與鄰近值的區分：**

| 值 | 時間點 | 來源 | 主動性 |
| :---- | :---- | :---- | :---- |
| preloaded_knowledge | 進場前 | 任何 | 被動（已積累） |
| external_narrative_human | 體驗中 | 他人口述 | 被動（接收） |
| active_information_retrieval | 體驗中 | 數位/紙本查詢 | **主動（觀察者發起）** |

---

## 五、[v0.2 NEW] Ve_valence — 時間感效價

`Ve_valence` 是 v1.4 新增的 **Layer 1 Measurement** 欄位，與 `Ve` 構成正交測量對。

| 欄位 | 測量維度 |
| :---- | :---- |
| Ve | 時間感強度（0.0–10.0） |
| Ve_valence | 時間感效價（-1.0 to +1.0） |

### 評分標準

| 值 | 標籤 | 感官基準 | 判斷語句 |
| :---- | :---- | :---- | :---- |
| **+1.0** | Positive Expansion | 時間被安放、凝止是愉悅的；常伴隨 absorption / resonance / stillness | 「想停久一點」「時間像靜下來」「離開時有被收留的感覺」 |
| **+0.5** | Mildly Positive | 輕微愉悅延展；有想多留一會兒的感覺 | |
| **0.0** | Neutral / Mixed | 時間感被明顯感知，但難以判定正負；常見於高度資訊化或儀式化場域 | 「時間感有變，但不特別愉悅或不適」 |
| **-0.5** | Mildly Negative | 略顯沉重，但不至於完全負向 | |
| **-1.0** | Negative Compression | 時間被感知為拖累、壓迫、困住；常伴隨 impatience / claustrophobia / overstimulation | 「時間像被卡住」「越待越累」 |

**必填條件：** `Ve > 0` 時必填；`Ve = 0` 時可填（建議）。
**不污染原則：** `Ve_valence` 不影響 `Ve` 分數或 `sdindex_score`。

### Graph-RAG 應用

`Ve_valence` 啟用以下查詢類型：
- "找出所有時間感強（Ve ≥ 7）但效價負向的場域" → 壓迫性場域研究
- "比較同一場域不同季節的效價變化" → 配合 `temporal_variant_of` 使用
- "哪些場域達到 Ve_valence = +1.0？它們的 Vg_subtype 分布如何？" → 正向凝止的幾何條件

---

## 六、[v0.2 NEW] free_keywords — 自由現象學關鍵字

### 欄位定義

| 屬性 | 值 |
| :---- | :---- |
| Layer | Layer 2 — Semantic |
| 類型 | array\<string\> |
| Max items | 3 |
| Required | No |

### 功能定位

`free_keywords` 是 Ontology 中 `Concept` 節點的**候選種子層**。

**Subtype（固定詞表）vs free_keywords（自由詞）的功能分工：**

| | Subtype | free_keywords |
| :---- | :---- | :---- |
| 回答問題 | 「結構來源/幾何類型是什麼」 | 「感知現象像什麼/值得成為概念節點」 |
| 詞表性質 | 固定，controlled vocabulary | 自由，observer-generated |
| 層次 | 結構描述 | 現象描述 |

**Hard Rule：** free_keywords 不得重複 subtype 名稱或其近義重述。

### 有效範例

| ✓ 有效 | 說明 |
| :---- | :---- |
| ceremonial_slowness | 儀式性的緩慢感，超越單純的時間延展 |
| borrowed_dignity | 借用歷史或他人權威所產生的身份感 |
| managed_silence | 被設計或管理出來的靜默，而非自然靜默 |
| socially_suspended_time | 社會情境使時間感被集體暫停 |

| ✗ 無效 | 原因 |
| :---- | :---- |
| layered_threshold | 已是 Vg_subtype，語義重複 |
| AI_trigger | active_information_retrieval 的近義縮寫 |
| beautiful | 純情緒詞，不具現象描述性 |

### 升格規則（Concept Node Promotion）

某 free_keyword 若在 corpus 中重複出現 ≥ 3 次，且語義穩定，可在後續 Ontology 版本評估升格為 controlled `Concept` node，並建立正式的 `activates` 關係。

---

## 七、[v0.2 NEW] Relation Tags — 記錄關係標記

Relation tags 屬於 **Layer 2 — Semantic / graph linkage layer**，不參與分數計算。

### 7.1 FieldRecord 間關係類型

| 關係 | 說明 | 連結方向 |
| :---- | :---- | :---- |
| **temporal_variant_of** | 同一場域在不同物候/季節/時段下的變體 | FieldRecord → FieldRecord |
| **counterpoint_of** | 結構性對照：感知邏輯形成鮮明反差 | FieldRecord ↔ FieldRecord |
| **sensory_mirror_of** | 跨場域類型的感知共振：不同空間共享相似現象學結構 | FieldRecord ↔ FieldRecord |

**使用準則對比：**

| 關係 | 場域類型相同？ | 感知結構相似？ | 目的 |
| :---- | :---- | :---- | :---- |
| temporal_variant_of | ✓（同一地點）| — | 時間/物候變化追蹤 |
| counterpoint_of | 通常不同 | ✗ 對立 | 對照組分析 |
| sensory_mirror_of | 不同 | ✓ 相似 | 跨類型概念共振 |

### 7.2 跨 Corpus 關係類型（v0.1 保留）

| 關係 | 從 | 到 | 說明 |
| :---- | :---- | :---- | :---- |
| references | Article | Book | 文章引用書稿 |
| embodies | Article | Concept | 文章體現某核心概念 |
| observes | FieldRecord | Space | 田野記錄對應的實體場域 |
| activates | Space | Concept | 場域觸發某概念（如 Ve activation） |
| resonates_with | Article | FieldRecord | 文本與田野在結構上呼應 |
| influences | Person | Concept | 思想家影響某概念形成 |
| documents | FieldRecord | SensoryEvent | 記錄特定感官事件 |

---

## 八、情感軌跡 Emotion Trajectory

| 欄位 | 類型 | 說明 |
| :---- | :---- | :---- |
| entry_state | text | 入場狀態：高期待 / 零預期 / 感官疲勞 / 旅途放鬆... |
| turning_point | text | 轉折點（無則留空） |
| exit_state | text | 離場狀態：共鳴 / 平靜 / 身體放鬆 / 被收留... |
| trajectory_type | select | 見下表 |
| key_insight | text | 核心洞察：這個場域給你最精準的一句話 |

**trajectory_type 選項**

| 值 | 說明 |
| :---- | :---- |
| expectation_collapse_reframe | 預期崩解後重構 |
| flat_positive | 平穩正向 |
| ascending_resonance | 上升共鳴 |
| melancholy_empathy | 憂鬱共情 |
| intellectual_compression | 智識壓縮 |
| existential_release | 存在釋放 |
| surprise_delight | 意外喜悅 |
| other | 其他 |

---

## 九、額外標記 Extra Flags

| 欄位 | 類型 | 說明 |
| :---- | :---- | :---- |
| sensory_saturation_effect | checkbox | 感官飽和效應（看太多同類場域） |
| preloaded_knowledge | checkbox | 預載知識激活（書稿/研究背景投射） |
| ai_collaboration | checkbox | 現場 AI 協作（即時資訊輔助） |
| repeat_visit | checkbox | 重複參訪（非首次） |
| ideal_condition | text | 最佳採樣條件：早晨7點前、非楓葉季... |
| research_finding | text | 研究發現：此記錄對論文的特殊貢獻、異常發現 |

---

## 十、三層結構模型 Three-Layer Architecture

```
Layer 1 — Measurement（測量層）
  vs_vector: { Vt, Vl, Vr, Vg, Ve }
  ve_valence: float (-1.0 to 1.0)        ← v1.4 NEW
  sdindex_score
  sensory_resilience

  規則：所有 Layer 2 / Layer 3 欄位不得直接修改 Layer 1 值

Layer 2 — Semantic（語義層）
  vs_subtypes: { Vt_subtype, Vl_source, Vr_source, Vg_subtype, Ve_trigger }
  free_keywords: array<string> max 3     ← v1.4 NEW
  relations: { temporal_variant_of,
               counterpoint_of,
               sensory_mirror_of }       ← v1.4 NEW

  規則：Subtype 描述結構來源；free_keywords 描述感知現象
  規則：free_keywords 不得重複 subtype 名稱

Layer 3 — Narrative（敘事層）
  field_notes: { Vt, Vl, Vr, Vg, Ve }
  emotion_trajectory
  ideal_condition
  research_finding
```

---

## 十一、跨 Corpus 對位欄位 Ontology Bridge

（v0.1 保留，新增 Ve_valence 對位）

| Article 維度 | FieldRecord 維度 | 對位邏輯 |
| :---- | :---- | :---- |
| Space_Pattern: enclosure | Vg_subtype: enclosure_deep / enclosure_shallow + Vr high | 邊界感強、材質包覆、聲音反射密 |
| Space_Pattern: vertical | Vg_subtype: void_centred + Vg high | 垂直視覺主導，向上延伸感 |
| Space_Pattern: dissolution | Vg_subtype: open_unframed + Ve high | 邊界模糊、情感滲透、空間溢出 |
| Space_Pattern: threshold | Vg_subtype: layered_threshold | 過渡感、入口意識、門檻體驗 |
| Space_Pattern: ambient | Vg low + crowd_density low + Vl: natural_diffused | 瀰漫式、無中心、感知均布 |
| Intent_Vector: inward | Ve low + trajectory: intellectual_compression | 向內收攏的感知與思想狀態 |
| Intent_Vector: outward | Ve high + trajectory: ascending_resonance | 向外擴散的感知與召喚狀態 |
| Intent_Vector: recursive | Ve_trigger: preloaded_knowledge / active_information_retrieval + ai_collaboration | 自我指涉的認知迴路 |
| Time_Velocity: arrested | Ve low + Ve_valence: +0.5 to +1.0 | 凝止是愉悅的停止，非壓迫 |
| Time_Velocity: compressed | Ve high + Ve_valence: -0.5 to -1.0 | **[v0.2]** 焦慮壓縮型，區別於愉悅延展 |
| Time_Velocity: layered | Ve: self_time_projection + turning_point 有值 | 多重時間層並存 |
| Confidence: 0.9+ | research_finding 有值 + sensory_saturation = false | 高確信度觀察，非疲勞狀態 |
| Evidence_Type: phenomenological | entry_state 有值 + ai_collaboration = false | 純粹第一人稱感知，無AI介入 |

---

## 十二、Concept Node 生長機制

```
free_keywords（每筆 FieldRecord 可有 0-3 個）
    ↓ 重複出現 ≥ 3 次且語義穩定
Concept Node（Ontology 正式節點）
    ↓ 建立關係
activates（Space → Concept）
embodies（Article → Concept）
influences（Person → Concept）
```

**目前 Concept Node 候選追蹤（corpus 中出現次數）：**

| keyword | 出現次數 | 狀態 |
| :---- | :---- | :---- |
| — | — | 待 v1.4 記錄積累後更新 |

---

## 十三、待定義欄位 Pending

| 欄位 | 現況 | 待辦 |
| :---- | :---- | :---- |
| Noise（Article corpus） | JSON中出現 Traffic / Urban / Soft 等值 | 正式定義選項清單 |
| ptv（Article corpus） | JSON中有向量值 [0.3, 0.2, 0.9, 0.7, 0.8] | 確認五個分量的語義定義 |
| counterpointIds（Article） | JSON中有此欄位但邏輯未確認 | 與 FieldRecord 的 counterpoint_of 對齊關係邏輯 |
| SDIndex 總分計算公式 | 目前等權加總 | 確認五向量是否需要差異加權 |
| field_type: sensory_event | schema 已定義 | QuickForm 尚未實作此分支 |

---

## 附錄：v1.4 JSON Schema diff（新增欄位）

```json
{
  "ve_valence": {
    "type": "number",
    "minimum": -1.0,
    "maximum": 1.0,
    "description": "Hedonic tone of Ve. +1=positive temporal expansion, 0=neutral, -1=negative compression. Layer 1 Measurement."
  },
  "free_keywords": {
    "type": "array",
    "items": { "type": "string", "pattern": "^[a-z][a-z0-9_]*$" },
    "maxItems": 3,
    "description": "Phenomenological concept seed candidates for Ontology Concept nodes. Layer 2 Semantic."
  },
  "relations": {
    "type": "object",
    "properties": {
      "temporal_variant_of": { "type": ["string", "null"] },
      "counterpoint_of": { "type": ["string", "null"] },
      "sensory_mirror_of": { "type": ["string", "null"] }
    },
    "additionalProperties": false,
    "description": "Graph-RAG linkage layer. Values are FieldRecord IDs or null. Layer 2 Semantic."
  }
}
```

**Default values for backward compatibility:**
```json
{
  "ve_valence": 0.0,
  "free_keywords": [],
  "relations": {
    "temporal_variant_of": null,
    "counterpoint_of": null,
    "sensory_mirror_of": null
  }
}
```

---

*Sabrina's Pause — Ontology v0.2*
*Generated March 2026 · Supersedes v0.1 · For AI agent use and cross-session communication*
*schema_version: CKV v1.4 · QuickForm v1.4*
