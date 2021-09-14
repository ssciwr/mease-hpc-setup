# script to run GPU compilation part of installs that needs to see the GPU

set -e -x

cd $1

source init.sh

# ironclust

cd ironclust/matlab

# NOTE: Fails to autodetect the path to nvcc (and doesn't just try nvcc)
# so need to set vcPath_nvcc in matlab/user.cfg
NVCC_DIR=$(which nvcc)
echo "vcPath_nvcc = '${NVCC_DIR}'" > user.cfg
cat user.cfg

matlab -nodesktop -nosplash -r "irc2 compile;quit"

cd ../../

# YASS

cd yass/src/gpu_bspline_interp
python setup.py install --force
cd ..
cd gpu_rowshift
python setup.py install --force
cd ../..

# re-install yass
pip install .