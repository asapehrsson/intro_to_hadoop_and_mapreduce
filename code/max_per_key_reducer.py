#!/usr/bin/python

import sys

maxValue = 0
oldKey = None

# The input has the format key \t value
#
# The highest value for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, maxValue)
        oldKey = thisKey
        maxValue = 0

    oldKey = thisKey
    value = float(thisSale)

    if maxValue < value:
        maxValue = value

if oldKey is not None:
    print "{0}\t{1}".format(oldKey, maxValue)
