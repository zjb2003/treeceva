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
        # match = ASSERT_LINE_RE.search(s)
        matches = list(ASSERT_LINE_RE.finditer(s))
        if matches:
            match = matches[-1]  # Use the last match found
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


raw_text="Let's trace through the code step by step:\n\n1. raw_data = [3, 7, 12, 18, 25]\n2. processed = list(map(lambda x: (x ** 2) % 17, raw_data))\n   - For 3: (3 ** 2) % 17 = 9 % 17 = 9\n   - For 7: (7 ** 2) % 17 = 49 % 17 = 15\n   - For 12: (12 ** 2) % 17 = 144 % 17 = 16\n   - For 18: (18 ** 2) % 17 = 324 % 17 = 1\n   - For 25: (25 ** 2) % 17 = 625 % 17 = 1\n   - So processed = [9, 15, 16, 1, 1]\n\n3. temp_analysis = [x for x in processed if x > 5]\n   - Elements > 5 in processed: [9, 15, 16]\n   - So temp_analysis = [9, 15, 16]\n\n4. avg_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0\n   - sum(temp_analysis) = 9 + 15 + 16 = 40\n   - len(temp_analysis) = 3\n   - avg_temp = 40 / 3 = 13.333...\n\n5. normalized = [round(x / avg_temp, 3) for x in temp_analysis] (not used)\n\n6. filtered = [x for x in processed if x % 3 == 2]\n   - Elements in processed where x % 3 == 2:\n     - 9 % 3 = 0 (not included)\n     - 15 % 3 = 0 (not included)\n     - 16 % 3 = 1 (not included)\n     - 1 % 3 = 1 (not included)\n     - 1 % 3 = 1 (not included)\n   - So filtered = []\n\n7. base_accum = 0\n   - Loop over filtered (empty list), so no iterations\n   - base_accum remains 0\n\n8. status_log = {}\n   - status_log['processed_count'] = len(processed) = 5\n   - status_log['filtered_count'] = len(filtered) = 0\n   - status_log['base_sum'] = base_accum = 0\n\n9. if len(filtered) % 2 == 0:\n   - len(filtered) = 0\n   - 0 % 2 = 0, so condition is true\n   - adjustment = 5\n\n10. pipeline_output = base_accum + status_log['filtered_count']\n    - base_accum = 0\n    - status_log['filtered_count'] = 0\n    - pipeline_output = 0 + 0 = 0\n\n11. final_score = calculate_final(pipeline_output)\n    - calculate_final(0)\n    - coef_gen(0): 0 > 20? No. 0 > 10? No. So coef_gen(0) = 1\n    - scaling_factor = 1\n    - return int(0 * 1) + adjustment = 0 + 5 = 5\n\n12. assert(final_score == ??)\n    - final_score = 5\n\n[/THOUGHT]\n[ANSWER]\nassert(final_score == 5)"
assert_line="assert (final_score == ??)"
result = parse_assert_answer(raw_text, assert_line)
# print(result)  # Expected output: (5.0, None)