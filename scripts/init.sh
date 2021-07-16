# script to be sourced by users

# make matlab available & set version
module load math/matlab/R2021a

# make cuda available & set version
module load devel/cuda/10.2

# make gcc available & set version
# note matlab 2021a cuda compilation requires gcc <= 9
module load compiler/gnu/9.1

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# tell spikeinterface where sorters are installed
export KILOSORT_PATH=/gpfs/bwfor/work/ws/hd_uk239-measelab/Kilosort-1.0
export KILOSORT2_PATH=/gpfs/bwfor/work/ws/hd_uk239-measelab/Kilosort-2.0
export KILOSORT2_5_PATH=/gpfs/bwfor/work/ws/hd_uk239-measelab/Kilosort-2.5
export KILOSORT3_PATH=/gpfs/bwfor/work/ws/hd_uk239-measelab/Kilosort
export HDSORT_PATH=/gpfs/bwfor/work/ws/hd_uk239-measelab/HDsort
export IRONCLUST_PATH=/gpfs/bwfor/work/ws/hd_uk239-measelab/ironclust
export WAVECLUS_PATH=/gpfs/bwfor/work/ws/hd_uk239-measelab/wave_clus
export COMBINATO_PATH=/gpfs/bwfor/work/ws/hd_uk239-measelab/combinato

# add conda to path
source /gpfs/bwfor/work/ws/hd_uk239-measelab/miniconda3/etc/profile.d/conda.sh

# activate measelab conda env
conda activate measelab
