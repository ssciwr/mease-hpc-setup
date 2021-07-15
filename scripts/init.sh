# script to be sourced by users

# make matlab available
module load math/matlab/R2021a

# tell spikeinterface where sorters are installed
export KILOSORT2_PATH=/gpfs/bwfor/work/ws/hd_uk239-measelab/Kilosort-2.0
export KILOSORT2_5_PATH=/gpfs/bwfor/work/ws/hd_uk239-measelab/Kilosort-2.5

# add conda to path
source /gpfs/bwfor/work/ws/hd_uk239-measelab/miniconda3/etc/profile.d/conda.sh

# activate measelab conda env
conda activate measelab