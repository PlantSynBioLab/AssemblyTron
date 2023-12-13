'''AssemblyTron j5 parsing script 

This script guides the user through finding the j5 DNA assembly design saved on their local machine. 

The script does not require any input files, and it transfers parsed CSV files to the correct directory in AssemblyTron. 

This script requires that `pandas` be installed in the python environment where the script is run. 

This script should not be executed except when copied to a folder with a j5 combinatorial design file, and then it can also be run as a module by calling `AssemblyTron.j5_to_csvs`

'''


import os
import pandas as pd
# import pyarrow as pa
# import pyarrow.feather as feather

def find_section_index(lines, section_name):
    for i, line in enumerate(lines):
        if section_name in line:
            return i
    return -1

def parse_j5(path=os.getcwd(), file_suffix="_combinatorial.csv"):
    files = [f for f in os.listdir(path) if f.endswith(file_suffix)]
    
    for file in files:
        # Read lines from the CSV file
        with open(os.path.join(path, file), "r") as csv_file:
            j5lines = csv_file.readlines()

        oligo = find_section_index(j5lines, "Oligo Synthesis")
        pcr = find_section_index(j5lines, "PCR Reactions")
        gibson = find_section_index(j5lines, "Assembly Pieces (SLIC/Gibson/CPEC)")
        golden_gate = find_section_index(j5lines, "Assembly Pieces (Golden-gate)")
        combinations = find_section_index(j5lines, "Combinations of Assembly Pieces")

        # Check if sections were found; if not, set them to -1
        sections = [oligo, pcr, gibson, golden_gate, combinations]

        # Read the Oligo Synthesis portion of the CSV file
        oligo_read = pd.read_csv(os.path.join(path, file), skiprows=oligo + 1, nrows=pcr - oligo - 3) if oligo >= 0 else None
        if oligo_read is not None:
            oligo_read = oligo_read.loc[:, ~oligo_read.columns.str.startswith("X")]
            oligo_read.to_csv(os.path.join(path, "oligo.csv"), index=False)

        # Read the PCR Reactions portion of the CSV file
        if pcr >= 0:
            if gibson >= 0 and golden_gate >= 0:
                pcr_read = pd.read_csv(os.path.join(path, file), skiprows=pcr + 1, nrows=golden_gate - pcr - 3)
            elif golden_gate >= 0:
                pcr_read = pd.read_csv(os.path.join(path, file), skiprows=pcr + 1, nrows=golden_gate - pcr - 3)
            elif gibson >= 0:
                pcr_read = pd.read_csv(os.path.join(path, file), skiprows=pcr + 1, nrows=gibson - pcr - 3)

            pcr_read = pcr_read.loc[:, ~pcr_read.columns.str.startswith("X")]
            pcr_read = pcr_read.drop(columns=['Alternate Template'])
            pcr_read.to_csv(os.path.join(path, "pcr.csv"), index=False)

        # Read the Assembly Pieces portion of the CSV file
        if gibson >= 0 and golden_gate >= 0:
            assembly_read = pd.read_csv(os.path.join(path, file), skiprows=golden_gate - 1, nrows=combinations - golden_gate - 3)
        elif golden_gate >= 0:
            assembly_read = pd.read_csv(os.path.join(path, file), skiprows=golden_gate + 1, nrows=combinations - golden_gate - 3)
        elif gibson >= 0:
            assembly_read = pd.read_csv(os.path.join(path, file), skiprows=gibson + 1, nrows=combinations - gibson - 3)

        if assembly_read is not None:
            assembly_read = assembly_read.loc[:, ~assembly_read.columns.str.startswith("X")]
            assembly_read.to_csv(os.path.join(path, "assembly.csv"), index=False)

        # Read the Combinations of Assembly Pieces
        if combinations >= 0:
            combinations_read = pd.read_csv(os.path.join(path, file), skiprows=combinations + 2, na_values=[""])
            combinations_read.to_csv(os.path.join(path, "combinations.csv"), index=False)

        # Save data as Feather files for sections that were found
        # if oligo_read is not None:
        #     pa_oligo = pa.Table.from_pandas(oligo_read)
        #     feather.write_feather(pa_oligo, os.path.join(path, "oligo.feather"))

        # if pcr >= 0:
        #     pa_pcr = pa.Table.from_pandas(pcr_read)
        #     feather.write_feather(pa_pcr, os.path.join(path, "pcr.feather"))

        # if assembly_read is not None:
        #     pa_assembly = pa.Table.from_pandas(assembly_read)
        #     feather.write_feather(pa_assembly, os.path.join(path, "assembly.feather"))

        # if combinations >= 0:
        #     pa_combinations = pa.Table.from_pandas(combinations_read)
        #     feather.write_feather(pa_combinations, os.path.join(path, "combinations.feather"))

if __name__ == "__main__":
    parse_j5()