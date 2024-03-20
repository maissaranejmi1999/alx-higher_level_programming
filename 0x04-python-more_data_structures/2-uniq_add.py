#!/usr/bin/python3
def uniq_add(my_list=[]):
    myset = set(my_list)
    s = 0
    for i in myset:
        s = s + i
    return s
