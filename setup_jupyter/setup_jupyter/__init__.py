import subprocess
import json
import sys
import time
import os


def jupyter_lab_count():
    return len(json.loads(subprocess.getoutput("jupyter lab list --jsonlist")))


def get_jupyter_lab_token():
    return json.loads(subprocess.getoutput("jupyter lab list --jsonlist"))[0]["token"]


def start_jupyter_lab(ip, port):
    assert jupyter_lab_count() == 0, "Error: Jupyter Lab server already running."
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


def print_instructions(port, hostname, userid, token):
    print("2. Run this command in a new terminal on *your* computer:")
    print(
        f"\nssh -L{port}:{hostname}:{port} {userid}@bwforcluster.bwservices.uni-heidelberg.de\n"
    )
    print("3. Open this address in a web browser to access the jupyter notebook:\n")
    print(f"localhost:54736/?token={token}\n")


def start():
    port = 54736
    hostname = subprocess.getoutput("hostname")
    assert (
        hostname[:5] != "login"
    ), "Error: This is a login node, setup-jupyter should be ran on a compute node."
    ip = subprocess.getoutput('getent hosts $(uname -n) | head -1 | cut -d " " -f 1')
    userid = subprocess.getoutput("whoami")
    subproc = start_jupyter_lab(ip, port)
    token = get_jupyter_lab_token()
    print_instructions(port, hostname, userid, token)
    subproc.wait()


status_filename = ".setup-jupyter-status.txt"


def clear_status_file():
    try:
        os.remove(status_filename)
    except OSError:
        pass


def submit():
    minutes = 30
    gpus = 0
    job_id = subprocess.getoutput(
        f"sbatch --parsable -t${minutes} --output={status_filename} setup-jupyter"
    )
    print("Submitted job with id f{job_id}...", end="")
    time.sleep(2)
    while not os.path.exists(status_filename):
        print(".", end="")
        time.sleep(2)
    with open(status_filename) as f:
        print(f.read())
