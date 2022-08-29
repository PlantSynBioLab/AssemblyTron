bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Cloning/* root@robot:/data/user_storage/Cloning/"
bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Restriction/* root@robot:/data/user_storage/Restriction/"
bash -c "scp -r root@robot:/data/user_storage/*/*/output_*.csv /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/outputs"

bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Golden_Gate/* root@robot:/data/user_storage/Golden_Gate/"
bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/robotpaths.csv root@robot:/data/user_storage/"

bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/output_new_pcrwell_location.csv root@robot:/data/user_storage/"
bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Cloning/Input.csv root@robot:/data/user_storage/Cloning/"

bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Golden_Gate/Input.csv root@robot:/data/user_storage/Golden_Gate/"

bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/output_*.csv root@robot:/data/user_storage/"
bash -c "scp -r root@robot:/data/user_storage/output_*.csv /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/"

bash -c "scp -r /mnt/c/Users/Public/Documents/opentrons/src/DNA-AssemblyLine/Protocols/Plate_Replication/*.csv root@robot:/data/user_storage/Protocols/Plate_Replication/"

pause