cd $1

# make matlab available
module load math/matlab/R2021a

# download kilosort
wget https://github.com/MouseLand/Kilosort/archive/refs/tags/1.0.tar.gz
tar xf 1.0.tar.gz
rm 1.0.tar.gz

# compile kilosort 2 GPU matlab code
cd Kilosort-1.0/CUDA
matlab -nodesktop -nosplash -r "mexGPUall;quit"
