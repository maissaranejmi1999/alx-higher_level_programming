#!/usr/bin/python3
def best_score(a_dictionary):
    s = 0
    if a_dictionary is None:
        return None
    for key in a_dictionary:
        if a_dictionary[key] >= s:
            s = a_dictionary[key]
    return s
