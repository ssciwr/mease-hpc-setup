#!/bin/bash

#SBATCH --partition=gpu-single
#SBATCH --nodes=1
#SBATCH --gres=gpu:any
#SBATCH --cpus-per-gpu=12
#SBATCH --ntasks-per-node=12
#SBATCH --time=48:00:00
#SBATCH --mem=60gb

# display node name and GPU info

hostname

nvidia-smi

python sort_smrx.py
