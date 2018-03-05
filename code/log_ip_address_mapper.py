#!/usr/bin/python

from base import get_stream, close_stream, get_common_log_format

pattern = get_common_log_format()
inf = get_stream()

for line in inf:
    try:
        data = pattern.match(line).groups()

        if len(data) == 7:
            address, identity, username, timestamp, request, statuscode, size = data

            requestArray = request.split()
            print "{0}\t{1}".format(address, identity)

    except:
        pass

close_stream(inf)
