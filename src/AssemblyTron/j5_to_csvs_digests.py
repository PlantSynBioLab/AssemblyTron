'''AssemblyTron j5 parsing script. This variation of the script accomodates desingns that inculde destination plasmid backbones. It functions similarly to j5_to_csvs

This script guides the user through finding the j5 DNA assembly design saved on their local machine. 

The script does not require any input files, and it transfers parsed CSV files to the correct directory in AssemblyTron. 

This script requires that `pandas` be installed in the python environment where the script is run. 

This script should not be executed except when copied to a folder with a j5 combinatorial design file, and then it can also be run as a module by calling `AssemblyTron.j5_to_csvs_digests`

'''
if __name__ == '__main__':
        
    import os
    import pandas as pd
    import re

    def parse_j5(path=".", file="_combinatorial.csv"):
        file_list = [f for f in os.listdir(path) if f.endswith(file)]

        for input_file in file_list:
            with open(os.path.join(path, input_file), 'r') as file:
                j5lines = file.readlines()

            # Extract line numbers for different sections
            digests = [i for i, line in enumerate(j5lines) if re.search("Digest Linearized Pieces", line)]
            oligo = [i for i, line in enumerate(j5lines) if re.search("Oligo Synthesis", line)]
            pcr = [i for i, line in enumerate(j5lines) if re.search("PCR Reactions", line)]
            gibson = [i for i, line in enumerate(j5lines) if re.search("Assembly Pieces (SLIC/Gibson/CPEC)", line)]
            golden_gate = [i for i, line in enumerate(j5lines) if re.search("Assembly Pieces (Golden-gate)", line)]
            combinations = [i for i, line in enumerate(j5lines) if re.search("Combinations of Assembly Pieces", line)]

            # Read Oligo Synthesis section of the CSV file
            oligo_read = pd.read_csv(input_file, skiprows=oligo[0] + 1, nrows=pcr[0] - oligo[0] - 3)
            oligo_read.to_csv(os.path.join(path, "oligo.csv"), index=False)

            pcr_read = None  # Define pcr_read before the conditional block
            assembly_read= None
            combinations_read=None
            digests_read=None
            # Read PCR Reactions section of the CSV file
            if gibson and golden_gate:
                pcr_read = pd.read_csv(input_file, skiprows=pcr[0] + 1, nrows=golden_gate[0] - pcr[0] - 3)
            elif golden_gate:
                pcr_read = pd.read_csv(input_file, skiprows=pcr[0] + 1, nrows=golden_gate[0] - pcr[0] - 3)
            elif gibson:
                pcr_read = pd.read_csv(input_file, skiprows=pcr[0] + 1, nrows=gibson[0] - pcr[0] - 3)
            
            if pcr_read is not None:
                pcr_read.to_csv(os.path.join(path, "pcr.csv"), index=False)
                print("pcr file created successfully")

            # Read Assembly Pieces section of the CSV file
            if gibson and golden_gate:
                assembly_read = pd.read_csv(input_file, skiprows=golden_gate[0] + 1, nrows=combinations[0] - golden_gate[0] - 3)
            elif golden_gate:
                assembly_read = pd.read_csv(input_file, skiprows=golden_gate[0] + 1, nrows=combinations[0] - golden_gate[0] - 3)
            elif gibson:
                assembly_read = pd.read_csv(input_file, skiprows=gibson[0] + 1, nrows=combinations[0] - gibson[0] - 3)
            if assembly_read is not None:
            assembly_read.to_csv(os.path.join(path, "assembly.csv"), index=False)
            print("assembly file created successfully")

            # Read Combinations section of the CSV file
            
            combinations_read = pd.read_csv(input_file, skiprows=combinations[0] + 2)
            if combinations_read is not None:
            combinations_read.to_csv(os.path.join(path, "combinations.csv"), index=False)
            print("combination file created successfully")

            # Read Digest Linearized Pieces section of the CSV file
            digests_read = pd.read_csv(input_file, skiprows=digests[0] + 1, nrows=oligo[0] - digests[0] - 3)
            if combinations_read is not None:
            digests_read.to_csv(os.path.join(path, "digests.csv"), index=False)
            print("digest file created successfully")

    if __name__ == "__main__":
        parse_j5()
