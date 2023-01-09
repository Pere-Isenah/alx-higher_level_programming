#!/usr/bin/python3

def main():

    print_reversed_list_integer()


def print_reversed_list_integer(my_list=[]):

    for x in my_list[::-1]:
        print("{}".format(x))


if __name__ == "__main__":

    main()
