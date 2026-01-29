# MODEL=DeepSeek-V3.2
MODEL=Qwen3-32B
MODEL=QwQ-32B
MODEL=Qwen2.5-72B-Instruct
MODEL=Qwen3-Next-80B-A3B-Instruct
# MODEL=Qwen3-Next-80B-A3B-Thinking
MODEL=Qwen3-235B-A22B-Thinking-2507
# MODEL=Qwen3-235B-A22B-Instruct-2507
# MODEL=Qwen3-Coder-480B-A35B-Instruct
API_BASE_URL=https://llmapi.paratera.com/v1/
OUTPUT_FILE=./result/${MODEL}_thought.jsonl
API_KEY=sk-k6SW1N0DmFPvkVdk_viyCA


# MODEL=claude-sonnet-4-5-20250929
# API_BASE_URL=https://api.ezai88.com/v1
# OUTPUT_FILE=./result/${MODEL}_thought.jsonl
# API_KEY=sk-gq8qRNNiNIjS0x8tzfMl8F9bscL4wopT7oA2qD2FU8xKTrnp


python ./eval_runner.py \
    --backend api \
    --input ./data/cross_function_with_assert.jsonl \
    --output $OUTPUT_FILE \
    --api_base_url $API_BASE_URL \
    --api_model $MODEL \
    --temperature 0 \
    --max_new_tokens 2048 \
    --resume \
    --batch_size 4 \
    --api_key $API_KEY

python analyze_results.py $OUTPUT_FILE > ./result/${MODEL}_analysis.log 2>&1