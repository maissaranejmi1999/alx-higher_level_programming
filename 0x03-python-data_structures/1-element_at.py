#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    for i in my_list:
        if i == idx:
            print("{:d}".format(i))
    if i != idx:
        return None
