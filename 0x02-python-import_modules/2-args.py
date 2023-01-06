#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv)))
    elif len(sys.argv) > 1:
        print("{} argument:".format(len(sys.argv)-1))
    for i, x in enumerate(sys.argv):
        if i == 0:

            continue
        print("{}: {}".format(i, x))
