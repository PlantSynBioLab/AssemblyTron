scp -r /mnt/c/Users/Public/Documents/opentrons/src/opentrons/Cloning/* root@robot:/data/user_storage/Cloning/
scp -r /mnt/c/Users/Public/Documents/opentrons/src/opentrons/Restriction/* root@robot:/data/user_storage/Restriction/
scp -r root@robot:/data/user_storage/*/*/output_*.csv /mnt/c/Users/Public/Documents/opentrons/src/opentrons/outputs

scp -r /mnt/c/Users/Public/Documents/opentrons/src/opentrons/Golden_Gate/* root@robot:/data/user_storage/Golden_Gate/
scp -r /mnt/c/Users/Public/Documents/opentrons/src/opentrons/robotpaths.csv root@robot:/data/user_storage/

scp -r /mnt/c/Users/Public/Documents/opentrons/src/opentrons/output_new_pcrwell_location.csv root@robot:/data/user_storage/
scp -r /mnt/c/Users/Public/Documents/opentrons/src/opentrons/Cloning/Input.csv root@robot:/data/user_storage/Cloning/

scp -r /mnt/c/Users/Public/Documents/opentrons/src/opentrons/Golden_Gate/Input.csv root@robot:/data/user_storage/Golden_Gate/

scp -r /mnt/c/Users/Public/Documents/opentrons/src/opentrons/output_*.csv root@robot:/data/user_storage/
scp -r root@robot:/data/user_storage/output_*.csv /mnt/c/Users/Public/Documents/opentrons/src/opentrons/

scp -r /mnt/c/Users/Public/Documents/opentrons/src/opentrons/Protocols/Plate_Replication/*.csv root@robot:/data/user_storage/Protocols/Plate_Replication/
