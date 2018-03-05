#!/usr/bin/python

import sys

salesTotal = 0
noOfSales = 0

# Just sum everything

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    salesTotal += float(thisSale)
    noOfSales += 1


print noOfSales, "\t", salesTotal

