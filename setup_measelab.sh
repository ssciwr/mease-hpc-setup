# go to measelab workspace
cd $(ws_find measelab)

#workaround git ssl isse
export GIT_SSL_NO_VERIFY=true

# clone mease-lab-to-nwb
git clone https://github.com/lkeegan/mease-lab-to-nwb.git
cd mease-lab-to-nwb

# create conda env
conda env create -f mease-env.yml

# activate env
source ~/miniconda3/etc/profile.d/conda.sh
conda activate measelab

# install
python setup.py develop
cd ..