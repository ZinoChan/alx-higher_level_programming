#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for n in dir(hidden_4):
        if n[0][:2] != "__":
            print(n)
