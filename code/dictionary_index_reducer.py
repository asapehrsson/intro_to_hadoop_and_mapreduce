#!/usr/bin/python

from base import get_stream, close_stream


# The input has the format key \t value
#
# Each key will hold all related values

def reducer():
    stream = get_stream()
    index = {}

    for line in stream:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Skip this line.
            continue

        key, source = data_mapped

        if key not in index:
            index[key] = []

        index[key].append(source)

    for key, value in index.iteritems():
        print "{0}\t{1}".format(key, value)

    close_stream(stream)


def main():
    reducer()


if __name__ == "__main__":
    main()
