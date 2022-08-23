import subprocess
import random
import click


def get_random_port(min_port=50000, max_port=59999):
    return random.randint(min_port, max_port)


def get_current_ip():
    return subprocess.getoutput("ip route | grep eno1 | grep src | awk '{print $9}'")


@click.command()
def start():
    ip = get_current_ip()
    port = get_random_port()
    print(f"Starting Jupyter Lab server on {ip}:{port}", flush=True)
    subproc = subprocess.Popen(
        ["jupyter", "lab", "--no-browser", f"--port={port}", f"--ip={ip}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    subproc.wait()
