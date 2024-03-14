#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = len(sys.argv) - 1
    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print(c, "argument:")
    else:
        print(c, "arguments:")
    x = 1
    while x < len(sys.argv):
        print("{}: {}".format(x, sys.argv[x]))
        x += 1
