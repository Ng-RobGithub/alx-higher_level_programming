#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{:c}".format(i + ord('a')), end="")
    if i > 0:
        print("{:c}".format(i + ord('A')), end="")

        print()
