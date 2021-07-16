cd $1

# init conda
source miniconda3/etc/profile.d/conda.sh

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# clone mease-lab-to-nwb
git clone https://github.com/lkeegan/mease-lab-to-nwb.git
cd mease-lab-to-nwb

# create conda env
conda env create -f mease-env.yml

# activate env
conda activate measelab

# install pytorch
# note: generally we should first do all conda install steps, then do pip installs
# (https://www.anaconda.com/blog/using-pip-in-a-conda-environment)
# so this should go into mease-env.yml:
conda install -y pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch-lts

# install mease-lab-to-nwb
python setup.py develop