import subprocess
from random import randint
import click


def get_random_port(min_port=50000, max_port=59999):
    return randint(min_port, max_port)


@click.command()
def start():
    ip = subprocess.getoutput('getent hosts $(uname -n) | head -1 | cut -d " " -f 1')
    port = get_random_port()
    print(f"Starting Jupyter Lab server on {ip}:{port}", flush=True)
    subproc = subprocess.Popen(
        ["jupyter", "lab", "--no-browser", f"--port={port}", f"--ip={ip}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    subproc.wait()
