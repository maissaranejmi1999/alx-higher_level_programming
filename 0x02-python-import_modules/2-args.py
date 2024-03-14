#!/usr/bin/python3
import sys
print(len(sys.argv) - 1, "argument:")
x = 1
while x < len(sys.argv):
    print("{}: {}".format(x, sys.argv[x]))
    x += 1
