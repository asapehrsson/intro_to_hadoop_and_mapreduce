#!/usr/bin/python

from base import get_stream, close_stream


# The input has the format key \t value
#
# Each key will hold all related values

def reducer():
    stream = get_stream()
    old_key = None
    hours = [0] * 24

    for line in stream:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Skip this line.
            continue

        this_key, this_hour = data_mapped

        # special case - first key
        if old_key is None:
            old_key = this_key

        if old_key != this_key:
            print_result(hours, old_key)
            old_key = this_key
            hours = [0] * 24

        hour = int(this_hour)

        if -1 < hour < len(hours):
            hours[hour] += 1

    print_result(hours, old_key)
    close_stream(stream)


def print_result(hours, old_key):
    result = []
    for i in range(0, len(hours)):
        result.append([hours[i], i])

    result.sort(key=lambda l: l[0], reverse=True)

    max_value = result[0][0]

    if max_value > 0:
        for post in result:
            if post[0] == max_value:
                print "{0}\t{1}".format(old_key, post[1])
            else:
                break


def main():
    reducer()


if __name__ == "__main__":
    main()
