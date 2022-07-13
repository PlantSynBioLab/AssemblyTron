#[metadata]
from setuptools import setup, find_packages

setup(
    name = "DNA-AssemblyLine",
    version = "0.0.2",
    author = "John Bryant",
    author_email = "jbryant2@vt.edu",
    description = "A package for automating DNA assembly with an Opentrons liquid handling robot",
    long_description = "file: README.md",
    long_description_content_type = "text/markdown",
    url = "https://github.com/PlantSynBioLab/opentrons",
    packages=find_packages(where="opentrons"),
#    Bug Tracker = []
    classifiers =[
        "Programming Language :: Python :: 3",
    	"Operating System :: OS Independent",
	"license :: Apache License 2.0"],

#[options]
#package_dir =
#    = src
#packages = find:
    python_requires = ">=3.6")

#[options.packages.find]
#where = src