**Sabrina's Pause**

SDIndex Fieldwork — Ontology v0.1

Based on CKV QuickForm v1.3

March 2026 · Taipei / Kyoto

# **一、系統目的 Purpose**

建立一套跨文本與跨場域的結構化知識系統，讓「AI共寫文本」與「人類田野感知紀錄」能被標定、互相連接、可檢索、可推理、可比較。

This ontology defines the data architecture for the SDIndex fieldwork corpus (FieldRecord) and its future integration with the Article/Library corpus. It serves as the shared language for all AI agents working with this archive.

# **二、節點類型 Node Types**

| 節點 | 說明 | 資料來源 |
| :---- | :---- | :---- |
| FieldRecord | 田野觀測紀錄，含五向量標註 | CKV QuickForm v1.3 / JSON |
| Article | 思想文本，含8維標註 | Notion Library / Journal |
| Space | 具體場域（地點實體） | FieldRecord 的 location 欄位 |
| Concept | 跨corpus核心概念 | 如 BadFaith™、Ve activation、Mirroring |
| Book | 五本書稿 | Archive / GitHub JSON |
| Person | 作者、引用思想家 | 如 Lynch、Whyte、Perec、Akiko Freeman |
| SensoryEvent | 餐酒會、音樂會、茶道等事件型場域 | field\_type: sensory\_event 的 FieldRecord |

# **三、FieldRecord 完整欄位 Schema**

## **3.1 基本資訊 Meta**

| 欄位 | 類型 | 說明 / 選項 |
| :---- | :---- | :---- |
| site\_name\_zh | text | 地名（中文） |
| site\_name\_en | text | 地名（英文） |
| site\_name\_local | text | 地名（當地語言，optional） |
| city | text | 城市，如 Kyoto / Taipei |
| region | text | 地區代碼，如 KYT / TPE |
| country | text | 國家代碼，如 JP / TW |
| date | date | 田野日期，格式 YYYY-MM-DD |
| site\_type | select | 見 3.2 |
| visit\_mode | select | 見 3.3 |
| companion | text | 同行者，如 solo / 老公 |
| weather | text | 晴、陰、雨... |
| season | select | winter / early\_spring / spring / summer / autumn / late\_autumn |
| time\_of\_day | select | morning / midday / afternoon / evening / night / full\_day |
| crowd\_density | select | empty / very\_low / low / moderate / high / crowded |
| field\_type | select | architectural / sensory\_event（v0.1 新增） |

## **3.2 場域類型 site\_type**

| 值 | 說明 |
| :---- | :---- |
| zen\_temple\_garden | 禪宗寺院庭園 |
| imperial\_garden | 皇家園林 |
| urban\_public\_space | 城市公共空間 |
| agricultural\_terroir | 農業風土場域 |
| winery\_vineyard | 酒莊葡萄園 |
| immersive\_overnight | 沉浸式過夜體驗 |
| natural\_landscape | 自然景觀 |
| commercial\_district | 商業區 |
| interview\_accompanied | 訪談陪同型 |
| other | 其他 |

## **3.3 參訪模式 visit\_mode**

| 值 | 說明 |
| :---- | :---- |
| solo\_free | 獨自自由參訪 |
| couple\_free | 雙人自由參訪 |
| guided\_tour | 導覽參觀 |
| interview\_accompanied | 訪談陪同 |
| immersive\_overnight | 沉浸過夜 |
| repeat\_visit | 重複參訪 |

# **四、五感向量 Five Sensory Vectors**

所有向量評分範圍：0.0 – 10.0（步進 0.5）。每個向量附有 field note 文字欄位。

