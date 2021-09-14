set -e -x

cd $1

source init.sh

# download kilosort 3 (no release yet: using git master)
git clone https://github.com/MouseLand/Kilosort.git

# compile kilosort 3 GPU matlab code
cd Kilosort/CUDA
matlab -nodesktop -nosplash -r "mexGPUall;quit"
