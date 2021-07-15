cd $1

# make matlab available
module load math/matlab/R2021a

# download kilosort 2
wget https://github.com/MouseLand/Kilosort/archive/refs/tags/v2.0.tar.gz
tar xf v2.0.tar.gz
rm v2.0.tar.gz

# compile kilosort 2 GPU matlab code
cd Kilosort-2.0/CUDA
matlab -nodesktop -nosplash -r "mexGPUall;quit"
