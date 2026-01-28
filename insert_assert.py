#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
import sys
from typing import Any, Dict

PRINT_RE = re.compile(
    r"""^(?P<indent>\s*)print\(\s*f(?P<q>["'])
        (?P<label>Result:|Target\s+result:)\s*
        \{(?P<expr>[^}]+)\}\s*
        (?P=q)\s*\)\s*$
    """,
    re.VERBOSE,
)

def _line_ending(s: str) -> str | None:
    # 保留原始行尾风格
    if s.endswith("\r\n"):
        return "\r\n"
    if s.endswith("\n"):
        return "\n"
    return None

def insert_asserts_in_code(code: str) -> str:
    lines = code.splitlines(True)  # True: 保留原始换行符
    out: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        raw = line.rstrip("\r\n")  # 用于正则匹配，不带行尾换行
        m = PRINT_RE.match(raw)

        if m:
            indent = m.group("indent")
            expr = m.group("expr").strip()

            # 1) 先把 print 行写回去；如果它没有换行符，补一个换行
            eol = _line_ending(line) or "\n"
            out.append(raw + eol)

            # 2) 如果下一行已经是 assert，就不重复插入
            if i + 1 < len(lines) and lines[i + 1].lstrip().startswith("assert("):
                i += 1
                continue

            # 3) 插入 assert 行：同缩进 + 同行尾风格
            out.append(f"{indent}assert({expr} == ??){eol}")

        else:
            out.append(line)

        i += 1

    return "".join(out)

def get_code_field(obj: Dict[str, Any]) -> str:
    if isinstance(obj.get("task"), dict) and isinstance(obj["task"].get("code"), str):
        return obj["task"]["code"]
    if isinstance(obj.get("code"), str):
        return obj["code"]
    return ""

def set_code_field(obj: Dict[str, Any], new_code: str) -> None:
    if isinstance(obj.get("task"), dict) and isinstance(obj["task"].get("code"), str):
        obj["task"]["code"] = new_code
    elif isinstance(obj.get("code"), str):
        obj["code"] = new_code

def main():
    if len(sys.argv) != 3:
        print("Usage: python add_asserts.py input.jsonl output.jsonl", file=sys.stderr)
        sys.exit(1)

    in_path, out_path = sys.argv[1], sys.argv[2]
    changed = 0
    inserted = 0

    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            obj = json.loads(line)
            code = get_code_field(obj)

            if code:
                new_code = insert_asserts_in_code(code)
                if new_code != code:
                    changed += 1
                    inserted += new_code.count("assert(") - code.count("assert(")
                set_code_field(obj, new_code)

            fout.write(json.dumps(obj, ensure_ascii=False) + "\n")

    print(f"Done. changed_records={changed}, inserted_asserts={inserted}")

if __name__ == "__main__":
    main()
