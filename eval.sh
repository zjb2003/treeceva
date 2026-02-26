#!/bin/bash
#SBATCH -J python
#SBATCH -N 1
#SBATCH -p a01
#SBATCH -o ./logs/%j-stdout.log
#SBATCH -e ./logs/%j-stderr.log
#SBATCH --no-requeue
#SBATCH --ntasks-per-node=8 #单节点CPU数
#SBATCH --gres=gpu:1 #单节点卡数
 
export NCCL_IB_HCA=mlx5_0,mlx5_1,mlx5_2,mlx5_3,mlx5_4,mlx5_6,mlx5_7,mlx5_8
export NCCL_BLOCKING_WAIT=1
export NCCL_ASYNC_ERROR_HANDLING=1
export TORCH_DISTRIBUTED_DEBUG=DETAIL
# mlx5_5为存储口，不连接GPU卡

source /apps/soft/anaconda3/bin/activate 
# conda env list
conda activate /home/fit/zhoum/WORK/miniconda3/envs/codesense
#conda环境选择

# DATASET=./data/cross_function_with_assert.jsonl
DATASET=./data/cross_function_2000_with_assert.jsonl

MODEL_PATH=/home/fit/zhoum/WORK/llms/models/base/Qwen3-Coder-30B-A3B-Instruct
MODEL=Qwen3-Coder-30B-A3B-Instruct_thought

MODEL_PATH=/home/fit/zhoum/WORK/llms/models/base/Qwen3-32B
MODEL=Qwen3-32B_thought

MODEL_PATH=/home/fit/zhoum/WORK/llms/models/Qwen/Qwen3-8B
MODEL=Qwen3-8B_thought

# MODEL_PATH=/home/fit/zhoum/WORK/llms/models/base/Qwen3-14B
# MODEL=Qwen3-14B_thought

MODEL_PATH=/home/fit/zhoum/WORK/llms/models/base/QwQ-32B
MODEL=QwQ-32B_thought

# batch size 决定“一次让模型算多少条输入”
# tensor_parallel_size 决定“一次让模型用多少张卡来算” 
python eval_runner.py \
  --backend local \
  --input $DATASET \
  --output ./result/$MODEL.jsonl \
  --local_model_path $MODEL_PATH \
  --temperature 0 \
  --resume \
  --max_length 4096 \
  --max_new_tokens 2048 \
  --batch_size 4 \
  --tensor_parallel_size 1 \
  --cot

python analyze_results.py  ./result/$MODEL.jsonl