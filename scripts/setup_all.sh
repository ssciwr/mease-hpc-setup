set -e -x

INSTALL=/gpfs/bwfor/work/ws/hd_uk239-measelab

# miniconda

bash setup_conda.sh $INSTALL

# mease-lab-to-nwb & measelab env

bash setup_measelab.sh $INSTALL

# init script for users (also used by the rest of the setup scripts below)

cp init.sh $INSTALL/init.sh

# helper script for starting jupyter server

bash setup_setup_jupyter.sh

# sorters

# bash setup_yass.sh $INSTALL

bash setup_combinato.sh $INSTALL

bash setup_hdsort.sh $INSTALL

bash setup_herdingspikes2.sh $INSTALL

bash setup_ironclust.sh $INSTALL

bash setup_kilosort.sh $INSTALL

bash setup_kilosort2.sh $INSTALL

bash setup_kilosort2_5.sh $INSTALL

bash setup_kilosort3.sh $INSTALL

bash setup_klusta.sh $INSTALL

# bash setup_mountainsort4.sh $INSTALL

# bash setup_spyking_circus.sh $INSTALL

bash setup_tridesclous.sh $INSTALL

bash setup_waveclus.sh $INSTALL

# this step currently needs to be done manually
# on a node with a GPU installed:

# srun --partition=gpu-single --ntasks=1 --time=0:30:00 --nodes=1 --ntasks-per-node=1 --cpus-per-gpu=1 --gres=gpu:RTX2080:1 --pty /bin/bash

# bash compile_gpu.sh $INSTALL
