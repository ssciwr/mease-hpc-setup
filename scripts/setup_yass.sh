cd $1

source init.sh

# download YASS (no release yet: using git master)
git clone https://github.com/paninski-lab/yass

# install it & dependencies
cd yass
pip install .

# install pytorch
conda install -y pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch-lts

# NOTE: yass GPU code compiled in compile_gpu.sh
# NOTE: this needs to run on a node with the GPU!