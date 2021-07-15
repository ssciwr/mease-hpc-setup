# mease-hpc-setup

work-in-progress setup guide & installation scripts for running https://github.com/lkeegan/mease-lab-to-nwb on HPC

## MLS&WISO Cluster

### Initial setup
To get started, after logging into the cluster, do
```
source /gpfs/bwfor/work/ws/hd_uk239-measelab/init.sh
```
You should then be in the `measelab` conda environment, with these programs installed & on path:
- conda
- matlab
- mease-lab-to-nwb
- kilosort 2.5

If you want this to be done every time you log on, add the above line to the file `~/.bashrc`

Note: all dependencies have for now been installed to this temporary workspace `/gpfs/bwfor/work/ws/hd_uk239-measelab`
 (which all users in `bw20g013` should have read/write access to)

### SDS
To get SDS access on the cluster type
```
kinit
```
using your SDS@hd service password

The files are located at
```
/mnt/sds-hd/sd19b001
```

### Interactive use
To run an interactive job (i.e. log on directly to a HPC node and run commands there):

```
srun --partition=gpu-single --ntasks=1 --time=0:30:00 --nodes=1 --ntasks-per-node=1 --cpus-per-gpu=1 --mem=64gb --gres=gpu:RTX2080:1 --pty /bin/bash
```

This asks for 30mins with 1 cpu, 1 RTX2080 GPU, and 64GB of ram.
Other GPU types available are listed here:
https://wiki.bwhpc.de/e/BwForCluster_MLS%26WISO_Production_Hardware#Coprocessor_Nodes

Once the job starts you will be logged into the machine, and will have to activate the measelab environment again:

### Batch jobs

Longer jobs can be submitted as batch jobs to a queue, and will run when resources are available.