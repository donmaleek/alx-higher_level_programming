#!/usr/bin/python3

import sys

if __name__ == "__main__":
    dumbed = len(sys.argv)

    if dumbed == 1:
        print("{:d} arguments.".format(dumbed - 1))
    elif dumbed == 2:
        print("{:d} argument:".format(dumbed - 1))
    else:
        print("{:d} arguments:".format(dumbed - 1))
    for i in range(1, dumbed):
        print("{:d}: {:s}".format(i, sys.argv[i]))
