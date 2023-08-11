#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    print("{:d} argument{}{}:".format(argc, "" if argc == 1 else "s", "" if argc == 0 else ":", "\n" if argc > 0 else "."))

    for i, arg in enumerate(argv, start=1):
        print("{:d}: {}".format(i, arg))
