#!/usr/bin/env python3
"""
将 entries/ 下的 .md 文件转为 dist/humans.json
格式：每条由正文 + --author 组成
"""

import json
import re
import os
from pathlib import Path

ENTRIES_DIR = Path(__file__).parent.parent / "entries"
OUTPUT_FILE = Path(__file__).parent.parent / "dist" / "humans.json"


def parse_md(filepath: Path) -> list[dict]:
    category = filepath.stem
    text = filepath.read_text(encoding="utf-8")

    # 跳过标题行
    lines = text.strip().split("\n")
    entries = []
    current_text = []

    for line in lines:
        line = line.strip()

        # 跳过空行和 markdown 标题
        if not line or line.startswith("#"):
            continue

        # 匹配 --author 行
        if line.startswith("--"):
            author = line[2:].strip()
            if current_text:
                entries.append({
                    "text": "\n".join(current_text),
                    "author": author,
                    "category": category
                })
                current_text = []
        else:
            current_text.append(line)

    # 如果最后一条没有 author（容错）
    if current_text:
        entries.append({
            "text": "\n".join(current_text),
            "author": "anonymous",
            "category": category
        })

    return entries


def main():
    all_entries = []

    for md_file in sorted(ENTRIES_DIR.glob("*.md")):
        entries = parse_md(md_file)
        all_entries.extend(entries)
        print(f"  {md_file.name}: {len(entries)} entries")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(all_entries, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"\n✅ {len(all_entries)} entries -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
