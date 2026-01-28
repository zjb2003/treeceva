import os
import re
import json
import argparse
from pathlib import Path

INVALID_CHARS = r'<>:"/\\|?*\n\r\t'  # Windows forbidden + common control chars

def safe_filename(s: str, max_len: int = 180) -> str:
    """Make a string safe for filenames across OS."""
    if s is None:
        s = "None"
    s = str(s)

    # Replace whitespace with single underscore
    s = re.sub(r"\s+", "_", s.strip())

    # Replace invalid characters
    trans = {ord(ch): "_" for ch in INVALID_CHARS}
    s = s.translate(trans)

    # Extra cleanup (avoid weird trailing dots/spaces on Windows)
    s = s.strip(" .")

    # Limit length
    if len(s) > max_len:
        s = s[:max_len].rstrip(" ._")

    return s or "empty"

def answer_to_token(answer):
    """
    Convert answer field to a stable filename token.
    Handles int/float/str/list/dict/etc.
    """
    if answer is None:
        return "None"

    # If it's already a number
    if isinstance(answer, (int, float)):
        # Keep human-readable; avoid scientific notation if possible
        # For floats: strip trailing zeros
        if isinstance(answer, float):
            s = f"{answer:.10f}".rstrip("0").rstrip(".")
            return s if s else "0"
        return str(answer)

    # If it's a string that looks numeric, keep it
    if isinstance(answer, str):
        return answer.strip()

    # For complex types: json-dump compact, then sanitize
    try:
        return json.dumps(answer, ensure_ascii=False, separators=(",", ":"))
    except Exception:
        return str(answer)

def extract_code(item: dict):
    # Your sample format: item["task"]["code"]
    task = item.get("task") or {}
    return task.get("code")

def extract_answer(item: dict):
    task = item.get("task") or {}
    return task.get("answer")

def main():
    parser = argparse.ArgumentParser(description="Extract task.code into ./example as id_answer.py")
    parser.add_argument("--input", type=str, required=True, help="Path to jsonl dataset (e.g., cross_function.jsonl)")
    parser.add_argument("--outdir", type=str, default="./example", help="Output directory (default: ../example)")
    parser.add_argument("--encoding", type=str, default="utf-8", help="File encoding (default: utf-8)")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_dir = Path(args.outdir)
    out_dir.mkdir(parents=True, exist_ok=True)

    total = 0
    written = 0
    skipped = 0
    collisions = 0

    with in_path.open("r", encoding=args.encoding) as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            total += 1
            try:
                item = json.loads(line)
            except Exception as e:
                print(f"[WARN] line {line_no}: JSON parse failed: {e}")
                skipped += 1
                continue

            _id = item.get("id")
            if not _id:
                print(f"[WARN] line {line_no}: missing 'id' field, skipped")
                skipped += 1
                continue

            code = extract_code(item)
            if not code or not isinstance(code, str) or not code.strip():
                print(f"[WARN] line {line_no} id={_id}: missing/empty code, skipped")
                skipped += 1
                continue

            ans = extract_answer(item)
            ans_token = answer_to_token(ans)

            fname = f"{safe_filename(_id)}_{safe_filename(ans_token)}.py"
            out_path = out_dir / fname

            # Handle collisions
            if out_path.exists():
                collisions += 1
                stem = out_path.stem
                suffix = out_path.suffix
                k = 2
                while True:
                    candidate = out_dir / f"{stem}_v{k}{suffix}"
                    if not candidate.exists():
                        out_path = candidate
                        break
                    k += 1

            out_path.write_text(code.rstrip() + "\n", encoding="utf-8")
            written += 1

    print("==== Done ====")
    print(f"Input:   {in_path}")
    print(f"Outdir:  {out_dir.resolve()}")
    print(f"Total lines parsed as items: {total}")
    print(f"Written .py files:          {written}")
    print(f"Skipped:                    {skipped}")
    print(f"Filename collisions:        {collisions}")

if __name__ == "__main__":
    main()
