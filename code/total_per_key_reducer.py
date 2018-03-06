#!/usr/bin/python

from base import get_stream, close_stream

# The input has the format key \t value
# Where key is a category (store, type, etc), value is the sale amount
#
# All the sales for a particular category will be presented,
# then the key will change and we'll be dealing with the next store

test_text = """alfa\t5
alfa\t7
beta\t3.0
beta\t1 
"""


def reducer():
    value_total = 0
    old_key = None

    stream = get_stream()
    for line in stream:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Skip this line.
            continue

        this_key, this_value = data_mapped

        if old_key is None:
            old_key = this_key

        if old_key != this_key:
            print "{0}\t{1}".format(old_key, value_total)
            old_key = this_key
            value_total = 0

        value_total += float(this_value)

    print "{0}\t{1}".format(old_key, value_total)

    close_stream(stream)


def main():
    reducer()


if __name__ == "__main__":
    main()
