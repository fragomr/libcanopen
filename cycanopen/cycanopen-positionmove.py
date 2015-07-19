"""

purpose:
  this script starts a travel order

usage:
  python cycanopen-profilemove.py all
  python cycanopen-profilemove.py 2

prerequisits:
  the device has to be in profile position mode
  there has to be a position target

please see:
  cycanopen-402-prepare.py

"""

import sys,time
from canopen import *

canopen = CANopen(interface="can0",timeout=300)

if len(sys.argv) == 2:
    # get the node address from the first command-line argument
    if ((sys.argv[1] == "ALL") or (sys.argv[1] == "all")):
        #start 2
        value = canopen.SDODownloadExp(2, 0x6040, 0, 0x7F, 2)
        value = canopen.SDODownloadExp(2, 0x6040, 0, 0x0F, 2)
        #start 2
        value = canopen.SDODownloadExp(3, 0x6040, 0, 0x7F, 2)
        value = canopen.SDODownloadExp(3, 0x6040, 0, 0x0F, 2)
        #start 2
        value = canopen.SDODownloadExp(5, 0x6040, 0, 0x7F, 2)
        value = canopen.SDODownloadExp(5, 0x6040, 0, 0x0F, 2)
    else:
        node = int(sys.argv[1])
        #start 2
        value = canopen.SDODownloadExp(node, 0x6040, 0, 0x7F, 2)
        value = canopen.SDODownloadExp(node, 0x6040, 0, 0x0F, 2)
else:
    print("usage: %s node-nr or ALL" % sys.argv[0])
    exit(1)
