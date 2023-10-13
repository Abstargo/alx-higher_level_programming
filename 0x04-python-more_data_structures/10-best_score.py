#!/usr/bin/python3

def best_score(a_dictionary):
    """Write a function that returns a key with the biggest integer"""

    if a_dictionary:
        return (max(a_dictionary, key=a_dictionary.get))
    return (None)
