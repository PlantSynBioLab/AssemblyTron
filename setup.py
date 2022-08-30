#[metadata]
from setuptools import setup
from setuptools import find_packages

setup(
    name = "AssemblyTron",
    version = "0.0.1",
    author = "John Bryant",
    author_email = "jbryant2@vt.edu",
    description = "A package for automating DNA assembly with an Opentrons liquid handling robot",
    long_description = "file: README.md",
    long_description_content_type = "text/markdown",
    url = "https://github.com/PlantSynBioLab/opentrons",
    packages=find_packages(where="AssemblyTron"),
#    Bug Tracker = []
    classifiers =[
        "Programming Language :: Python :: 3",
    	"Operating System :: OS Independent",
	    "License :: OSI Approved :: Apache Software License"],
    package_data={'': ['*.r','*.bat','*.sh']},
    include_package_data=True,

#[options]
#package_dir =
#    = src
#packages = find:
    python_requires = ">=3.6",
    install_requires=[
      'pandas', 'os','shutil','numpy','subprocess','datetime','csv'
  ],
  )

#[options.packages.find]
#where = src