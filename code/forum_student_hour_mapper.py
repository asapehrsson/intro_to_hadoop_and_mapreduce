#!/usr/bin/python

import csv
from datetime import datetime

from base import get_stream, close_stream


def mapper():
    stream = get_stream()
    reader = csv.reader(stream, delimiter='\t')

    for line in reader:
        if len(line) > 9:
            # just pick the first 10 elements
            post_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at = line[:9]
            try:
                date_time = get_date_time(added_at)

                print "{0}\t{1}".format(author_id, date_time.hour)
            except ValueError:
                print("Skipping line")

    close_stream(stream)


def get_date_time(value):
    return datetime.strptime(value[0:25], '%Y-%m-%d %H:%M:%S.%f')


def main():
    mapper()


if __name__ == "__main__":
    main()
