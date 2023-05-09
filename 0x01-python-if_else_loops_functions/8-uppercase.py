#!/usr/bin/python3
def uppercase(str):
    ans = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            ans += chr(ord(c) - (ord('a') - ord('A')))
        else:
            ans += c
    print(ans, end="\n")


