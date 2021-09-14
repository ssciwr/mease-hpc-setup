set -e -x

cd $1

source init.sh

pip install Cython h5py tqdm

pip install click klusta klustakwik2
