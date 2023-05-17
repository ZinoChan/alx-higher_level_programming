#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    sum = 0
    prev_num = 0
    for char in reversed(roman_string):
        curr_num = roman_numerals.get(char, 0)
        if curr_num < prev_num:
            sum -= curr_num
        else:
            sum += curr_num
        prev_num = curr_num
    return sum
