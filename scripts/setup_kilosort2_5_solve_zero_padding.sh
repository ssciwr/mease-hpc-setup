set -e -x

cd $1

source init.sh

# download a fork of kilosort 2.5 with a fix for batches with no spikes
# see https://github.com/MouseLand/Kilosort/pull/288
git clone -b solve_zero_padding git@github.com:RobertoDF/Kilosort.git Kilosort-2.5_solve_zero_padding

# compile kilosort 2.5 GPU matlab code
cd Kilosort-2.5_solve_zero_padding/CUDA
matlab -nodesktop -nosplash -r "mexGPUall;quit"

# also need to patch spikeinterface, since it generates a kilosort_main.m:
# https://github.com/SpikeInterface/spikeinterface/blob/master/spikeinterface/sorters/kilosort2_5/kilosort2_5_master.m
# and this file is modified in the solve_zero_padding fork
# patch checks if extra functions in fork exist, and if so it calls them
patch --verbose miniconda3/envs/measelab/lib/python3.8/site-packages/spikeinterface/sorters/kilosort2_5/kilosort2_5_master.m patch_si_for_ks25_fork.diff
