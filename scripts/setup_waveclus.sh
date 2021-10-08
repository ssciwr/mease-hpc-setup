set -e -x

cd $1

source init.sh

# download wave_clus (no release yet: using git master)
git clone https://github.com/csn-le/wave_clus
