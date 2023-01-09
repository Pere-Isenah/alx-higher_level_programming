#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    divisible_elements = []

    for i in my_list:

        if i % 2 == 0:

            divisible_elements.append(True)
        else:

            divisible_elements.append(False)
    return divisible_elements
