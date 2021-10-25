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


def get_jupyter_lab_info(job_id):
    jupyter_data = subprocess.getoutput(
        f"srun --jobid={job_id} jupyter lab list --jsonlist"
    )
    try:
        return json.loads(jupyter_data)[0]
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


@click.command()
@click.option(
    "--runtime",
    type=click.IntRange(1, 48),
    required=True,
    default=1,
    help="Job runtime in hours",
    show_default=True,
    prompt="Job runtime in hours",
)
@click.option(
    "--gpu-type",
    type=click.Choice(
        [
            "none",
            "any",
            "K80",
            "TITAN",
            "V100",
            "GTX1080",
            "RTX2080",
            "V100",
            "V100S",
            "RTX3090",
            "RTX8000",
        ],
        case_sensitive=False,
    ),
    required=True,
    default="any",
    help="Type of GPU",
    show_default=True,
    prompt="GPU type required",
)
@click.option(
    "--cpus",
    type=click.IntRange(1, 32),
    required=True,
    default=1,
    help="Number of cpus required",
    show_default=True,
    prompt="Number of cpus required",
)
@click.option(
    "--memory",
    type=click.IntRange(16, 360),
    required=True,
    default=60,
    help="Memory required in GB",
    show_default=True,
    prompt="Memory required in GB",
)
@click.option(
    "-v",
    "--verbose",
    default=False,
    is_flag=True,
    help="Verbose output",
)
def submit(runtime, gpu_type, cpus, memory, verbose):
    sbatch_options = "--partition=single"
    with_gpu = gpu_type != "none"
    if with_gpu:
        sbatch_options = f"--partition=gpu-single --cpus-per-gpu={cpus} --gres=gpu{':1' if gpu_type == 'any' else ':' + gpu_type + ':1'}"
    minutes = 60 * runtime
    sbatch_cmd = f"sbatch --parsable -t{minutes} --ntasks-per-node={cpus} --mem={memory}gb {sbatch_options} --output=.setup-jupyter-log.txt setup-jupyter-start"
    if verbose:
        print("# sbatch command: " + sbatch_cmd)
    job_id = subprocess.getoutput(sbatch_cmd)
    print(
        f"\nSubmitted {runtime}-hour {cpus}-CPU, {memory}gb memory{', ' + gpu_type + ' GPU' if with_gpu else ''} job with id {job_id}.",
        flush=True,
    )
    wait_for_job_to_run(job_id)
    hostname = get_scontrol_output(job_id).get("BatchHost")
    userid = subprocess.getoutput("whoami")
    print("Looking for jupyter server info...", end="", flush=True)
    info = get_jupyter_lab_info(job_id)
    while not info:
        print(".", end="", flush=True)
        time.sleep(2)
        info = get_jupyter_lab_info(job_id)
    print(f"found.", flush=True)
    print_instructions(info["port"], hostname, userid, info["token"])
