cd $1

# init conda
source miniconda3/etc/profile.d/conda.sh

# activate env
conda activate measelab

pip install Cython h5py tqdm

pip install click klusta klustakwik2
