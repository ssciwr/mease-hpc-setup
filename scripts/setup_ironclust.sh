cd $1

# make matlab available
module load math/matlab/R2021a

# make cuda available
module load devel/cuda/11.2

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# download ironclust (no release yet: using git master)
git clone https://github.com/flatironinstitute/ironclust

# compile ironclust GPU matlab code

# NOTE: this needs to run on a node with the GPU!

# NOTE: Fails to autodetect the path to nvcc (and doesn't just try nvcc)
# need to set vcPath_nvcc in matlab/default.cfg
# For now have just hard-coded this BY HAND on the cluster:
# /gpfs/bwfor/lhome/software/common/devel/cuda/11.2.2/bin/nvcc

# have done the above & then ran the below by hand using RTX2080 node
# should check if this works on other nodes
# and at some point this should happen as part of the script

cd ironclust/matlab
matlab -nodesktop -nosplash -r "irc2 compile;quit"
