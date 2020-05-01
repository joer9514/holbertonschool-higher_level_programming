#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    if num is 0:
        print("{:d} arguments.".format(num))
    elif num is 1:
        print("{:d} argument:".format(num))
    else:
        print("{:d} arguments:".format(num))
    for argv in range(1, len(sys.argv)):
        print("{:d}: {}".format(argv, (sys.argv[argv])))
