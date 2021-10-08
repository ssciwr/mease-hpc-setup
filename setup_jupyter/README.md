# setup-jupyter

Python script to help with setting up a jupyter server instance on HPC

After logging in and starting an interactive job,
type `setup-jupyter` to start a jupyter server,
and get instructions for how to access it from the web browser on your computer.

Example output:

```
(measelab) [hd_ab123@XXXXXX ~]$ setup-jupyter
1. Starting Jupyter Lab server......done.

2. Run this command on *your* computer:

ssh -L12345:XXXXXX:12345 hd_ab123@bwforcluster.bwservices.uni-heidelberg.de

3. Open this address in a web browser:

localhost:12345/?token=abcdefghijklmnopqrstuvwxyz

```
