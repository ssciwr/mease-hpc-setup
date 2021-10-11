import subprocess
import json
import sys
import time
import os
import click


def start_jupyter_lab(ip, port):
    print("1. Starting Jupyter Lab server...", end="")
    return subprocess.Popen(
        ["jupyter", "lab", "--no-browser", f"--port={port}", f"--ip={ip}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


port = 54736


def start():
    ip = subprocess.getoutput('getent hosts $(uname -n) | head -1 | cut -d " " -f 1')
    subproc = start_jupyter_lab(ip, port)
    subproc.wait()


def print_instructions(port, hostname, userid, token):
    print("\n1. Run this command in a new terminal on *your* computer:")
    print(
        f"\nssh -L{port}:{hostname}:{port} {userid}@bwforcluster.bwservices.uni-heidelberg.de\n"
    )
    print("2. Open this address in a web browser to access the jupyter notebook:\n")
    print(f"localhost:54736/?token={token}\n", flush=True)


def get_jupyter_lab_info(job_id):
    jupyter_data = subprocess.getoutput(
        f"srun --jobid={job_id} jupyter lab list --jsonlist"
    )
    try:
        return json.loads(jupyter_data)[0]
    except:
        return None


def get_scontrol_output(jobid):
    data = {}
    scontrol_output = subprocess.getoutput(f"scontrol show job {jobid}")
    for item in scontrol_output.split():
        pair = item.split("=")
        if len(pair) == 2:
            key, value = pair
            data[key] = value
    return data


def submit():
    minutes = click.prompt("Job runtime in minutes", type=int, default=60)
    gpu = click.prompt("GPU required", type=bool, default=False)
    options = "--partition=single"
    if gpu:
        options = "--partition=gpu-single --gres=gpu:1"
    sbatch_cmd = f"sbatch --parsable -t{minutes} {options} --output=.setup-jupyter-log.txt setup-jupyter-start"
    job_id = subprocess.getoutput(sbatch_cmd)
    print(f"Submitted job with id {job_id}...", end="", flush=True)
    time.sleep(2)
    state = get_scontrol_output(job_id).get("JobState")
    while not state or state != "RUNNING":
        print(".", end="", flush=True)
        time.sleep(2)
        state = get_scontrol_output(job_id).get("JobState")
    print(f"job started.", flush=True)
    hostname = get_scontrol_output(job_id).get("BatchHost")
    userid = subprocess.getoutput("whoami")
    print("Looking for jupyter server info...", flush=True)
    info = get_jupyter_lab_info(job_id)
    while not info:
        print(".", end="", flush=True)
        time.sleep(2)
        info = get_jupyter_lab_info(job_id)
    print(f"found.", flush=True)
    print_instructions(info["port"], hostname, userid, info["token"])
