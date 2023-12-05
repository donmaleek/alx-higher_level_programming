#!/usr/bin/python3

import sys

disol = len(sys.argv)
summ = 0
if __name__ == "__main__":
    if disol == 1:
        summ = 0
    else:
        for i in range(1, disol):
            summ += int(sys.argv[i])
    print("{:d}".format(summ))
