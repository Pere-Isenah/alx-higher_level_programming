#!/usr/bin/python3

def main():

    print_list_integer()


def print_list_integer(my_list=[]):

    for x in my_list:

        print("{:d}".format(x))


if __name__ == "__main__":

    main()
