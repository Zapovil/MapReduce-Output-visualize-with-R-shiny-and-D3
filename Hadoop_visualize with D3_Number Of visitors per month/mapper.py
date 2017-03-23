#!/usr/bin/env python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data)== 10:
		ip = data[0]
		data = data[3]
		date = data[4:12]
		print '{0} \t {1}'.format(ip,date)
