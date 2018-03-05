#!/usr/bin/python

# Format of each line is:
# date | time | store name | item description | cost | method of payment
#
# Key is store name, value is cost
# Write to standard output, separated by a tab

from base import get_stream, close_stream

inf = get_stream()

for line in inf:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)

close_stream(inf)