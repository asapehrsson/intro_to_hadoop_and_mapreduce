import StringIO
import re
import sys


# open a file if given as argument
# else read from stdin
def get_stream(text=None):
    input_file = None

    if text is not None:
        return StringIO.StringIO(text)
    else:
        if len(sys.argv) == 2:
            input_file = sys.argv[1]

        if input_file:
            return open(input_file)
        else:
            return sys.stdin


# close file if it was given as input
def close_stream(inf):
    try:
        inf.close()
    except:
        pass


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
