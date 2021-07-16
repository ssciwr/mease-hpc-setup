cd $1

# init conda
source miniconda3/etc/profile.d/conda.sh

# activate env
conda activate measelab

# make mpi available (openmpi < 3 required apparently?)
# module load mpi/openmpi/2.1-intel-17.0

# install
# this installs a bunch of stuff:
# conda install -c spyking-circus spyking-circus -y
# try pip?:
pip install spyking-circus

# note: apparently installs files to $HOME? should check
# also see if MPI is working, docs say it needs a hosts file but seem aimed at desktop user?