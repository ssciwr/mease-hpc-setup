cd $1

# init conda
source miniconda3/etc/profile.d/conda.sh

# activate env
conda activate measelab

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# download Combinato (no release yet: using git master)
git clone https://github.com/jniediek/combinato

cd combinato
python setup_options.py
