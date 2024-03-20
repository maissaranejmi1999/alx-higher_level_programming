#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    diction = sorted(a_dictionary)
    for key in diction:
        print(key, ":", a_dictionary.get(key))
