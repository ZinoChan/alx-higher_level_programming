#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for n in my_list[::-1]:
        print("{}".format(n))


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
