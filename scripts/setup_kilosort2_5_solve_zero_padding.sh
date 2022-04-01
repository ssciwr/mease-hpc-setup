set -e -x

cd $1

source init.sh

# download a fork of kilosort 2.5 with a fix for batches with no spikes
# see https://github.com/MouseLand/Kilosort/pull/288
git clone -b solve_zero_padding git@github.com:RobertoDF/Kilosort.git Kilosort-2.5_solve_zero_padding

# compile kilosort 2.5 GPU matlab code
cd Kilosort-2.5_solve_zero_padding/CUDA
matlab -nodesktop -nosplash -r "mexGPUall;quit"
