#!/usr/bin/python3

def main():

    no_c()


def no_c(my_string):

    new_string = ""
    for x in my_string:

        if x == "c" or x == "C":

            continue
        new_string += x
    return new_string


if __name__ == "__main__":

    main()
