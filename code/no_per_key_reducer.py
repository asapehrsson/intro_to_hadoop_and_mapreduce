#!/usr/bin/python

import sys

totalHit = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, other = data_mapped

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, totalHit)
        oldKey = thisKey
        totalHit = 0

    oldKey = thisKey
    totalHit += 1

if oldKey is not None:
    print "{0}\t{1}".format(oldKey, totalHit)
