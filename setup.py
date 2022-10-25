#[metadata]
from setuptools import setup
from setuptools import find_packages

setup(
    name = "AssemblyTron",
    version = "0.0.8",
    author = "John Bryant",
    author_email = "jbryant2@vt.edu",
    description = "A package for automating DNA assembly with an Opentrons liquid handling robot",
    long_description = "AssemblyTron is a package for automating DNA assembly with an Opentrons liquid handling robot. DNA-Assembly line implements combinatorial DNA assemblies based on designs created with j5 (Hillson, N.J., Rosengarten, R.D., and Keasling J.D. (2012) j5 DNA Assembly Design Automation Software. ACS Synthetic Biology 1 (1), 14-21. DOI: 10.1021/sb2000116), currently accessibe via: https://public-diva.jbei.org/. \nThe AssemblyTron vignette is hosted at: https://plantsynbiolab.github.io/AssemblyTron-vignette/ and is intended to guide a novice user through installation and use of AssemblyTron to build DNA constructs via Golden Gate assembly in the Opentrons OT-2 robot. We assume that the user has a folder/directory containing the results of a j5 combinatorial assembly design on the computer connected to their OT-2 robot. AssemblyTron then operates on the files within this folder to generate specific assembly instructions for the user and the OT-2 robot which are saved in this folder. The vignette is also available on our Github. \nTechnical documentation is stored on our Github and hosted at: https://assemblytron.readthedocs.io/en/latest/AssemblyTron.html",
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
      'pandas','numpy','datetime'
  ],
  )

#[options.packages.find]
#where = src