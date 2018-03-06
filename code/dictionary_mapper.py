#!/usr/bin/python
import re
import csv
from base import get_stream, close_stream


def clean(part):
    result = re.sub('[^a-zA-Z]+', '', part)
    result = result.lower()
    return result


def prepare(body):
    # split into substrings
    result = re.split(r'[#=/-;!.?,\s]\s*', body)
    if len(result) > 1:
        # remove unwanted characters
        result = map(clean, result)

    return result


stream = get_stream()
reader = csv.reader(stream, delimiter='\t')


def print_all(index, line):
    for key, value in index.iteritems():
        print "{0}\t{1}\t{2}".format(line[0], key, value)


def print_no(index, line):
    for key, value in index.iteritems():
        print "{0}\t{1}".format(key, value)


def print_source(index, line):
    for key, value in index.iteritems():
        print "{0}\t{1}".format(key, line[0])


for line in reader:
    try:
        if len(line) > 4:
            body = line[4]

            # remove html markup
            body = re.sub('<[^<]+?>', '', body)
            parts = prepare(body)

            index = {}
            for part in parts:
                if len(part) > 0:
                    if index.has_key(part):
                        index[part] += 1
                    else:
                        index[part] = 1

            print_source(index, line)

    except:
        pass

close_stream(stream)
