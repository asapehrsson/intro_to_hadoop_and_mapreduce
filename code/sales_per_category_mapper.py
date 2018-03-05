#!/usr/bin/python

# Content of each line is (separated by the \t character)
# date | time | store name | item description | cost | method of payment
#
# Key is category, value is cost
# Write to standard output, separated by a tab

from base import get_stream, close_stream

inf = get_stream()

for line in inf:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(item, cost)

close_stream(inf)