# The new static IP address (and subnet mask) for your OT-2.
#
# You should choose an address from a private range that you control, like
# 10.x.x.x/8 or 192.168.x.x/16.
STATIC_IP = "169.254.231.53/16"


#################################################################
# You shouldn't normally need to edit anything below this line. #
#################################################################
## WIRED IP

import os
from pathlib import Path
from opentrons import protocol_api

# A human-readable name to identify this connection configuration. May appear in
# logs, etc.
CONNECTION_ID = "support-team-wired-static-ip"

# Note, in case you're looking to manually remove this file to undo the work of
# this script: other versions called it "support-wired-static-ip".
CONNECTION_FILE_NAME = "support-team-wired-static-ip"

# See:
# https://developer.gnome.org/NetworkManager/stable/nm-settings-keyfile.html
KEYFILE_CONTENTS = f"""\
# This configuration file was added here with the help of Opentrons Support.
# OT-2s don't normally come with it, out of the factory.
#
# Normally, factory-installed NetworkManager configurations assign the OT-2's
# wired IP address dynamically. The presence of this extra configuration file
# overrides those to instead set a known, static wired IP address.
#
# This can be useful for working around issues with mDNS, or for using the OT-2
# in a network without relying on DHCP.
[connection]
id={CONNECTION_ID}
type=ethernet
autoconnect-priority=20
interface-name=eth0
permissions=
[ethernet]
cloned-mac-address=permanent
mac-address-blacklist=
[ipv4]
dns-search=
method=manual
addresses={STATIC_IP}
"""

KEYFILE_PATH = Path("/var/lib/NetworkManager/system-connections") / CONNECTION_FILE_NAME

metadata = {'apiLevel': '2.0'}

def run(protocol: protocol_api.ProtocolContext):
    protocol.comment(f"Run this protocol to set your OT-2's IP address to {STATIC_IP}.")

    if not protocol.is_simulating():
        KEYFILE_PATH.write_text(KEYFILE_CONTENTS)
        os.sync()
        protocol.comment("Done.")

        protocol.comment("Restart your OT-2 to apply the changes.")
