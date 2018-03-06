#!/usr/bin/python

from urlparse import urlparse

from base import get_stream, close_stream, get_common_log_format


def extract_path(value):
    result = ""

    array = value.split()

    if len(array) > 1:
        result = array[1]

        if result.startswith("http"):
            parsed_url = urlparse(result)

            if len(parsed_url) > 2:
                result = parsed_url[2]
            else:
                result = ""

    return result


def mapper():
    pattern = get_common_log_format()
    inf = get_stream()

    for line in inf:
        try:
            data = pattern.match(line).groups()

            if len(data) == 7:
                address, identity, username, timestamp, request, statuscode, size = data

                path = extract_path(request)

                if len(path) > 0:
                    print "{0}\t{1}".format(path, identity)

        except:
            pass

    close_stream(inf)


def main():
    mapper()


if __name__ == "__main__":
    main()
