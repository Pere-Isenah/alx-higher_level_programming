#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def elem_search(element):
        return element if element != search else replace
    return list(map(elem_search, my_list))
