#!/usr/bin/python3

def multiple_returns(sentence):
    """A function that returns a tuple of its length"""
    if sentence == "":
        return (0, None)
    return(len(sentence), sentence[0])