cd $1

# workaround for git ssl isse
export GIT_SSL_NO_VERIFY=true

# download wave_clus (no release yet: using git master)
git clone https://github.com/csn-le/wave_clus