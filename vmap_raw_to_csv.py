#!/usr/bin/env python
import csv, sys

header=['netblock','volatility']
writer = csv.DictWriter(sys.stdout, fieldnames=header)
writer.writeheader()
for i in sys.stdin.readlines(): 
    block,volatility = i[:-1].split(' ')[0:2]
    writer.writerow({'netblock':block,'volatility': volatility})
