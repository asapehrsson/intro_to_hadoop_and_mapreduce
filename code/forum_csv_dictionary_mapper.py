#!/usr/bin/python
import csv
import re

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


def print_all(index, source):
    for key, value in index.iteritems():
        print "{0}\t{1}\t{2}".format(source, key, value)


def print_no(index, source):
    for key, value in index.iteritems():
        print "{0}\t{1}".format(key, value)


def print_source(index, source):
    for key, value in index.iteritems():
        print "{0}\t{1}".format(key, source)


def mapper(what):
    stream = get_stream()
    reader = csv.reader(stream, delimiter='\t')

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

                if what == "number":
                    print_no(index, line[0])
                elif what == "source":
                    print_source(index, line[0])
                else:
                    print_all(index, line[0])
        except:
            pass

    close_stream(stream)


def main():
    mapper("no")


if __name__ == "__main__":
    main()