| 向量 | 中文標籤 | 測量對象 | v0.1 定義更新 |
| :---- | :---- | :---- | :---- |
| Vt | 傳統文化密度 | 場域中傳統文化符號、歷史積澱、儀式感的濃度 | — |
| Vl | 光線質感 | 光源類型、光線方向性、明暗對比、漫射程度 | — |
| Vr | 材質與觸感 | 人體與環境之間的物理介面：建築材料、器皿、溫度、質地。擴展至餐酒、茶道等感官事件場域的器物觸感 | 已擴展：從建築表面延伸至所有可感知的物理質地介面 |
| Vg | 空間幾何結構感 | 空間的幾何秩序、視覺引導、層次感、邊界清晰度 | — |
| Ve | 時間感 | 場域誘發的時間感知：壓縮、延展、凝止、分層 | — |

## **4.1 向量子類型 Subtypes**

**Vt 子類型**

| 值 | 說明 |
| :---- | :---- |
| architectural\_heritage | 建築遺產型 |
| agricultural\_terroir | 農業風土型 |
| biographical\_founder | 創始人傳記型 |
| intangible\_practice | 非物質文化實踐型 |
| corporate\_constructed | 企業建構型 |
| non\_intervention\_natural | 無干預自然型 |

**Vl 光源類型**

| 值 | 說明 |
| :---- | :---- |
| natural\_diffused | 自然漫射光 |
| natural\_direct | 自然直射光 |
| artificial\_warm | 人工暖光 |
| artificial\_neutral | 人工中性光 |
| mixed | 混合光源 |
| candlelight\_lantern | 燭光 / 燈籠 |

**Vr 來源**

| 值 | 說明 |
| :---- | :---- |
| architectural\_design | 建築設計本身的材質選擇 |
| social\_protocol | 社會禮儀約定產生的克制感 |
| invited\_openness | 邀請式開放感 |
| cognitive\_compression | 認知壓縮型 |
| existential\_permission | 存在許可型 |
| guided\_tour\_managed | 導覽管理型 |

**Vg 幾何子類型**

| 值 | 說明 |
| :---- | :---- |
| enclosure\_deep | 深度圍合 |
| enclosure\_shallow | 淺度圍合 |
| open\_framed | 有框開放 |
| open\_unframed | 無框開放 |
| layered\_threshold | 層疊門檻 |
| void\_centred | 虛空中心 |
| geometric\_strict | 幾何嚴謹 |
| geometric\_organic | 幾何有機 |

**Ve 啟動機制**

| 值 | 說明 |
| :---- | :---- |
| external\_narrative\_AI | 外部敘事介入（AI） |
| external\_narrative\_human | 外部敘事介入（人類） |
| preloaded\_knowledge | 預載知識激活 |
| intrinsic\_spatial | 空間本身固有誘發 |
| self\_time\_projection | 自我時間投射 |
| none | 無明確啟動機制 |

# **五、情感軌跡 Emotion Trajectory**

| 欄位 | 類型 | 說明 |
| :---- | :---- | :---- |
| entry\_state | text | 入場狀態：高期待 / 零預期 / 感官疲勞 / 旅途放鬆... |
| turning\_point | text | 轉折點（無則留空）：歷史敘事介入 / 知識突然激活... |
| exit\_state | text | 離場狀態：共鳴 / 平靜 / 身體放鬆 / 被收留... |
| trajectory\_type | select | 見下表 |
| key\_insight | text | 核心洞察：這個場域給你最精準的一句話 |

**trajectory\_type 選項**

| 值 | 說明 |
| :---- | :---- |
| expectation\_collapse\_reframe | 預期崩解後重構 |
| flat\_positive | 平穩正向 |
| ascending\_resonance | 上升共鳴 |
| melancholy\_empathy | 憂鬱共情 |
| intellectual\_compression | 智識壓縮 |
| existential\_release | 存在釋放 |
| surprise\_delight | 意外喜悅 |
| other | 其他 |

# **六、額外標記 Extra Flags**

