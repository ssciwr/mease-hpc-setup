# Mease Lab HPC Setup

Instructions / reference information for using [mease-lab-to-nwb](https://github.com/ssciwr/mease-lab-to-nwb) on the [MLS&WISO bwForCluster](https://wiki.bwhpc.de/e/Category:BwForCluster_MLS%26WISO_Production).

## Account registration

Register for an account (see [BwForCluster_User_Access](https://wiki.bwhpc.de/e/BwForCluster_User_Access) for full instructions):

- [Join the RV](https://www.bwhpc-c5.de/en/ZAS/bwforcluster_collaboration.php)
  - You'll need an acronym and password from your advisor
  - Submit them in your request to join the RV as a coworker at the link above
- [Get permission from the University](https://bwforcluster.urz.uni-heidelberg.de/)
  - This is a separate step from joining the RV
- [Set up 2FA](https://bwservices.uni-heidelberg.de/user/twofa.xhtml)
  - 2-factor authentication using an authenticator app on your phone, e.g. Google Authenticator
  - The app then displays a new 6-digit code every 30 seconds
  - Use this code when asked for an OTP (one-time password) when logging in the cluster
- [Set a service password](https://bwservices.uni-heidelberg.de/)
  - After logging in with your uniid, you should see a list of services
  - Register for "bwForCluster MLS&WISO Production" and set a service password

## Initial setup

Log in to the cluster with username `hd_UNIID`, where `UNIID` is your uni-id:

```
ssh hd_ab123@bwforcluster.bwservices.uni-heidelberg.de
```

It will ask you for your bwForCluster service password, and your OTP (the current 6-digit token displayed in your authenticator app)

After logging into the cluster, do

```
source /gpfs/bwfor/work/ws/hd_uk239-measelab/init.sh
```

You should then be in the `measelab` conda environment, with these programs installed & on path:

- matlab
- [mease-lab-to-nwb](https://github.com/ssciwr/mease-lab-to-nwb)
- [setup-jupyter](https://github.com/ssciwr/mease-hpc-setup/setup-jupyter)
- spike sorters
  - [HDSort](https://git.bsse.ethz.ch/hima_public/HDsort)
  - [Herdingspikes2](https://github.com/mhhennig/hs2)
  - [IronClust](https://github.com/jamesjun/ironclust)
  - [Kilosort](https://github.com/MouseLand/Kilosort) 1.0, 2.0, 2.5, 3.0 (git master)
  - [Klusta](https://github.com/kwikteam/klusta)
  - [Tridesclous](https://tridesclous.readthedocs.io/)
  - [Waveclus](https://github.com/csn-le/wave_clus)
  - [Combinato](https://github.com/jniediek/combinato)

To do this automatically every time you log on or run a job (recommended), add the above line to your `~/.bashrc` with this command:

```
echo "source /gpfs/bwfor/work/ws/hd_uk239-measelab/init.sh" >> ~/.bashrc
```

## SDS

To get SDS access on the cluster type

```
kinit
```

and enter your SDS@hd service password when prompted.

The files are then located at

```
/mnt/sds-hd/sd19b001
```

## Interactive Jupyter use

There is a helper script for setting up and using a remote jupyter server on the cluster.
To use it, type

```
setup-jupyter
```

- it will ask you how long you need the job to run for, how much RAM you need, how many cpus, etc.
- it will then submit a batch job to the queue and wait for it to start running
  - if it doesn't start running after a few minutes, there may be no available nodes with the specs you asked for
  - to get something to run now, consider trying again with reduced requirements, e.g. `any` for gpu, `60` for gb of RAM
- once the job is running, it prints out instructions for what to do next
  - open an ssh shell within your terminal with the escape key sequence: `Enter`, `~`, `C`
    - if this works you'll see a new line starting with `ssh>`
  - copy and paste the line starting with `-L` and press `Enter`
    - it should then say `Forwarding port.`
    - press `Enter` again to return to the normal command line
  - open the web address starting with `localhost:` in your web browser

Type `setup-jupyter --help` or see [setup-jupyter](https://github.com/ssciwr/mease-hpc-setup/tree/main/setup-jupyter) for more information.

### Jupyter tips

- If you prefer the jupyter notebook interface to jupyter lab, go to "Help -> Launch Classic Notebook"
- The Jupyter working directory will be the same directory you ran `setup-jupyter` from
- SDS files are located at `/mnt/sds-hd/sd19b001`
  - Make sure you did `kinit` after logging in to have access to these
- When you are finished using jupyter, go to "File -> Shutdown"
  - This stops the job running on HPC, otherwise it will keep running there for the entire allocated time.
- On your ssh connection to the cluster, you can see all of your current jobs (queued and running) with `squeue`
  - If you have any jobs queued or running that you won't use any more, you can cancel them with `scancel JOBID`, where `JOBID` is the number displayed by `squeue`
- If you are stuck in the queue waiting for your job to start, consider reducing your requirements
  - The RAM, CPU & GPU for each type of node are listed [here](https://wiki.bwhpc.de/e/BwForCluster_MLS%26WISO_Production_Hardware#CPU_Nodes)
  - The actual RAM available is a little bit less than the listed values
  - You can see a list of idle nodes (but unfortunately not which specific GPU types are idle) with `sinfo_t_idle`
- If you run out of disk space in your home directory you can get various errors
  - e.g. `File Load Error` when trying to open a notebook
  - Deleting files from within jupyterlab doesn't actually delete them but moves them to a trash folder
    - To see how much space this is taking up: `du -sh .local/share/Trash`
    - To empty out the trash folder: `rm -rf .local/share/Trash`

## bwVisu

This is a new service for using graphical user interface programs - in particular Phy - on HPC.

### Account registration

- Assumes you have already set up your MLS&WISO HPC account
- [Set a service password](https://bwservices.uni-heidelberg.de/)
  - After logging in with your uniid, you should see a list of services
  - Register for "bwVisu" and set a service password

### Login

- go to [bwvisu-web.urz.uni-heidelberg.de/accounts/login](https://bwvisu-web.urz.uni-heidelberg.de/accounts/login)
- login in using
  - username: `hd_UNIID`, where `UNIID` is your uni-id (same as for MLS&WISO ssh login)
  - password: is the bwVisu service password you set above (*not* the same as your MLS&WISO service password!)
  - OTP: the current 6-digit token displayed in your authenticator app (same as for MLS&WISO ssh login)

### Use

- scroll down to Phy, then click on the blue "v2" button
- click the green "Start new job" button, enter runtime and press "start" again
- click on the new "Phy - v2 xyz123" button under "Running jobs"
- click on the Xpra Web Client link to open Phy in a new webpage
- Press "Enter" to close a dialog box that may or may not be initially visible
- You should then see a dialog box asking you to choose your params.py file
  - The "Home" directory is your home directory on MLS&WISO
  - For SDS: Other locations -> Computer -> mnt -> sds-hd -> sd19b001
  - Note: for SDS access you need to have an active kerberos ticket on MLS&WISO

## Interactive command-line use

To see how many idle nodes with GPUs attached are currently available:

```
sinfo_t_idle | grep "gpu-single"
```

To run an interactive job on one of these nodes (i.e. log on to it and run commands there):

```
srun --partition=gpu-single --ntasks=1 --time=0:30:00 --nodes=1 --ntasks-per-node=1 --cpus-per-gpu=1 --mem=64gb --gres=gpu:RTX2080:1 --pty /bin/bash
```

This asks for 30mins with 1 cpu, 1 RTX2080 GPU, and 64GB of ram.
Other GPU types available are listed in [this table](https://wiki.bwhpc.de/e/BwForCluster_MLS%26WISO_Production_Hardware#Coprocessor_Nodes)

(Note not all of the system RAM is available, e.g. if the machine has 64gb the most you can ask for is around 60gb)

If you don't mind which type of GPU you get, you can simply use

```
--gres=gpu:1
```

Once the job starts you will be logged into the machine - if you didn't add
the source line to your `~/.bashrc` file you will have to run it again manually.

## Batch jobs

Longer jobs can be submitted as batch jobs to a queue, and will run when resources are available.
See https://wiki.bwhpc.de/e/BwForCluster_MLS%26WISO_Production_Slurm for more information.

If you have a running batch job and you want to log in to the node where it is running you can do
```
srun --jobid=123456 --pty /bin/bash
```
Then e.g. `htop` to see CPU/RAM use, or `nvidia-smi` to see GPU use.

## MUA-Analysis

The MUA-Analysis repo is cloned at `/mnt/sds-hd/sd19b001/MUA-analysis`.

See `/mnt/sds-hd/sd19b001/Liam/MUA_examples/example1` for an example of how to run this on HPC.

### Files

The two matlab files are copied from Example_experiment, with these changes:

- the location of MUA-analysis on HPC is added to the matlab path
  - `addpath(genpath('/mnt/sds-hd/sd19b001/MUA-analysis'))`
- tell matlab to use 12 cpu cores
  - `parpool('local', 12)`
- the `dataDir` in example_experimental_parameters.m is modified
  - SDS on HPC is located at `/mnt/sds-hd/sd19b001`
  - HPC is linux so `/` is used to separate directories in paths (versus `\` on Windows)

After modifying example_experimental_parameters.m I ran `matlab -batch example_experimental_parameters` to re-generate the .mat file.

There is also a file `submit.sh`: this describes what resources your analysis job needs and what command it should run.

The file `slurm-1271232.out` and the folder `/mnt/sds-hd/sd19b001/Liam/ECE_testing_data/2021-08-20_M6_S1_ECE_Processing_example` are generated outputs from running the analysis.

### submit.sh

```
#!/bin/bash

#SBATCH --partition=gpu-single
#SBATCH --nodes=1
#SBATCH --cpus-per-gpu=12
#SBATCH --ntasks-per-node=12
#SBATCH --gres=gpu:1
#SBATCH --time=1:00:00

time matlab -batch ECE_Workflow_example
```

- first line just says this is a bash script
- then `#SBATCH` lines ask for
  - 12 cpu cores
  - 1 gpu
  - max job runtime of 1 hour
- last line is the actual job: runs the ECE_Workflow_example matlab script

### To run the analysis

- to submit the job: `sbatch submit.sh`
- you can then see status of your jobs with `squeue`
- the output will be written to `slurm-12345.out`, where `12345` will be your job id
- the files generated by the analysis (for this example) are found at `/mnt/sds-hd/sd19b001/Liam/ECE_testing_data/2021-08-20_M6_S1_ECE_Processing_example`

### Notes

- MUA-Analysis repo is cloned at `/mnt/sds-hd/sd19b001/MUA-analysis`
