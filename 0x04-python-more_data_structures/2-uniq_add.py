#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    s = set()
    for n in my_list:
        if n not in s:
            sum += n
            s.add(n)
    return sum
