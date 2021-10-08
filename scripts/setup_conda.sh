set -e -x

cd $1

# download miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

# install
bash miniconda.sh -b -p $(pwd)/miniconda3

# add conda to PATH
source miniconda3/etc/profile.d/conda.sh

# update conda
conda update -n base conda -y

rm miniconda.sh
