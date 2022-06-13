# Install Notes

Some notes on the installation on MLS&WISO,
(hopefully) not relevant for the end user.

The initial idea is just to install everything in a folder,
then share this location along with a script for the user to source,
which puts everything in PATH, loads the relevant modules,
and activates the conda env.

## Location

All files are now installed on SDS:

- `/mnt/sds-hd/sd19b001/HPC_INSTALLATION`

## Reproducibility

To recreate the HPC installation:

- remove all files in `/mnt/sds-hd/sd19b001/HPC_INSTALLATION`
- run `setup_all.sh` which should reinstall everything from scratch
- note: for ironclust gpu support, `compile_gpu.sh` also needs to run on a node with a GPU

### Previous location (no longer in use)

Temporary workspace allocated for 30 days with:

```
ws_allocate measelab 30
```

Location of resulting folder:

```
ws_find measelab
```

Then set read/write access for all members of `bw20g013` group (NB: not yet confirmed that this works):

```
setfacl -Rm g:bw20g013:rwX,d:g:bw20g013:rwX /gpfs/bwfor/work/ws/hd_uk239-measelab

```

To see access permissions:

```
getfacl $(ws_find measelab)
```

Status of all workspaces can be shown with:

```
ws_list
```

To renew the workspace for another 30 days from now:

```
ws_extend measelab 30
```
