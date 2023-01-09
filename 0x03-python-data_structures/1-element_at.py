#!/usr/bin/python3

def main():

    element_at()


def element_at(my_list, idx):

    if idx < 0:

        return "None"

    elif idx >= len(my_list):

        return "None"

    else:

        return my_list[idx]


if __name__ == "__main__":

    main()
