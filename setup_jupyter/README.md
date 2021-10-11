# setup-jupyter

Python script to help with setting up a remote jupyter server instance on HPC

## How to use

1. Log in to the cluster

2. Start an interactive job where the jupyter server will run

3. Type `setup-jupyter`

4. Copy and paste the `ssh ...` command provided by `setup-jupyter` into a new terminal on your computer

5. Open the address provided in your web browser

## What it does

- starts a jupyter-lab server instance with the current ip
- gets the token from the server, as well as the username and hostname
- uses these to construct an ssh command to setup port forwarding
- also the web address where the jupyter notebook can be found

## Example output

```
(measelab) [hd_ab123@XXXXXX ~]$ setup-jupyter
1. Starting Jupyter Lab server......done.

2. Run this command on *your* computer:

ssh -L12345:XXXXXX:12345 hd_ab123@bwforcluster.bwservices.uni-heidelberg.de

3. Open this address in a web browser:

localhost:12345/?token=abcdefghijklmnopqrstuvwxyz

```
