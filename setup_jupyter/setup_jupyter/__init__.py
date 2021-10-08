import subprocess
import json
import sys
import time


def jupyter_lab_count():
    return len(json.loads(subprocess.getoutput("jupyter lab list --jsonlist")))


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
    token = json.loads(subprocess.getoutput("jupyter lab list --jsonlist"))[0]["token"]
    return token


def print_instructions(port, hostname, userid, token):
    print("2. Run this command on *your* computer:")
    print(
        f"\nssh -L{port}:{hostname}:{port} {userid}@bwforcluster.bwservices.uni-heidelberg.de\n"
    )
    print("3. Open this address in a web browser:\n")
    print(f"localhost:54736/?token={token}\n")


def start():
    port = 54736
    hostname = subprocess.getoutput("hostname")
    ip = subprocess.getoutput('getent hosts $(uname -n) | head -1 | cut -d " " -f 1')
    userid = subprocess.getoutput("whoami")
    token = start_jupyter_lab(ip, port)
    print_instructions(port, hostname, userid, token)
