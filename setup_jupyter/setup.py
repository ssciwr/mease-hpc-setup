from setuptools import find_packages, setup

with open("README.md", encoding="utf8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="setup_jupyter",
    version="0.0.1",
    author="Liam Keegan",
    author_email="liam@keegan.ch",
    description="Script to run jupyter server on HPC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ssciwr/mease-hpc-setup/setup_jupyter",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "setup-jupyter = setup_jupyter.submit:submit",
            "setup-jupyter-start = setup_jupyter.start:start",
        ]
    },
)
