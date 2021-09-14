set -e -x

cd $1

source init.sh

# download Combinato (no release yet: using git master)
git clone https://github.com/jniediek/combinato

cd combinato
python setup_options.py
