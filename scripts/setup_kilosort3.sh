cd $1

# make matlab available
module load math/matlab/R2021a

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# download kilosort 3 (no release yet: using git master)
git clone https://github.com/MouseLand/Kilosort.git

# compile kilosort 3 GPU matlab code
cd Kilosort/CUDA
matlab -nodesktop -nosplash -r "mexGPUall;quit"
