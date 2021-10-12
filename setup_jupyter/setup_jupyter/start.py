import subprocess
from random import randrange
import click


@click.command()
def start():
    ip = subprocess.getoutput('getent hosts $(uname -n) | head -1 | cut -d " " -f 1')
    port = 50000 + randrange(9999)
    print(f"Starting Jupyter Lab server on {ip}:{port}", flush=True)
    subproc = subprocess.Popen(
        ["jupyter", "lab", "--no-browser", f"--port={port}", f"--ip={ip}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    subproc.wait()
