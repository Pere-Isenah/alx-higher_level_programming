#!/usr/bin/python3

def main():

    max_integer()


def max_integer(my_list=[]):

    if not my_list:
        return None
    max_value = my_list[0]
    for i in my_list:
        if i > max_value:
            max_value = i
    return max_value


if __name__ == "__main__":

    main()
