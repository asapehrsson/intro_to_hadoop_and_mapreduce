#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import re

from base import get_stream, close_stream


def clean(part):
    result = re.sub('[^a-zA-ZåäöÅÄÖ]+', '', part)
    result = result.lower()
    return result


def prepare(body):
    # split into substrings
    result = re.split(r'[#=/-;!.?,\s]\s*', body)
    if len(result) > 1:
        # remove unwanted characters
        result = map(clean, result)

    return result


def mapper():
    stream = get_stream()

    for line in stream:
        try:
            parts = prepare(line)
            for part in parts:
                if len(part) > 0:
                    print "{0}\t{1}".format(part, 1)

        except:
            pass

    close_stream(stream)


def main():
    mapper()


if __name__ == "__main__":
    main()
