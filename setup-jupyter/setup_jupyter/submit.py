import subprocess
import click
import setup_jupyter.util as util


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
    util.wait_for_job_to_run(job_id)
    util.wait_for_info_and_print(job_id)
