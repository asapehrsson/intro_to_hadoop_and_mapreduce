import sys
import re


# open a file if given as argument
# else read from stdin
def get_stream():
    file_name_given = None

    if len(sys.argv) == 2:
        file_name_given = sys.argv[1]

    if file_name_given:
        return open(file_name_given)
    else:
        return sys.stdin


# close file if it was given as input
def close_stream(inf):
    if inf is not sys.stdin:
        inf.close()


def get_common_log_format():
    parts = [
        r'(?P<host>\S+)',  # host %h
        r'(?P<indent>\S+)',  # indent %l (unused)
        r'(?P<user>\S+)',  # user %u
        r'\[(?P<time>.+)\]',  # time %t
        r'"(?P<request>.*)"',  # request "%r"
        r'(?P<status>[0-9]+)',  # status %>s
        r'(?P<size>\S+)'
    ]

    pattern = re.compile(r'\s+'.join(parts) + r'\s*\Z')
    return pattern
