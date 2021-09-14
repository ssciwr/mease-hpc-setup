set -e -x

cd $1

source init.sh

# download kilosort 2.5
wget https://github.com/MouseLand/Kilosort/archive/refs/tags/v2.5.tar.gz
tar xf v2.5.tar.gz
rm v2.5.tar.gz

# compile kilosort 2.5 GPU matlab code
cd Kilosort-2.5/CUDA
matlab -nodesktop -nosplash -r "mexGPUall;quit"