| 欄位 | 類型 | 說明 |
| :---- | :---- | :---- |
| sensory\_saturation\_effect | checkbox | 感官飽和效應（看太多同類場域） |
| preloaded\_knowledge | checkbox | 預載知識激活（書稿/研究背景投射） |
| ai\_collaboration | checkbox | 現場 AI 協作（即時資訊輔助） |
| repeat\_visit | checkbox | 重複參訪（非首次） |
| paired\_record | text | 配對記錄 ID，如 KYT-20260324-A |
| ideal\_condition | text | 最佳採樣條件：早晨7點前、非楓葉季... |
| research\_finding | text | 研究發現：此記錄對論文的特殊貢獻、異常發現 |

# **七、關係類型 Relation Types**

以下定義 FieldRecord corpus 與 Article corpus 之間，以及各節點之間的關係類型，為未來 Graph RAG 接入的基礎。

| 關係 | 從 | 到 | 說明 |
| :---- | :---- | :---- | :---- |
| references | Article | Book | 文章引用書稿 |
| embodies | Article | Concept | 文章體現某核心概念 |
| observes | FieldRecord | Space | 田野記錄對應的實體場域 |
| activates | Space | Concept | 場域觸發某概念（如 Ve activation） |
| resonates\_with | Article | FieldRecord | 文本與田野在結構上呼應 |
| influences | Person | Concept | 思想家影響某概念形成 |
| counterpoint\_of | FieldRecord | FieldRecord | 對照組配對記錄 |
| documents | FieldRecord | SensoryEvent | 記錄特定感官事件 |

# **八、跨Corpus對位欄位 Ontology Bridge**

這是兩個 corpus 能夠對話的核心。以下欄位在 Article 與 FieldRecord 之間具有語義對位能力。

| Article 維度 | FieldRecord 維度 | 對位邏輯 |
| :---- | :---- | :---- |
| Space\_Pattern: enclosure | Vg\_subtype: enclosure\_deep / enclosure\_shallow \+ Vr high | 邊界感強、材質包覆、聲音反射密 |
| Space\_Pattern: vertical | Vg\_subtype: void\_centred \+ Vg high | 垂直視覺主導，向上延伸感 |
| Space\_Pattern: dissolution | Vg\_subtype: open\_unframed \+ Ve high | 邊界模糊、情感滲透、空間溢出 |
| Space\_Pattern: threshold | Vg\_subtype: layered\_threshold | 過渡感、入口意識、門檻體驗 |
| Space\_Pattern: ambient | Vg low \+ crowd\_density low \+ Vl: natural\_diffused | 瀰漫式、無中心、感知均布 |
| Intent\_Vector: inward | Ve: low \+ trajectory: intellectual\_compression | 向內收攏的感知與思想狀態 |
| Intent\_Vector: outward | Ve: high \+ trajectory: ascending\_resonance | 向外擴散的感知與召喚狀態 |
| Intent\_Vector: recursive | Ve\_trigger: preloaded\_knowledge \+ ai\_collaboration | 自我指涉的認知迴路 |
| Time\_Velocity: arrested | Ve low \+ temporal感: 凝止 | 時間靜止感 |
| Time\_Velocity: layered | Ve: self\_time\_projection \+ turning\_point 有值 | 多重時間層並存 |
| Confidence: 0.9+ | research\_finding 有值 \+ sensory\_saturation \= false | 高確信度觀察，非疲勞狀態 |
| Evidence\_Type: phenomenological | entry\_state 有值 \+ ai\_collaboration \= false | 純粹第一人稱感知，無AI介入 |

# **九、待定義欄位 Pending**

| 欄位 | 現況 | 待辦 |
| :---- | :---- | :---- |
| Noise（Article corpus） | JSON中出現 Traffic / Urban / Soft 等值 | 正式定義選項清單 |
| ptv（Article corpus） | JSON中有向量值 \[0.3, 0.2, 0.9, 0.7, 0.8\] | 確認五個分量的語義定義 |
| counterpointIds（Article） | JSON中有此欄位但邏輯未確認 | 與 FieldRecord 的 paired\_record 對齊關係邏輯 |
| SDIndex 總分計算公式 | 目前手動給分 | 確認五向量加權方式 |

Sabrina's Pause — Ontology v0.1

Generated March 2026 · For AI agent use and cross-session communication