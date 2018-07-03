import os
import sys


def load_puzzle(filename):
    if not os.path.isfile(filename):
        sys.stderr.write("File '{0}' does not exist".format(filename))
        quit(-1)
    else:
        file = open(filename, 'r')
        return file
