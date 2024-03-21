#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict1 = a_dictionary.copy()
    for key in dict1:
        if dict1[key] == value:
            del a_dictionary[key]
    return a_dictionary
