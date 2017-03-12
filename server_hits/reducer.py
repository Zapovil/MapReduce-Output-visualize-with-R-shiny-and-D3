#!/usr/bin/env python

import sys

ip_address = None
ip_address_count = 0

for line in sys.stdin:
    nip_addressip_address = line.strip().split()
    if len(nip_address) != 1:
        continue

    if ip_address and ip_address != nip_address:
        print "{0}\t{1}".format(ip_address, ip_address_count)
        current_ip_address_count = 0

		ip_address = new_ip_address
		ip_address_count += 1

if ip_address != None:
    print "{0}\t{1}".format(ip_address, p_address_count)
