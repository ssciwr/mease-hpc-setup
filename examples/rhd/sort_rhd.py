# Python script to concatenate, pre-process & sort RHD files with kilosort2

# the path where rhd files can be found
base_path = Path(r"/mnt/sds-hd/sd19b001/Filippo/Animals/Cohort12_33-38/#33")
# the location of the probe file
probe_path = "tetrode_64_backchip_nogroups.prb"
# the path where the kilosort output should go
output_path = Path(r"kilosort2")

import spikeinterface as si
import spikeinterface.extractors as se
import spikeinterface.sorters as ss
import spikeinterface.toolkit as st
import probeinterface as pi
from pathlib import Path
from pprint import pformat
import datetime


# a print function that timestamps the output
def tprint(string=""):
    print(f"|| {datetime.datetime.now():%H:%M:%S} || {string}")


tprint(f"base_path: {rhd_path}")

# search for all rhd files in base_path & sort them
rhd_files = sorted(list(base_path.glob("**/*.rhd")))
tprint(f"number of rhd files found: {len(rhd_files)}")

# create a recording object for each rhd file
recordings = [se.read_intan(file, stream_id="0") for file in rhd_files]
tprint(f"number of recordings: {len(recordings)}")

# concatenate all recordings to form a single long recording
multi_recording = si.concatenate_recordings(recordings)

# add duration and samples for each rhd file as recording annotations
# these will be stored in the spikeinterface_recording.json file
multi_recording.set_annotation(
    "recording_samples", [r.get_total_samples() for r in recordings]
)
multi_recording.set_annotation(
    "recording_duration", [r.get_total_duration() for r in recordings]
)
multi_recording.set_annotation(
    "recording_name", [r._kwargs["file_path"] for r in recordings]
)

# add probe info
probegroup = pi.read_prb(probe_path)
multi_recording = multi_recording.set_probegroup(probegroup)

tprint(f"recording_list:\n {pformat(multi_recording.recording_list)}")

# pre-processing

# note: this step converts the raw traces from a uint16 in range [0,2^16)
# to a int16 in range [-2^15, 2^15) which is what kilosort assumes it will get
multi_recording = st.preprocessing.scale(multi_recording, offset=-32768, dtype="int16")
# bandpass filter
multi_recording = st.preprocessing.bandpass_filter(
    multi_recording, freq_min=600, freq_max=6000
)

# set kilosort parameters
ks_params = ss.get_default_params("kilosort2")
ks_params["n_jobs_bin"] = 12
ks_params["detect_threshold"] = 3
ks_params["freq_min"] = 600
ks_params["NT"] = 256 * 1024 + 64
tprint(f"kilosort parameters\n: {pformat(ks_params)}")

# run kilosort
tprint("starting sorting")
sorting = ss.run_kilosort2(
    multi_recording, output_folder=output_path, verbose=True, **ks_params
)
tprint("sorting finished")
