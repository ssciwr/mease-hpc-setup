import subprocess
import json
import sys
import time
import os


def start_jupyter_lab(ip, port):
    print("1. Starting Jupyter Lab server...", end="")
    p = subprocess.Popen(
        ["jupyter", "lab", "--no-browser", f"--port={port}", f"--ip={ip}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    time.sleep(1)
    while jupyter_lab_count() == 0:
        print(".", end="")
        time.sleep(1)
    print("done.\n")
    return p


port = 54736


def start():
    assert (
        hostname[:5] != "login"
    ), "Error: This is a login node, setup-jupyter should be ran on a compute node."
    ip = subprocess.getoutput('getent hosts $(uname -n) | head -1 | cut -d " " -f 1')
    subproc = start_jupyter_lab(ip, port)
    subproc.wait()


def print_instructions(port, hostname, userid, token):
    print("2. Run this command in a new terminal on *your* computer:")
    print(
        f"\nssh -L{port}:{hostname}:{port} {userid}@bwforcluster.bwservices.uni-heidelberg.de\n"
    )
    print("3. Open this address in a web browser to access the jupyter notebook:\n")
    print(f"localhost:54736/?token={token}\n", flush=True)


def get_jupyter_lab_token(job_id):
    return json.loads(
        subprocess.getoutput(f"srun --jobid={job_id} jupyter lab list --jsonlist")
    )[0]["token"]


def get_scontrol_output(jobid):
    data = {}
    scontrol_output = subprocess.getoutput(f"scontrol show job {jobid}")
    for item in scontrol_output.split:
        key, value = item.split("=")
        data[key] = value


def submit():
    minutes = 30
    gpus = 0
    sbatch_cmd = f"sbatch --parsable -t{minutes} --output=.setup-jupyter-log.txt setup-jupyter-start"
    print(sbatch_cmd)
    job_id = subprocess.getoutput(sbatch_cmd)
    print(f"Submitted job with id {job_id}...", end="", flush=True)
    time.sleep(2)
    output = get_scontrol_output(job_id)
    print(output)
    while output["JobState"] != "RUNNING":
        print(".", end="", flush=True)
        time.sleep(2)
        output = get_scontrol_output(job_id)
        print(output)
    userid = subprocess.getoutput("whoami")
    token = get_jupyter_lab_token(job_id)
    print_instructions(port, scontrol_output["BatchHost"], userid, token)
