### 2026-03-XX: Schema v1.4.1 部署與資料字典確立
- **工具更新**：QuickForm 升級至 v1.4.1，實作三色 Tag Cloud、非阻斷式 Alert 邏輯與防覆寫 Sequence。
- **文件更新**：產出 `SDIndex_Data_Dictionary_v1.4.1.md`，取代原有的 v1.3 填寫指南。
- **核心變更**：
  1. 確立 18 個 free_keywords 的客觀物理觸發條件（Null Protocol 啟用）。
  2. 導入 Graph-RAG 關聯標記（temporal_variant_of, counterpoint_of, sensory_mirror_of）。
  3. 新增 `ve_valence` (-1 to +1) 效價評估。
