#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    j = 0
    for i in my_list:
        if j == idx:
            print("Element at index {:d} is {:d}".format(idx, i))
            break
        else:
            i = i + 1
            j = j + 1
    if j != idx:
        return None
