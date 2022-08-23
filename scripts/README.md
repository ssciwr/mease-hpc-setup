# Install Notes

Some notes on the installation on Helix,
(hopefully) not relevant for the end user.

The initial idea is just to install everything in a folder,
then share this location along with a script for the user to source,
which puts everything in PATH, loads the relevant modules,
and activates the conda env.

## Location

All files are now installed on SDS:

- `/mnt/sds-hd/sd19b001/HPC_INSTALLATION_HELIX`

## Reproducibility

To recreate the HPC installation:

- remove all files in `/mnt/sds-hd/sd19b001/HPC_INSTALLATION_HELIX`
- run `setup_all.sh` which should reinstall everything from scratch
- note: for ironclust gpu support, `compile_gpu.sh` also needs to run on a node with a GPU
