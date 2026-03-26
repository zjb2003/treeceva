#!/usr/bin/env python3
"""
分析 TreecEva 评估结果，直接输出分析报告
"""

import json
import argparse
import statistics
from collections import defaultdict, Counter
from typing import Dict, Any, List
from dataset import parse_assert_answer, extract_original_assert
from pathlib import Path



class TreecEvaAnalyzer:
    """TreecEva 评估结果分析器"""
    def __init__(self, result_file: str, dataset_file: str):
        self.result_file = result_file
        self.dataset_file = dataset_file

        self.results = []
        self.dataset_code_map = {}  # id -> code

        self.load_results()
        if dataset_file:
            self.load_dataset()

    
    def load_results(self):
        """加载结果文件，若文件不存在则自动创建"""
        path = Path(self.result_file)

        if not path.exists():
            print(f"结果文件不存在，自动创建: {path}")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()

        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():  # 跳过空行
                        self.results.append(json.loads(line.strip()))
            print(f"成功加载 {len(self.results)} 条结果")
            print("-" * 30)
        except Exception as e:
            print(f"加载结果文件失败: {e}")
            self.results = []
    
    def load_dataset(self):
        path = Path(self.dataset_file)
        if not path.exists():
            raise FileNotFoundError(f"Dataset file not found: {path}")

        if path.suffix == ".json":
            data = json.loads(path.read_text(encoding="utf-8"))
            for item in data:
                _id = item.get("id")
                code = item.get("task", {}).get("code")
                if _id and code:
                    self.dataset_code_map[_id] = code
        else:  # jsonl
            with path.open("r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    item = json.loads(line)
                    _id = item.get("id")
                    code = item.get("task", {}).get("code")
                    if _id and code:
                        self.dataset_code_map[_id] = code

        print(f"加载原始数据集 {len(self.dataset_code_map)} 条")
        print("-" * 30)

    def calculate_basic_metrics(self) -> Dict[str, Any]:
        """计算基本指标"""
        total = len(self.results)
        if total == 0:
            return {'total_samples': 0, 'correct_count': 0, 'accuracy': 0, 'error_rate': 0}

        correct = sum(1 for r in self.results if r.get('correct', False))
        accuracy = correct / total
        
        # 统计错误类型
        error_counts = Counter()
        for r in self.results:
            error = r.get('error')
            if error:
                error_counts[error] += 1
        
        # 统计有效预测数量
        valid_predictions = sum(1 for r in self.results if r.get('predicted_answer') is not None)
        valid_accuracy = correct / valid_predictions if valid_predictions > 0 else 0
        
        return {
            'total_samples': total,
            'correct_count': correct,
            'accuracy': accuracy,
            'valid_predictions': valid_predictions,
            'valid_accuracy': valid_accuracy,
            'error_counts': dict(error_counts),
            'error_rate': (total - valid_predictions) / total
        }
    
    def analyze_answer_types(self) -> Dict[str, Any]:
        """分析答案类型分布"""
        answer_types = defaultdict(int)
        gold_types = defaultdict(int)
        
        for r in self.results:
            pred = r.get('predicted_answer')
            gold = r.get('gold_answer')
            
            # 分类预测答案类型
            if pred is not None:
                if isinstance(pred, int) or (isinstance(pred, float) and pred.is_integer()):
                    answer_types['integer'] += 1
                elif isinstance(pred, float):
                    answer_types['float'] += 1
                else:
                    answer_types['other'] += 1
            
            # 分类标准答案类型
            if isinstance(gold, int):
                gold_types['integer'] += 1
            elif isinstance(gold, float):
                gold_types['float'] += 1
            else:
                gold_types['other'] += 1
        
        return {
            'predicted_answer_types': dict(answer_types),
            'gold_answer_types': dict(gold_types)
        }
    
    def calculate_numerical_accuracy(self, tolerance: float = 1e-6) -> Dict[str, Any]:
        """计算数值准确率（考虑浮点数比较）"""
        exact_matches = 0
        approximate_matches = 0
        total_valid = 0
        
        differences = []
        
        for r in self.results:
            pred = r.get('predicted_answer')
            gold = r.get('gold_answer')
            
            if pred is not None and gold is not None:
                total_valid += 1
                try:
                    diff = abs(float(pred) - float(gold))
                    differences.append(diff)
                    
                    if diff < tolerance:
                        exact_matches += 1
                    elif diff < 0.1:  # 允许0.1的误差
                        approximate_matches += 1
                except (TypeError, ValueError):
                    pass
        
        # 使用 statistics 替代 numpy 以减少依赖
        mean_diff = statistics.mean(differences) if differences else 0
        median_diff = statistics.median(differences) if differences else 0
        max_diff = max(differences) if differences else 0

        return {
            'exact_matches': exact_matches,
            'approximate_matches': approximate_matches,
            'total_valid': total_valid,
            'exact_accuracy': exact_matches / total_valid if total_valid > 0 else 0,
            'approximate_accuracy': (exact_matches + approximate_matches) / total_valid if total_valid > 0 else 0,
            'mean_difference': mean_diff,
            'median_difference': median_diff,
            'max_difference': max_diff,
            'differences': differences
        }
    
    def analyze_error_patterns(self) -> Dict[str, Any]:
        """分析错误模式"""
        error_patterns = defaultdict(list)
        
        for r in self.results:
            if not r.get('correct', False):
                error_type = r.get('error', 'wrong_answer')
                pred = r.get('predicted_answer')
                gold = r.get('gold_answer')
                
                error_patterns[error_type].append({
                    'id': r.get('id'),
                    'predicted': pred,
                    'gold': gold,
                    # 截断过长的文本以便显示
                    'raw_text': (r.get('raw_text', '')[:50] + '...') if r.get('raw_text') else ''
                })
        
        return {
            'error_patterns': {k: len(v) for k, v in error_patterns.items()},
            'error_examples': {k: v[:3] for k, v in error_patterns.items()}  # 每种错误类型的前3个例子
        }
    
    def generate_report(self) -> str:
        """生成分析报告"""
        if not self.results:
            return "无数据可分析。"

        basic_metrics = self.calculate_basic_metrics()
        answer_types = self.analyze_answer_types()
        numerical_accuracy = self.calculate_numerical_accuracy()
        error_patterns = self.analyze_error_patterns()
        
        report = f"""
=== TreecEva 评估结果分析报告 ===

[基本指标]
- 总样本数: {basic_metrics['total_samples']}
- 正确数量: {basic_metrics['correct_count']}
- 准确率:   {basic_metrics['accuracy']:.2%}
- 有效预测数: {basic_metrics['valid_predictions']}
- 有效准确率: {basic_metrics['valid_accuracy']:.2%}
- 错误率:   {basic_metrics['error_rate']:.2%}

[数值准确率] (浮点数比较)
- 精确匹配数: {numerical_accuracy['exact_matches']}
- 近似匹配数: {numerical_accuracy['approximate_matches']}
- 精确准确率: {numerical_accuracy['exact_accuracy']:.2%}
- 近似准确率: {numerical_accuracy['approximate_accuracy']:.2%}
- 平均差异:   {numerical_accuracy['mean_difference']:.4f}
- 中位数差异: {numerical_accuracy['median_difference']:.4f}
- 最大差异:   {numerical_accuracy['max_difference']:.4f}

[答案类型分布]
预测答案类型:
"""
        for atype, count in answer_types['predicted_answer_types'].items():
            report += f"  - {atype}: {count}\n"
        
        report += "标准答案类型:\n"
        for atype, count in answer_types['gold_answer_types'].items():
            report += f"  - {atype}: {count}\n"
        
        report += "\n[错误分析]\n"
        for error_type, count in error_patterns['error_patterns'].items():
            report += f"  - {error_type}: {count}\n"
        
        if basic_metrics['error_counts']:
            report += "\n详细错误统计:\n"
            for error_type, count in basic_metrics['error_counts'].items():
                report += f"  - {error_type}: {count}\n"

        return report
    
    def reanalyze_and_update_file(self):
        updated_results = []
        changed_count = 0
        if self.dataset_file is None:
            print("未提供 dataset_file，无法重新分析。")
            return

        for r in self.results:
            sample_id = r.get("id")
            raw_text = r.get("raw_output", "")
            gold = r.get("gold_answer")

            # ✅ 从原始数据集中取 code
            code = self.dataset_code_map.get(sample_id)
            if not code:
                r["predicted_answer"] = None
                r["correct"] = False
                r["error"] = "missing_dataset_code"
                updated_results.append(r)
                continue

            # ✅ 从 code 中提取 original_assert
            original_assert = extract_original_assert(code)
            if not original_assert:
                r["predicted_answer"] = None
                r["correct"] = False
                r["error"] = "original_assert_not_found"
                updated_results.append(r)
                continue

            # 1. 解析答案
            pred, error = parse_assert_answer(raw_text, original_assert)

            # 2. 判题
            if pred is None or gold is None:
                correct = False
            else:
                try:
                    correct = float(pred) == float(gold)
                except Exception:
                    correct = False

            # 3. 统计变更
            if (
                r.get("predicted_answer") != pred
                or r.get("correct") != correct
                or r.get("error") != error
            ):
                changed_count += 1

            # 4. 更新
            r["predicted_answer"] = pred
            r["correct"] = correct
            r["error"] = error

            updated_results.append(r)

        # ✅ 覆盖写回文件
        with open(self.result_file, "w", encoding="utf-8") as f:
            for r in updated_results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        self.results = updated_results

        print(f"重新分析完成，更新 {changed_count} 条")
        print("-" * 30)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("result_file")
    parser.add_argument("--dataset_file", default=None)
    parser.add_argument("--reanalyze", action="store_true")

    args = parser.parse_args()

    analyzer = TreecEvaAnalyzer(
        args.result_file,
        args.dataset_file
    )

    if args.reanalyze:
        analyzer.reanalyze_and_update_file()

    print(analyzer.generate_report())



if __name__ == "__main__":
    main()