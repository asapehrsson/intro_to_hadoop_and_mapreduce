#!/usr/bin/python

# Format of each line is:
# date | time | store name | item description | cost | method of payment
#
# Key is weekday, value is cost
# Write to standard output, separated by a tab
from datetime import datetime

from base import get_stream, close_stream


def mapper():
    stream = get_stream()
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    try:
        for line in stream:
            data = line.strip().split("\t")
            if len(data) == 6:
                date, time, store, item, cost, payment = data
                weekday = days[datetime.strptime(date, "%Y-%m-%d").weekday()]

                print "{0}\t{1}".format(weekday, float(cost))
    except:
        pass

    close_stream(stream)


def main():
    mapper()


if __name__ == "__main__":
    main()
