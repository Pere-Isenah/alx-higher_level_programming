#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    b = 0
    for x in sys.argv[1::]:
        b += int(x)
    print(b)
