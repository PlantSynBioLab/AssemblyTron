# AssemblyTron

This is a package to automate DNA assembly builds with the Opentron OT-2 liquid handling robot. You can use
[Github-flavored Markdown](https://guides.github.com/PlantSynBioLab/opentrons)
to access the working repository.

AssemblyTron is a package for automating DNA assembly with an Opentrons liquid handling robot. DNA-Assembly line implements combinatorial DNA assemblies based on designs created with j5 (Hillson, N.J., Rosengarten, R.D., and Keasling J.D. (2012) j5 DNA Assembly Design Automation Software. ACS Synthetic Biology 1 (1), 14-21. DOI: 10.1021/sb2000116), currently accessibe via: https://public-diva.jbei.org/.

This vignette is intended to guide a novice user through installation and use of AssemblyTron to build DNA constructs via Golden Gate assembly in the Opentrons OT-2 robot. We assume that the user has a folder/directory containing the results of a j5 combinatorial assembly design on the computer connected to their OT-2 robot. AssemblyTron then operates on the files within this folder to generate specific assembly instructions for the user and the OT-2 robot which are saved in this folder.