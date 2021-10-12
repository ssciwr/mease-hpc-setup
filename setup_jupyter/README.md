# setup-jupyter

Python script to help with setting up a remote jupyter server instance on HPC

## How to use

1. Log in to the cluster

- e.g. `ssh hd_ab213@bwforcluster.bwservices.uni-heidelberg.de`
- you'll need to enter an OTP (one time password) as well as your password
- you should be in the measelab environment (i.e. command line starts with `(measelab)`)
  - if not, `source /gpfs/bwfor/work/ws/hd_uk239-measelab/init.sh`

2. Start an interactive job where the jupyter server will run

- e.g. 30mins, no gpu: `srun --partition=single --time=0:30:00 --pty /bin/bash`
- or 4hrs, with gpu: `srun --partition=gpu-single --gres=gpu:1 --time=4:00:00 --pty /bin/bash`

3. Type `setup-jupyter` to

- start a jupyter lab server instance
- display a command to set up port forwarding
- display the web address of the jupyter notebook

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

2. Run this command in a new terminal on *your* computer:

ssh -L12345:XXXXXX:12345 hd_ab123@bwforcluster.bwservices.uni-heidelberg.de

3. Open this address in a web browser:

localhost:12345/?token=abcdefghijklmnopqrstuvwxyz

```

## Tips

- When you are finished using the notebook, go to "File -> Shutdown" so that the job on HPC is also stopped, otherwise it will keep running there for the allocated time.
- If you prefer the jupyter notebook interface to jupyter lab, go to "Help -> Launch Classic Notebook"
- SDS files are located at `/mnt/sds-hd/sd19b001`
