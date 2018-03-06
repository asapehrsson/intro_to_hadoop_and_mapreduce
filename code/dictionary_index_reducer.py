#!/usr/bin/python

import sys

valueTotal = 0
oldKey = None

# The input has the format key \t value
# Where key is a category (store, type, etc), value is the sale amount
#
# All the sales for a particular category will be presented,
# then the key will change and we'll be dealing with the next store

index = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    key, source = data_mapped

    if not index.has_key(key):
        index[key] = []

    index[key].append(source)

for key, value in index.iteritems():
    print "{0}\t{1}".format(key, value)
