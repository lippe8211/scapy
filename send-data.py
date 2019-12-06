#!/usr/bin/env python
import sys
from scapy.all import *

try:
    traceHost = str(sys.argv[1])
except IndexError as error:
    print("Start script with\n" + sys.argv[0] + " <host> ")
    sys.exit(1)

r2, unans = tr2, unans = traceroute([traceHost], maxttl=20)
