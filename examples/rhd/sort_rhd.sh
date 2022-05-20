#!/bin/bash

#SBATCH --partition=gpu-single
#SBATCH --nodes=1
#SBATCH --gres=gpu:RTX3090:1
#SBATCH --ntasks-per-node=12
#SBATCH --time=48:00:00
#SBATCH --mem=90gb

# display node name and GPU info

hostname

nvidia-smi

python sort_rhd.py
