# Mease Lab HPC Setup

Work-in-progress setup guide & installation scripts for
running [mease-lab-to-nwb](https://github.com/lkeegan/mease-lab-to-nwb) on HPC.

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
- various sorters
  - [HDSort](https://git.bsse.ethz.ch/hima_public/HDsort)
  - [Herdingspikes2](https://github.com/mhhennig/hs2)
  - [IronClust](https://github.com/jamesjun/ironclust)
  - [Kilosort](https://github.com/MouseLand/Kilosort)
    - 1.0
    - 2.0
    - 2.5
    - 3.0 (git master)
  - [Klusta](https://github.com/kwikteam/klusta)
  - ~[Mountainsort4](https://github.com/flatironinstitute/mountainsort)~
    - not yet working
  - ~[SpykingCircus](https://spyking-circus.readthedocs.io/)~
    - not yet working
  - [Tridesclous](https://tridesclous.readthedocs.io/)
  - [Waveclus](https://github.com/csn-le/wave_clus)
  - [Combinato](https://github.com/jniediek/combinato)
  - ~[YASS](https://github.com/paninski-lab/yass)~
    - not yet working

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

### Batch jobs

Longer jobs can be submitted as batch jobs to a queue, and will run when resources are available.
