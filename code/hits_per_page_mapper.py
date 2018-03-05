#!/usr/bin/python

import re
from base import get_stream, close_stream

parts = [
    r'(?P<host>\S+)',  # host %h
    r'(?P<indent>\S+)',  # indent %l (unused)
    r'(?P<user>\S+)',  # user %u
    r'\[(?P<time>.+)\]',  # time %t
    r'"(?P<request>.*)"',  # request "%r"
    r'(?P<status>[0-9]+)',  # status %>s
    r'(?P<size>\S+)'
]

pattern = re.compile(r'\s+'.join(parts) + r'\s*\Z')

inf = get_stream()

for line in inf:
    data = pattern.match(line).groups()
    if len(data) == 7:
        address, identity, username, timestamp, request, statuscode, size = data

        requestArray = request.split()

        if len(requestArray) > 1:
            path = requestArray[1]
            print "{0}\t{1}".format(path, identity)

close_stream(inf)
