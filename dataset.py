# dataset.py

import json
import re
from decimal import Decimal
from pathlib import Path
from typing import Dict, Iterable, Optional, Set, Tuple

ANSWER_BLOCK_RE = re.compile(r"\[ANSWER\](.*?)\[/ANSWER\]", re.DOTALL | re.IGNORECASE)
ASSERT_LINE_RE = re.compile(
    r"assert\s*\(\s*([^\)]+?)\s*==\s*([^\)]+?)\s*\)", re.IGNORECASE
)

def iter_jsonl(path: Path) -> Iterable[Dict]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

def extract_original_assert(code: str) -> Optional[str]:
    for line in code.splitlines():
        if "assert" in line and "??" in line:
            return line.strip()
    return None

def parse_assert_answer(
    raw_text: str,
    original_assert: str,
) -> Tuple[Optional[float], Optional[str]]:
    if not raw_text:
        return None, "empty_output"

    spaces = []
    m = ANSWER_BLOCK_RE.search(raw_text)
    if m:
        spaces.append(m.group(1))
    spaces.append(raw_text)

    match = None
    for s in spaces:
        match = ASSERT_LINE_RE.search(s)
        if match:
            break

    if not match:
        return None, "no_assert_found"

    lhs_model, rhs_model = match.group(1).strip(), match.group(2).strip()

    m_orig = ASSERT_LINE_RE.search(original_assert.replace("??", ""))
    if not m_orig:
        return None, "invalid_original_assert"

    if lhs_model != m_orig.group(1).strip():
        return None, "cheating_modified_lhs"

    try:
        val = Decimal(rhs_model)
        if not val.is_finite():
            return None, "non_finite_number"
        return float(val), None
    except Exception:
        return None, "rhs_not_numeric_literal"

def load_existing_ids(path: Path) -> Set[str]:
    if not path.exists():
        return set()
    ids = set()
    for obj in iter_jsonl(path):
        if isinstance(obj.get("id"), str):
            ids.add(obj["id"])
    return ids
