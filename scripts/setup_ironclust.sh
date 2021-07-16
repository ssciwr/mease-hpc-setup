cd $1

# make matlab available
module load math/matlab/R2021a

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# download ironclust (no release yet: using git master)
git clone https://github.com/flatironinstitute/ironclust

# compile ironclust GPU matlab code
cd ironclust/matlab
matlab -nodesktop -nosplash -r "irc2 compile;quit"
