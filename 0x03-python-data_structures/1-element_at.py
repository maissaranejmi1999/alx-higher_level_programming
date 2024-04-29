#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    for i in my_list:
        if i == idx:
            break
        else:
            i = i + 1
    if i != idx:
        return None
    else:
        print("Element at index {:d} is {:d}".format(idx, i)
