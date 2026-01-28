# eval_runner.py

import argparse
import datetime as dt
from pathlib import Path

from prompt import SYSTEM_PROMPT, build_user_prompt
from dataset import (
    iter_jsonl,
    extract_original_assert,
    parse_assert_answer,
    load_existing_ids,
)
from tqdm import tqdm
import json
from backend import Backend, LocalBackend, APIBackend
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)



def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("--backend", choices=["local", "api"], required=True)
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)

    ap.add_argument("--batch_size", type=int, default=1)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--top_p", type=float, default=1.0)
    ap.add_argument("--max_new_tokens", type=int, default=128)
    ap.add_argument("--resume", action="store_true")

    # local
    ap.add_argument("--local_model_path")
    ap.add_argument("--tensor_parallel_size", type=int, default=1)
    ap.add_argument("--dtype", default="auto")
    ap.add_argument("--trust_remote_code", action="store_true")

    # api
    ap.add_argument("--api_base_url")
    ap.add_argument("--api_model")
    ap.add_argument("--api_key")

    args = ap.parse_args()
    
    logger.info("Eval started")
    logger.info("Backend: %s", args.backend)
    logger.info("Batch size: %d", args.batch_size)

    if args.backend == "local":
        backend = LocalBackend(
            model_path=args.local_model_path,
            dtype=args.dtype,
            trust_remote_code=args.trust_remote_code,
            tensor_parallel_size=args.tensor_parallel_size,
        )
    else:
        backend = APIBackend(
            base_url=args.api_base_url,
            model=args.api_model,
            api_key=args.api_key,
        )


    gen_kwargs = dict(
        temperature=args.temperature,
        top_p=args.top_p,
        max_new_tokens=args.max_new_tokens,
    )

    input_path = Path(args.input)
    output_path = Path(args.output)
    existing = load_existing_ids(output_path) if args.resume else set()

    batch_samples, batch_prompts = [], []

    def flush():
        raws = backend.generate_batch(batch_prompts, **gen_kwargs)
        with output_path.open("a", encoding="utf-8") as f:
            for sample, raw in tqdm(zip(batch_samples, raws)):
                code = sample["task"]["code"]
                gold = sample["task"].get("answer")
                orig = extract_original_assert(code)
                pred, err = parse_assert_answer(raw, orig)

                ok = pred is not None and gold is not None and abs(pred - gold) <= 1e-6
                logger.info("Flushing batch | size=%d", len(batch_samples))

                record = {
                    "id": sample["id"],
                    "predicted_answer": pred,
                    "gold_answer": gold,
                    "correct": ok,
                    "error": err,
                    "raw_output": raw,
                }

                f.write(json.dumps(record, ensure_ascii=False) + "\n")

    for sample in iter_jsonl(input_path):
        if args.resume and sample["id"] in existing:
            continue

        prompt = SYSTEM_PROMPT + "\n\n" + build_user_prompt(sample["task"]["code"])
        batch_samples.append(sample)
        batch_prompts.append(prompt)

        if len(batch_samples) >= args.batch_size:
            flush()
            batch_samples.clear()
            batch_prompts.clear()

    if batch_samples:
        flush()

if __name__ == "__main__":
    main()
