#!/usr/bin/env python3
"""
json_to_md.py — SDIndex CKV Record Converter
Converts layer2_ckv.json → layer2_view.md for RAG retrieval

Usage:
  # Single record
  python json_to_md.py data/raw/KYT-20260330-A/layer2_ckv.json

  # Batch: all records under data/raw/
  python json_to_md.py --batch data/raw/

  # Batch: current directory tree
  python json_to_md.py --batch .

Output: layer2_view.md saved next to each layer2_ckv.json
"""

import json
import sys
import os
from pathlib import Path


def safe(d, *keys, default="—"):
    """Safely traverse nested dict."""
    for k in keys:
        if isinstance(d, dict):
            d = d.get(k, None)
        else:
            return default
        if d is None:
            return default
    return d if d != "" else default


def vs_bar(score, max_score=10):
    """Visual bar for Vs scores."""
    try:
        filled = round(float(score))
        return "█" * filled + "░" * (max_score - filled) + f"  {score}"
    except (TypeError, ValueError):
        return str(score)


def valence_arrow(val):
    """Direction arrow for ve_valence."""
    try:
        v = float(val)
        if v > 0.3:
            return f"↑ +{v} (擴張／提升)"
        elif v < -0.3:
            return f"↓ {v} (收縮／沉降)"
        else:
            return f"→ {v} (中性張力)"
    except (TypeError, ValueError):
        return str(val)


