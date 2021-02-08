# OT2 Modular Cloning (MoClo) and Transformation in E. coli Workflow

Source: https://github.com/DAMPLAB/OT2-MoClo-Transformation-Ecoli

Material for OT2 Modular Cloning and Transformation in E. coli Workflow

This workflow enables end-to-end molecular cloning using the OT2 liquid handling robot by OpenTrons. This includes:
- Performing modular cloning (Golden Gate) reactions.
- Transforming plasmids into E. coli using heat shock.
- Plating cell transformations onto rectangular agar plates.

All code for this project is freely distributed for academic and commercial uses under the MIT license.

## General Installation

1. Confirm that you have [Python 3](https://www.python.org/downloads/) installed.

2. Download [OT2 APP](https://opentrons.com/ot-app) from Opentrons' website.

3. Clone the [GitHub repository](https://github.com/DAMPLAB/OT2-MoClo-Transformation-Ecoli) to a local computer.

## Modular Cloning, Cell Transformation, and Cell Plating

### Getting Started

Users looking to implement the OT2 Modular Cloning and Transformation in E. coli workflow are encouraged to consult the [instructions](docs/MoClo_Transformation_instructions.pdf). If you are looking to contribute to this project, please raise an issue or pull request. Otherwise, feel free to reach out to [rychen58](mailto:richen@bu.edu).

### Initial setup

1. Prepare 1 CSV file (which can be produced in Excel) representing input DNA plate map. The input DNA plate maps may contain up to 96 DNA fragments and vectors, 8 rows by 12 columns, with each cell containing the name for DNA parts and empty wells left blank. The CSV file should represent 96-well microplate format plates of DNA parts at the desire concentration chossen by the users.

2. Prepare 1 CSV file representing the combination list for combinations of parts to assemble, with each row representing one assembly. Each row should have N columns with the names of the parts to assemble (which must match the names in the plate maps of step 1).

### Generating protocol

3. Run the OT2-MoClo/moclo_transformation/moclo_transform_generator.py using Python (e.g. typing `python3 moclo_transform_generator.py` in the command line). Select the plate map, combinations list, and an output folder for the protocol when prompted.

4. A protocol named `moclo_transform_protocol.py` should be saved in the output folder. 

## Authors

* **Rita R. Chen** - [rychen58](https://github.com/rychen58)
* **Nick Emery** - [emernic](https://github.com/emernic)


