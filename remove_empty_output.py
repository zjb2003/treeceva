import json

# 输入和输出文件路径
input_file = r'result\Qwen3-235B-A22B-Thinking-2507_thought.jsonl'
output_file = r'result\Qwen3-235B-A22B-Thinking-2507_thought_cleaned.jsonl'

# 读取文件，删除 raw_output 为空的数据，写入新文件
deleted_count = 0
kept_count = 0

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        if line.strip():  # 跳过空行
            data = json.loads(line)
            # 检查 raw_output 是否为空
            raw_output = data.get('raw_output', '')
            if raw_output and raw_output.strip():  # 如果 raw_output 不为空
                outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
                kept_count += 1
            else:
                deleted_count += 1

print(f"✓ 完成！")
print(f"✓ 删除了 {deleted_count} 条 raw_output 为空的数据")
print(f"✓ 保留了 {kept_count} 条数据")
print(f"✓ 结果已保存到 {output_file}")
