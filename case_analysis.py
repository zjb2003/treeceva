import json
import argparse
import os

# python case_analysis.py ./result/Qwen2.5-7B-Instruct.jsonl ./data/cross_function_with_assert.jsonl --id id-00006

def load_dataset_code(dataset_file):
    """
    加载原始数据集，构建 ID 到 Code 的映射字典
    """
    id_to_code = {}
    print(f"正在加载数据集: {dataset_file} ...")
    try:
        with open(dataset_file, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                item = json.loads(line)
                # 结构: item -> "task" -> "code"
                if 'id' in item and 'task' in item and 'code' in item['task']:
                    id_to_code[item['id']] = item['task']['code']
        print(f"数据集加载完成，共包含 {len(id_to_code)} 条数据。")
        return id_to_code
    except Exception as e:
        print(f"读取数据集出错: {e}")
        return {}

def analyze_results(result_file, id_to_code, target_id=None):
    """
    读取结果文件，匹配代码并输出
    """
    print(f"\n正在分析结果: {result_file} ...")
    if target_id:
        print(f"正在筛选特定 ID: {target_id}")
    print("=" * 60)
    
    found_count = 0
    
    try:
        with open(result_file, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                res = json.loads(line)
                
                res_id = res.get('id', 'Unknown ID')
                
                # 核心修改：如果指定了 target_id 且当前 ID 不匹配，则跳过
                if target_id and res_id != target_id:
                    continue
                
                found_count += 1
                
                # 1. 提取基础信息
                predicted = res.get('predicted_answer')
                gold = res.get('gold_answer')
                raw_text = res.get('raw_text')
                is_correct = res.get('correct')
                
                # 2. 从映射中查找对应的原始代码
                code = id_to_code.get(res_id, "【警告：未在原始数据集中找到对应 ID 的代码】")
                
                # 3. 格式化输出 (保持原格式不变)
                print(f"ID: {res_id} | 状态: {'✅ 正确' if is_correct else '❌ 错误'}")
                print("-" * 60)
                
                print("[原始代码 (Code)]:")
                print(code.strip())
                print("-" * 60)
                
                print(f"[真实答案 (Gold)]: {gold}")
                print(f"[预测答案 (Pred)]: {predicted}")
                print("-" * 60)
                
                print("[模型完整输出 (Raw Output)]:")
                print(raw_text.strip() if raw_text else "None")
                
                print("=" * 60 + "\n")
        
        # 如果指定了ID但没找到，给出提示
        if target_id and found_count == 0:
            print(f"提示：在结果文件中未找到 ID 为 '{target_id}' 的记录。")
            
    except Exception as e:
        print(f"读取结果文件出错: {e}")

def main():
    parser = argparse.ArgumentParser(description="合并评估结果与原始代码进行分析")
    parser.add_argument('result_file', help="你的结果文件路径 (例如: results.jsonl)")
    parser.add_argument('dataset_file', help="原始数据集文件路径 (例如: dataset.jsonl)")
    
    # 新增的可选参数
    parser.add_argument('--id', help="指定要查看的特定 ID (例如: id-00006)", default=None)
    
    args = parser.parse_args()
    
    if not os.path.exists(args.result_file) or not os.path.exists(args.dataset_file):
        print("错误：文件不存在，请检查路径。")
        return

    # 1. 加载数据集构建索引
    code_map = load_dataset_code(args.dataset_file)
    
    # 2. 遍历结果并输出
    analyze_results(args.result_file, code_map, target_id=args.id)

if __name__ == "__main__":
    main()