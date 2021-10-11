from setuptools import find_packages, setup

setup(
    name="setup_jupyter",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "setup-jupyter=setup_jupyter.command_line:submit",
            "setup-jupyter-start=setup_jupyter.command_line:start",
        ]
    },
)
