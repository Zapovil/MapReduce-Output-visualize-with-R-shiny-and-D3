#!/usr/bin/python

import sys

num_visitors = 0
current_date = None
current_ip = None
for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    new_ip, new_date = data

    if current_ip and current_ip != new_ip:
    	num_visitors += 1
    current_ip = new_ip

    if current_date and current_date != new_date:

        print "#{0}\t{1}".format(current_date, num_visitors)
	num_visitors = 0

    current_date = new_date


if current_date != None:
    print "#{0}\t{1}".format(current_date, num_visitors+1)
