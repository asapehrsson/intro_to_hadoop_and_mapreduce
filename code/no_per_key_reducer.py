#!/usr/bin/python

from base import get_stream, close_stream


def reducer():
    stream = get_stream()
    total_hit = 0
    old_key = None

    for line in stream:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Skip this line.
            continue

        this_key, other = data_mapped

        # special case - first key
        if old_key is None:
            old_key = this_key

        if old_key != this_key:
            print_result(old_key, total_hit)
            old_key = this_key
            total_hit = 0

        total_hit += 1

    # special case - last key
    print_result(old_key, total_hit)

    close_stream(stream)


def print_result(old_key, total_hit):
    print "{0}\t{1}".format(old_key, total_hit)


def main():
    reducer()


if __name__ == "__main__":
    main()
