#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    
    s = float("-inf")
    for key in a_dictionary:
        if a_dictionary[key] >= s:
            s = a_dictionary[key]
    return s
