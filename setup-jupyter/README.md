# setup-jupyter

Python script to help with setting up a remote jupyter server instance on HPC

## How to use

1. Log in to the cluster

- e.g. `ssh hd_ab213@bwforcluster.bwservices.uni-heidelberg.de`
- you'll need to enter an OTP (one time password) as well as your password
- make sure you can access sds (`ls /mnt/sds-hd/sd19b001`)
  - if not, `kinit`
- you should be in the measelab environment (i.e. command line starts with `(measelab)`)
  - if not, `source /mnt/sds-hd/sd19b001/HPC_INSTALLATION/init.sh`

2. Submit a jupyter lab server job

- `setup-jupyter`
  - note: the jupyter working directory will be the directory you run this command from
- choose how long it should run, and if you want a GPU (optionally which kind), how many CPUs, how much RAM
- the job is submitted to the queue
- once it is running, instructions for how to access the jupyter notebook are displayed

## What it does

- submits a job to the queue which will start a jupyter lab server instance
- monitors the state of the job
- once the job is running, get the token and hostname of the jupyter server
- uses these to construct an ssh command to setup port forwarding
- uses these to construct the web address where the jupyter notebook can be found

## Example output

```
(measelab) [hd_xx123@login3 setup_jupyter]$ setup-jupyter
Job runtime in hours [1]: 2
GPU type required (none, any, TITAN, V100, GTX1080, RTX2080, V100, V100S, RTX3090, RTX8000) [any]:
Number of cpus required [1]: 12
Memory required in GB [60]: 60

Submitted 2-hour 12-CPU, 60gb memory, any GPU job with id 787623...job started.
Looking for jupyter server info....found.

 To access the jupyter notebook:

1. Press the keys 'Enter', then '~', then 'shift+C' in your terminal: this should give you a new command line starting with 'ssh>'

2. Paste this into the terminal and press 'Enter': it should then say 'Forwarding Port', press 'Enter' again to go back to the normal command line

-L57191:h11c1111:57191

3. Open this address in a web browser to access the jupyter notebook:

localhost:57191/?token=0e28e2f990ca9f2d7feadd0daa1bb439eaebaf69a623c738


Note: If step 2 doesn't work in your ssh client, you can instead open a new command line terminal, and create a new ssh connection which forwards the required port with this command: (you will probably have to re-enter your OTP and password though)

ssh -L57191:h11c1111:57191 hd_xx123@bwforcluster.bwservices.uni-heidelberg.de
```
