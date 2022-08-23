# script to be sourced by users

# make matlab available & set version
module load math/matlab/R2022a

# make cuda available & set version
module load devel/cuda/11.6

# make gcc available & set version
# note matlab 2022a cuda compilation requires gcc <= 9
module load compiler/gnu/8.5

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# tell spikeinterface where sorters are installed
export KILOSORT_PATH=${MEASE_HPC_INSTALL}/Kilosort-1.0
export KILOSORT2_PATH=${MEASE_HPC_INSTALL}/Kilosort-2.0
export KILOSORT2_5_PATH=${MEASE_HPC_INSTALL}/Kilosort-2.5
export KILOSORT2_5_SOLVE_ZERO_PADDING_PATH=${MEASE_HPC_INSTALL}/Kilosort-2.5_solve_zero_padding
export KILOSORT3_PATH=${MEASE_HPC_INSTALL}/Kilosort
export HDSORT_PATH=${MEASE_HPC_INSTALL}/HDsort
export IRONCLUST_PATH=${MEASE_HPC_INSTALL}/ironclust
export WAVECLUS_PATH=${MEASE_HPC_INSTALL}/wave_clus
export COMBINATO_PATH=${MEASE_HPC_INSTALL}/combinato

# add conda to path
source ${MEASE_HPC_INSTALL}/miniconda3/etc/profile.d/conda.sh

# activate measelab conda env
conda activate measelab
