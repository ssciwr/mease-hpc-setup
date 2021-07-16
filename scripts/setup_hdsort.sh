cd $1

# make matlab available
module load math/matlab/R2021a

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# download HDsort (no release yet: using git master)
git clone https://git.bsse.ethz.ch/hima_public/HDsort.git