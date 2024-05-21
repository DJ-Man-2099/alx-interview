#!/usr/bin/python3
""" Task 1 """


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    for char in data:
        if ((char >> 8) | 0) != 0:
            return False

    return True
