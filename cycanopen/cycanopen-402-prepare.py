"""

purpose:
  this script prepares a device for a travel order

usage:
  python cycanopen-402-prepare.py 2

prerequisits:
  devices must be turned on
  can-bus is on can0

please see:
  cycanopen-profilemove.py

"""

import sys,time
from canopen import *

def tryread():
    try:
        f = canopen.read_frame()
        print "reply: ",
        f.dump()
        return f
    except Exception:
        print "** no reply **"

if len(sys.argv) == 2:
    # get the node address from the first command-line argument
    node = int(sys.argv[1])
else:
    print("usage: %s NODE" % sys.argv[0])
    exit(1)

canopen = CANopen(interface="can0",timeout=300)

#from canopen.pxd
"""
int CANOPEN_NMT_MC_CS_START          # 0x01
#define CANOPEN_NMT_MC_CS_START_STR      "Start remote node"
int CANOPEN_NMT_MC_CS_STOP           # 0x02
#define CANOPEN_NMT_MC_CS_STOP_STR       "Stop remote node"
int CANOPEN_NMT_MC_CS_PREOP          # 0x80
#define CANOPEN_NMT_MC_CS_PREOP_STR      "Enter pre-operation state"
int CANOPEN_NMT_MC_CS_RESET_APP      # 0x81
#define CANOPEN_NMT_MC_CS_RESET_APP_STR  "Reset application"
int CANOPEN_NMT_MC_CS_RESET_COM      # 0x82
#define CANOPEN_NMT_MC_CS_RESET_COM_STR  "Reset communication"
"""

#TODO investigate why nanotec behaves differently than maxon
if ((node==2) or (node==3)):
    canopen.nmt_send(node, 0x81) # reset
    tryread()
    canopen.nmt_send(node, 0x01) # start
    tryread()

#value = canopen.SDODownloadExp(7, 0x6040, 0, 1, 1)
#  can0  607   [8]  2F 40 60 00 01 00 00 00
#value = canopen.SDODownloadExp(7, 0x6040, 0, 1, 2)
#  can0  607   [8]  2B 40 60 00 01 00 00 00
#value = canopen.SDODownloadExp(7, 0x6040, 0, 1, 3)
#  can0  607   [8]  27 40 60 00 01 00 00 00
#value = canopen.SDODownloadExp(7, 0x6040, 0, 1, 4)
#  can0  607   [8]  23 40 60 00 01 00 00 00

value = canopen.SDOUploadExp(node, 0x6041, 0)
print("6041:  = 0x%.8x\n" % value)
#  can0  605   [4]  40 41 60 00
#  can0  585   [8]  4B 41 60 00 40 02 00 00


value = canopen.SDODownloadExp(node, 0x6060, 0, 0x01, 1)
#  can0  605   [8]  2F 60 60 00 01 00 00 00
#  can0  585   [8]  60 60 60 00 00 00 00 00
#  can0  185   [6]  40 06 00 00 00 00

value = canopen.SDODownloadExp(node, 0x6040, 0, 0x06, 2)
#  can0  605   [8]  2B 40 60 00 06 00 00 00
#  can0  585   [8]  60 40 60 00 00 00 00 00
#  can0  185   [6]  21 06 00 00 00 00

value = canopen.SDODownloadExp(node, 0x6040, 0, 0x07, 2)
#  can0  605   [8]  2B 40 60 00 07 00 00 00
#  can0  585   [8]  60 40 60 00 00 00 00 00
#  can0  185   [6]  33 06 00 00 00 00

value = canopen.SDODownloadExp(node, 0x6040, 0, 0x0F, 2)
#  can0  605   [8]  2B 40 60 00 0F 00 00 00
#  can0  585   [8]  60 40 60 00 00 00 00 00
#  can0  185   [6]  37 06 00 00 00 00

value = canopen.SDODownloadExp(node, 0x607A, 0, 0x3E80, 4)
#  can0  605   [8]  23 7A 60 00 80 3E 00 00
#  can0  585   [8]  60 7A 60 00 00 00 00 00

print("Startup done for node 0x%.2x ready for a profile position move" % node )
