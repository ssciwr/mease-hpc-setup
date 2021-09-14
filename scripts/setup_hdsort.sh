set -e -x

cd $1

source init.sh

# download HDsort (no release yet: using git master)
git clone https://git.bsse.ethz.ch/hima_public/HDsort.git