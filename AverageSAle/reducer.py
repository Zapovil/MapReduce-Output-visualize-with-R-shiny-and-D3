#!/usr/bin/python

import sys

sales_total = 0
old_item = None
count_item = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    this_item, this_sale = data

    if old_item and old_item != this_item:
        print "{0}\t{1}".format(old_item, sales_total)
        sales_total = 0
	count_item = 0
    old_item = this_item
    sales_total += float(this_sale)
    count_item+=1

if old_item != None:
    print "{0}\t{1}".format(old_item, sales_total)
