#!/usr/bin/env python
#
#
import sys
for i in sys.stdin.readlines():
    ip,val = i[:-1].split()
    s = int(float(val)*32) + 1
    if s > 31:
        s = 31
    for k in range(0,s):
        print("%s.%d" % ('.'.join(ip.split('.')[0:3]),s))
