#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary2 = {}
    for key in a_dictionary:
        a_dictionary2[key] = a_dictionary[key] * 2
    return a_dictionary2
