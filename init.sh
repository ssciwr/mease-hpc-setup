# script to be sourced by users
ROOTDIR=$(ws_find measelab)

# make matlab available
module load math/matlab/R2021a

# tell spikeinterface where sorters are installed
export KILOSORT2_5_PATH=$ROOTDIR/Kilosort-2.5

# add conda to path
source miniconda3/etc/profile.d/conda.sh

# activate measelab conda env
conda activate measelab