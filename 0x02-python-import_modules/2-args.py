#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    print("Number of argument{}:".format("s" if argc != 1 else ""), argc, end="")
    print("." if argc == 0 else ":")
        
        for idx, arg in enumerate(argv, start=1):
            print("{}: {}".format(idx, arg))
