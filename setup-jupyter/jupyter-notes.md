# Jupyter Notes

Notes on setting up and using a remote jupyter server on the cluster.

## Server setup

Start an interactive job with the desired resources and run time, e.g.

```
srun --partition=gpu-single --ntasks=1 --time=0:30:00 --nodes=1 --ntasks-per-node=1 --cpus-per-gpu=1 --mem=64gb --gres=gpu:RTX2080:1 --pty /bin/bash
```

Print the hostname

```
hostname
```

Start a jupyter server

```
jupyter notebook --no-browser --port=54736 --ip=$(getent hosts $(uname -n) | head -1 | cut -d " " -f 1)
```

Tips from cluster support:

- specify the local ip address (otherwise with default `loalhost` the forwarding doesn't work, at least for me)
- recommend using a port > 50000 (if the port is already in use forwarding also won't work)

Note the token provided in the output of the jupyter startup output

## Port forwarding setup

In a new terminal, set up a new ssh connection to forward this port on the node running the jupyter server to the local computer
(need to enter the OTP and password again):

```
ssh -L54736:HOSTNAME:54736 hd_UNIID@bwforcluster.bwservices.uni-heidelberg.de
```

where

- `UNIID` is your uniid, e.g. uk239
- `HOSTNAME` is the hostname of the node running the jupyter server

## Web browser

Finally, open a web browser with the address

```
localhost:54736/?token=abcabcabcabcabcabcabcabcabc

```

where token is the one given in the jupyter server output
