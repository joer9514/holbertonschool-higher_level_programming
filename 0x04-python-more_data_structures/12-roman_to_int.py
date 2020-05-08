#!/usr/bin/python3
def roman_to_int(roman_string):
    last = 0
    number = 0
    convert_to_int = [
        ['I', 1],
        ['V', 5],
        ['X', 10],
        ['L', 50],
        ['C', 100],
        ['D', 500],
        ['M', 1000]
    ]
    if type(roman_string) != str or roman_string is None:
        return 0
    for i in roman_string:
        for j in convert_to_int:
            if i == j[0]:
                if last == 0 or last >= j[1]:
                    number += j[1]
                elif last < j[1]:
                    number += j[1] - last * 2
                last = j[1]
    return(number)
