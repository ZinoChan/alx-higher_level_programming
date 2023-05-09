#!/usr/bin/python3
for chr in range(97, 123):
    if chr != 101 or chr != 113:
        print("{:c}".format(chr), end='')
