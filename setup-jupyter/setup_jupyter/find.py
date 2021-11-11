import subprocess
import setup_jupyter.util as util
import click


@click.command()
@click.argument("job_id", required=False, default=-1)
def find(job_id):
    if job_id == -1:
        job_id = subprocess.getoutput("squeue - t RUNNING - o % i - h | head -n 1")
    util.wait_for_info_and_print(job_id)
