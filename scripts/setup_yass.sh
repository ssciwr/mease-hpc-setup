cd $1

# make cuda available
module load devel/cuda/11.2

# init conda
source miniconda3/etc/profile.d/conda.sh

# activate env
conda activate measelab

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# download YASS (no release yet: using git master)
git clone https://github.com/paninski-lab/yass

# install it & dependencies
cd yass
pip install .

# install pytorch
conda install pytorch

# compile CUDA code
cd src/gpu_bspline_interp
python setup.py install --force
cd ..
cd gpu_rowshift
python setup.py install --force
cd ../..

# re-install yass
pip install .