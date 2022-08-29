#!/bin/bash
scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Cloning/* root@robot:/data/user_storage/Cloning/.
scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Restriction/* root@robot:/data/user_storage/Restriction/
scp -r root@robot:/data/user_storage/*/*/output_*.csv /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/outputs
scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Golden_Gate/* root@robot:/data/user_storage/Golden_Gate/
scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/robotpaths.csv root@robot:/data/user_storage/
scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/output_new_pcrwell_location.csv root@robot:/data/user_storage/
scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Cloning/Input.csv root@robot:/data/user_storage/Cloning/
scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Golden_Gate/Input.csv root@robot:/data/user_storage/Golden_Gate/
scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/output_*.csv root@robot:/data/user_storage/
scp -r root@robot:/data/user_storage/output_*.csv /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/
scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Protocols/Plate_Replication/*.csv root@robot:/data/user_storage/Protocols/Plate_Replication/