def convert(json_path: Path) -> Path:
    """Convert one layer2_ckv.json to layer2_view.md."""
    with open(json_path, "r", encoding="utf-8") as f:
        d = json.load(f)

    record_id     = safe(d, "record_id")
    schema_ver    = safe(d, "schema_version")
    generated_at  = safe(d, "generated_at")

    # Site
    site          = d.get("site", {})
    name_zh       = safe(site, "name_zh")
    name_en       = safe(site, "name_en")
    name_local    = safe(site, "name_local")
    city          = safe(site, "city")
    country       = safe(site, "country")
    site_type     = safe(site, "site_type")

    # Observation
    obs           = d.get("observation", {})
    obs_date      = safe(obs, "date")
    obs_time      = safe(obs, "time_of_day")
    weather       = safe(obs, "weather")
    duration      = safe(obs, "duration_minutes")
    crowd         = safe(obs, "crowd_density")
    visit_mode    = safe(obs, "visit_mode")
    preloaded     = safe(obs, "preloaded_knowledge", default=False)
    body_state    = safe(obs, "body_state")

    # Vs vector
    vs            = d.get("vs_vector", {})
    vt            = safe(vs, "vt")
    vl            = safe(vs, "vl")
    vr            = safe(vs, "vr")
    vg            = safe(vs, "vg")
    ve            = safe(vs, "ve_score")
    ve_val        = safe(vs, "ve_valence")

    # Subtypes
    sub           = d.get("vs_subtypes", {})
    vl_sub        = safe(sub, "vl_source")
    vr_sub        = safe(sub, "vr_source")
    ve_trigger    = safe(sub, "ve_trigger")

    # SDIndex
    sdi           = d.get("sdindex_computation", {})
    sdindex       = safe(sdi, "sdindex_score")
    formula       = safe(sdi, "formula_applied")
    weights       = sdi.get("weights", {})

    # Resilience (v1.4 split)
    res           = d.get("resilience", {})
    structural_r  = safe(res, "structural")
    atmospheric_r = safe(res, "atmospheric")

    # Phenomenology
    pheno         = safe(d, "phenomenology_mode")

    # Free keywords
    free_kw       = d.get("free_keywords", [])
    kw_str        = "  ·  ".join(free_kw) if free_kw else "—"

    # Relation tags
    rel_tags      = d.get("relation_tags", [])

    # Field notes
    fn            = d.get("field_notes", {})
    entry_state   = safe(fn, "entry_state")
    turning_point = safe(fn, "turning_point")
    key_insight   = safe(fn, "key_insight")
    exit_state    = safe(fn, "exit_state")

    # Emotion trajectory
    et            = d.get("emotion_trajectory", {})
    et_arc        = safe(et, "arc")
    et_peak       = safe(et, "peak_moment")
    et_valence    = safe(et, "overall_valence")

    # Asset class
    asset         = d.get("asset_class", {})
    asset_tier    = safe(asset, "tier")
    asset_note    = safe(asset, "note")

    # AI collaboration
    ai_collab     = safe(d, "ai_collaboration", default=False)

    # Weights string
    w_str = "  ".join([f"{k.upper()}×{v}" for k, v in weights.items()]) if weights else "—"

    # Relation tags block
    if rel_tags:
        rt_lines = "\n".join([
            f"- `{safe(r, 'type')}` → {safe(r, 'target_record_id')}  _{safe(r, 'note')}_"
            for r in rel_tags
        ])
    else:
        rt_lines = "_無_"

    md = f"""# {record_id}
> {name_zh}　{name_en}　{city}, {country}
> Schema {schema_ver}　·　Generated {generated_at}

---

## 場域識別

| 欄位 | 值 |
|------|-----|
| 地點（中）| {name_zh} |
| 地點（英）| {name_en} |
| 地點（本地）| {name_local} |
| 城市 | {city} |
| 國家 | {country} |
| 場域類型 | `{site_type}` |

---

## 採樣條件

| 欄位 | 值 |
|------|-----|
| 日期 | {obs_date} |
| 時段 | {obs_time} |
| 天氣 | {weather} |
| 停留時間 | {duration} 分鐘 |
| 人流密度 | {crowd} |
| 採樣模式 | {visit_mode} |
| 預載知識啟動 | {preloaded} |
| 身體狀態 | {body_state} |

---

## Vs 感知向量

| 維度 | 分數 | 視覺 |
|------|------|------|
| Vt 時間層次 | {vt} | {vs_bar(vt)} |
| Vl 光線質感 | {vl} | {vs_bar(vl)} |
| Vr 空間克制 | {vr} | {vs_bar(vr)} |
| Vg 幾何複雜 | {vg} | {vs_bar(vg)} |
| Ve 情感強度 | {ve} | {vs_bar(ve)} |

**Ve Valence（情感方向）：** {valence_arrow(ve_val)}

**Vl 來源：** `{vl_sub}`　**Vr 來源：** `{vr_sub}`　**Ve 觸發器：** `{ve_trigger}`

---

## SDIndex 計算

**SDIndex Score：{sdindex}**

公式：`{formula}`

權重：{w_str}

---

## Resilience（v1.4）

| 類型 | 分數 |
|------|------|
| 結構韌性 structural | {structural_r} |
| 氛圍韌性 atmospheric | {atmospheric_r} |

---

## 現象學模式

`{pheno}`

---

## 自由關鍵詞

{kw_str}

---

## 關聯標籤

{rt_lines}

---

## 田野筆記

**入場狀態**
{entry_state}

**轉折點**
{turning_point}

**核心洞見**
{key_insight}

**離場狀態**
{exit_state}

---

## 情感軌跡

| 欄位 | 值 |
|------|-----|
| 弧線 arc | {et_arc} |
| 峰值時刻 | {et_peak} |
| 整體 valence | {et_valence} |

---

## 資產等級

**Tier：** {asset_tier}
{asset_note}

---

## AI 協作

AI Collaboration Flag：{ai_collab}

---

_SDIndex Framework v{schema_ver}　·　CC-BY-4.0　·　Shihyen (Sabrina) Lin_
_Record ID：{record_id}_
"""

    out_path = json_path.parent / "layer2_view.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)

    return out_path


def batch(root: Path):
    """Find all layer2_ckv.json under root and convert them."""
    found = list(root.rglob("layer2_ckv.json"))
    if not found:
        print(f"No layer2_ckv.json found under {root}")
        return
    for p in sorted(found):
        try:
            out = convert(p)
            print(f"✓  {p}  →  {out}")
        except Exception as e:
            print(f"✗  {p}  ERROR: {e}")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    if args[0] == "--batch":
        root = Path(args[1]) if len(args) > 1 else Path(".")
        batch(root)
    else:
        p = Path(args[0])
        if not p.exists():
            print(f"File not found: {p}")
            sys.exit(1)
        out = convert(p)
        print(f"✓  {p}  →  {out}")


if __name__ == "__main__":
    main()
