#!/usr/bin/python3
"""
Module has a method that determines if
a given data set represents valid UTF-8 encoding
"""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else False"""
    n_bytes = 0
    for num in data:
        mask1 = 1 << 7
        if n_bytes == 0:
            mask = 1 << 7
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & (1 << 6))):
                return False
        n_bytes -= 1
    return n_bytes == 0
