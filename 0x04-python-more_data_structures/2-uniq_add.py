#!/usr/bin/python3
def uniq_add(my_list=[]):
    counter = 0
    for i in set(my_list):
        counter += i
    return (counter)
