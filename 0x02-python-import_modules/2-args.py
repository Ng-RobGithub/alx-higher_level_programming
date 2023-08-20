#!/usr/bin/python3

import sys

if __name__ == "__main__":
    size = len(sys.argv) - 1

    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(size))

        for i in range(size):
            print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
