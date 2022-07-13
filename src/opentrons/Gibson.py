def get_values(*names):
    import json
    _all_values = json.loads("""{"right_pipette":"p100_single_gen2","left_pipette":"p10_single_gen2","master_mix_csv":"Reagent,Slot,Well,Volume\\nGibson,1,A1,15\\nMgCl,1,A2,0.5\\nDNA1,1,A3,vDNA1\\nDNA1,1,A4,vDNA2\\nwater,1,A5,vwater\\n"}""")
    return [_all_values[n] for n in names]
#in line 3 the values for the volumes of water and each fragment change based on the concentration and the length of the fragment
#The term A5 designates which well and placement of the solution in question
#Return inputs from J5 to get volumes
metadata = {
    'protocolName': 'Gibson Assembly',
    'author': 'Eric Zirkle',
    'source': 'Protocol Library',
    'apiLevel': '2.2'
}

def run(protocol_context):
    
    # Setup pipettes
    [left_pipette, right_pipette, master_mix_csv] = get_values(
        "left_pipette", "right_pipette", "master_mix_csv")

    if not left_pipette and not right_pipette:
        raise Excption('You have to select at least 1 pipette.')

    pipette_l = None
    pipette_r = None
    
     # determine which pipette has the smaller volume range
    if pipette_l and pipette_r:
        if left_pipette == right_pipette:
            pip_s = pipette_l
            pip_l = pipette_r
        else:
            if pipette_l.max_volume < pipette_r.max_volume:
                pip_s, pip_l = pipette_l, pipette_r
            else:
                pip_s, pip_l = pipette_r, pipette_l
    else:
        pipette = pipette_l if pipette_l else pipette_r
        
    # specify the labware being used


    reagents_rack = protocol_context.load_labware(
        'opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',
        '1',
        'snapcap 2ml tuberack'
    )

    # rack of mastermix
    fragment_rack = protocol_context.load_labware(
        'strip_tube_rack', # define a 96 well strip-tube rack
        '2',
        'screwcap 2ml tuberack'
    )

    # rack of assembly pieces 
    fragment_rack = protocol_context.load_labware(
        'strip_tube_rack', # define a 96 well strip-tube rack
        '3',
        'screwcap 2ml tuberack'
    )
    
    reagents = {
        '2': screwrack,
        '3': res12
    }    
    #destination of final solution
    mastermix_dest = res12.wells()[A6]
    
    #The next section of code needs to establish the volume and source
    #This section comes from the PCR protocol, I am unsure what it actually does
    info_list = [
        [cell.strip() for cell in line.split(',')]
        for line in master_mix_csv.splitlines()[1:] if line
    ]
    # 
    for line in info_list[1:]:
        #recalling the data from line 3, specifically the volume and location from the create data set in that line
        source = reagents[line[1]].wells(line[2].upper())
        vol = float(line[3])
        if pipette_l and pipette_r:
            if vol <= pip_s.max_volume:
                pipette = pip_s
            else:
                pipette = pip_l
#the final transfer, the volume and source are pulled from the third line, teh destination is specified in line 43
        pipette.transfer(vol, source, mastermix_dest)