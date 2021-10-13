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

To do this automatically every time you log on or run a job, add the above line to your `~/.bashrc`:

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

and follow the instructions.
See [setup-jupyter](https://github.com/ssciwr/mease-hpc-setup/tree/main/setup-jupyter) for more information.

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
Other GPU types available are listed here:
https://wiki.bwhpc.de/e/BwForCluster_MLS%26WISO_Production_Hardware#Coprocessor_Nodes

If you don't mind which type of GPU you get, you can simply use

```
--gres=gpu:1
```

Once the job starts you will be logged into the machine - if you didn't add
the source line to your `~/.bashrc` file you will have to run it again manually.

## Batch jobs

Longer jobs can be submitted as batch jobs to a queue, and will run when resources are available.
See https://wiki.bwhpc.de/e/BwForCluster_MLS%26WISO_Production_Slurm for more information.