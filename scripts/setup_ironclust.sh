cd $1

source init.sh

# download ironclust (no release yet: using git master)
git clone https://github.com/flatironinstitute/ironclust

# NOTE: ironclust GPU matlab code compiled in compile_gpu.sh
# NOTE: this needs to run on a node with the GPU!