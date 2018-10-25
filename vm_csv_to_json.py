#!/usr/bin/env python
#
# 
import json
import random
import time

def generate_random_network():
    dt = time.strftime("%Y/%m/%d",time.gmtime(time.time()))
    address = "%d.%d.%d.0" % (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    block=24
    change = random.randint(0,1000)
    return {('%s' % address): {'block':block, 'date': dt,'vty': change}}

if __name__ == '__main__':
    results = []
    for i in range(0,20):
        results.append(generate_random_network())
    print(json.dumps(results))
