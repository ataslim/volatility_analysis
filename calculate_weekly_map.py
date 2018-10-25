import sys
import os
import socket
import struct

def read_set_file(sf_n):
    result = set()
    line_count = 0 
    with os.popen('rwsetcat %s' % sf_n,'r') as data_pipe:
        for line in data_pipe.readlines():
            line_count += 1
            if(line_count % 10000 == 0):
                sys.stderr.write('.')
                sys.stderr.flush()
            result.add(line[:-1])
        data_pipe.close()
        sys.stderr.write('\n')
    return result

def calc_distance(a,b,limit):
    # distance is the number of elements that differ between the
    # two sets -- hamming distance
    intersect = a.intersection(b)
    s1 = len(a.difference(intersect))
    s2 = len(b.difference(intersect))
    return((s1 + s2)/limit)

def aggregate_set_elements(sf_n, prefix_length):
    results = {}
    proto_mask = 0xFFFFFFFF
    mask = 0xFFFFFFFF & (
        (proto_mask >> (32 - prefix_length)) << (32 - prefix_length))
    complement = 0xFFFFFFFF - mask
    for i in sf_n:
        ip_as_int = struct.unpack('!L',socket.inet_aton(i))[0]
        masked_ip = ip_as_int & mask
        stringed_ip = socket.inet_ntoa(struct.pack('!L',masked_ip))
        # Now generate a vector
        offset = ip_as_int & complement
        if not stringed_ip in results:
            results[stringed_ip] = set([offset])
        else:
            results[stringed_ip].add(offset)
    return results

if __name__ == '__main__':
    mask = int(sys.argv[1])
    s1 = sys.argv[2]
    s2 = sys.argv[3]
    map_1 = aggregate_set_elements(read_set_file(s1), mask)
    sys.stderr.write("Read map 1, %d elements" % len(map_1))
    map_2 = aggregate_set_elements(read_set_file(s2), mask)
    sys.stderr.write("Read map 1, %d elements" % len(map_1))
    limit =  2**(32 - mask)
    keys = set(map_1.keys())
    keys = keys.union(set(map_2.keys()))
    for element in keys:
        if not element in map_1:
            s1 = set([])
        else:
            s1 = map_1[element]
        if not element in map_2:
            s2 = set([])
        else:
            s2 = map_2[element]
        print("%s %f" % (element, calc_distance(s1,s2,limit)))
            
