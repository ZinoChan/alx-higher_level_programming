#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argv_len = len(argv) - 1
    if argv_len > 1:
        print(argv_len, "arguments:")
        for idx in range(1, argv_len + 1):
            print("{:d}: {}".format(idx, argv[idx]))
    elif argv_len == 1:
        print(argv_len, "argument:")
        for idx in range(1, argv_len + 1):
            print("{:d}: {}".format(idx, argv[idx]))
    elif argv_len == 0:
        print(argv_len, "argumentns.")
