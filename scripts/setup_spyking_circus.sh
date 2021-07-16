cd $1

# init conda
source miniconda3/etc/profile.d/conda.sh

# activate env
conda activate measelab

pip install spyking-circus

# note: apparently installs files to $HOME?
# should check if them not existing breaks anything for the user,
# or if they need to copy these files to their $HOME?

# also see if MPI is working, docs say it needs a hosts file but also seem aimed at a desktop user?