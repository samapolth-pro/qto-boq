"""Rebuild prices.js (bundled fallback for installed copies) from prices.json.
Usage: python3 tools/sync_prices.py   (run from the repo root after editing prices.json)
prices.json format: {"meta": {checkedAt, region, summary, next}, "prices": [{code, cat, name, unit, mat, matSrc, lab, labSrc, labPct?, note, asOf}, ...]}
"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
d = json.loads((root / "prices.json").read_text(encoding="utf-8"))
d["prices"] = sorted(d["prices"], key=lambda p: p["code"])
(root / "prices.json").write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
(root / "prices.js").write_text("window.QTO_PRICES=" + json.dumps(d, ensure_ascii=False) + ";", encoding="utf-8")
print(len(d["prices"]), "prices, checkedAt", d["meta"].get("checkedAt"))
