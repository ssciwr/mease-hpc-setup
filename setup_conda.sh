# go to measelab workspace
cd $(ws_find measelab)

# download miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

# install
bash miniconda.sh -b

# add conda to PATH
source miniconda3/etc/profile.d/conda.sh

# update conda
conda update -n base conda -y
