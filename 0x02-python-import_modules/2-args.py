#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    argv = sys.argv[1:]

    print("{:d} argument{}{}{}".format(argc,
        's' if argc != 1 else '',
        '' if argc == 0 else ':',
        '' if argc == 0 else '\n'))

    for i, arg in enumerate(argv, start=1):
        print("{:d}: {:s}".format(i, arg))
