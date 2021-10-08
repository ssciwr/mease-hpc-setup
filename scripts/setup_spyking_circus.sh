set -e -x

cd $1

source init.sh

pip install spyking-circus

# note: apparently installs files to $HOME?
# should check if them not existing breaks anything for the user,
# or if they need to copy these files to their $HOME?

# also see if MPI is working, docs say it needs a hosts file but also seem aimed at a desktop user?
