#!/usr/bin/python3

if __name__ == "__main__":
    """Python scripts that adds up all the arguments passed to it"""

    import sys

    total_sum = sum(int(arg) for arg in sys.argv[1:])

    print(total_sum)
