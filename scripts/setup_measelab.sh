cd $1

# init conda
source miniconda3/etc/profile.d/conda.sh

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# clone mease-lab-to-nwb
git clone https://github.com/lkeegan/mease-lab-to-nwb.git
cd mease-lab-to-nwb

#git checkout expand_env_deps # skip this as pytorch install currently hangs on hpc

# create conda env
conda env create -f mease-env.yml

# activate env
conda activate measelab

# install mease-lab-to-nwb
python setup.py develop