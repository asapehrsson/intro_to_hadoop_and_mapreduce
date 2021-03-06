#!/usr/bin/python

from base import get_stream, close_stream


# The input has the format key \t value
#
# The highest value for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

def reducer():
    max_value = 0
    old_key = None
    stream = get_stream()

    for line in stream:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Skip this line.
            continue

        this_key, this_sale = data_mapped

        # special case - first key
        if old_key is None:
            old_key = this_key

        if old_key != this_key:
            print_result(max_value, old_key)
            old_key = this_key
            max_value = 0

        value = float(this_sale)

        if max_value < value:
            max_value = value

    # special case - last key
    print_result(max_value, old_key)

    close_stream(stream)


def print_result(max_value, old_key):
    print "{0}\t{1}".format(old_key, max_value)


def main():
    reducer()


if __name__ == "__main__":
    main()
