import subprocess
import json
import sys
import time
import click


def print_instructions(port, hostname, userid, token):
    print("\n To access the jupyter notebook:")
    print(
        "\n1. Press the keys 'Enter', then '~', then 'C' in your terminal: this should give you a new command line starting with 'ssh>'"
    )
    print(
        "\n2. Paste this into the terminal and press 'Enter': it should then say 'Forwarding Port', press 'Enter' again to go back to the normal command line"
    )
    print(f"\n-L{port}:{hostname}:{port}\n")
    print("3. Open this address in a web browser to access the jupyter notebook:\n")
    print(f"localhost:{port}/?token={token}\n", flush=True)
    print(
        "\nNote: If step 2 doesn't work in your ssh client, you can instead open a new command line terminal, and create a new ssh connection which forwards the required port with this command: (you will probably have to re-enter your OTP and password though)"
    )
    print(
        f"\nssh -L{port}:{hostname}:{port} {userid}@bwforcluster.bwservices.uni-heidelberg.de\n"
    )


def get_jupyter_lab_servers(job_id):
    jupyter_data = subprocess.getoutput(
        f"srun --jobid={job_id} jupyter lab list --jsonlist"
    )
    try:
        data = json.loads(jupyter_data)
        if len(data) > 1:
            print("** Warning: multiple running jupyter servers found **")
        return data
    except:
        return None


def get_scontrol_output(job_id):
    data = {}
    scontrol_output = subprocess.getoutput(f"scontrol show job {job_id}")
    for item in scontrol_output.split():
        pair = item.split("=")
        if len(pair) == 2:
            key, value = pair
            data[key] = value
    return data


def wait_for_job_to_run(job_id):
    print(
        "Job queued...",
        end="",
        flush=True,
    )
    state = get_scontrol_output(job_id).get("JobState")
    while not state or state != "RUNNING":
        try:
            print(".", end="", flush=True)
            time.sleep(2)
            state = get_scontrol_output(job_id).get("JobState")
        except KeyboardInterrupt:
            print(f"\nCancelling job {job_id}.")
            print(subprocess.getoutput(f"scancel {job_id}"))
            sys.exit()
    print(f"job running.", flush=True)


def wait_for_info_and_print(job_id):
    hostname = get_scontrol_output(job_id).get("BatchHost")
    userid = subprocess.getoutput("whoami")
    print("Looking for jupyter server info...", end="", flush=True)
    servers = get_jupyter_lab_servers(job_id)
    while not servers:
        print(".", end="", flush=True)
        time.sleep(2)
        servers = get_jupyter_lab_servers(job_id)
    print(f"found.", flush=True)
    for server in servers:
        print_instructions(server["port"], hostname, userid, server["token"])
