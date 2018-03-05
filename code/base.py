import sys


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
