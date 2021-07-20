# Install Notes

Some notes on the installation on MLS&WISO,
(hopefully) not relevant for the end user.

The initial idea is just to install everything locally,
then share this location along with a script for the user to source,
which puts everything in PATH, loads the relevant modules,
and activates the conde env.

## Location

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

Should find a better long term solution here, but this
should be ok for testing purposes.

Todo:

- see if read-only access would still allow everything to run
- find long term alternative
- better way to do this
  - singularity container? (will GPU etc work?)
  - spack packages for sorters?
  - get them installed by urz as modules? (kilosort2 is already on there)


## Reproducibility

For now just a bunch of bash scripts:

- wipe workspace then run `setup_all.sh` should reinstall everything from scratch
- after that, `compile_gpu.sh` needs to run on a node with the GPU

Todo:

- integrate the compile_gpu step into setup_all as a job?
