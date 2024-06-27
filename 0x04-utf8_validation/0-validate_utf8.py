#!/usr/bin/python3
"""
Module has a method that determines if
a given data set represents valid UTF-8 encoding
"""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else False"""
    n_bytes = 0
    for num in data:
        if n_bytes == 0:
            if num & 0b10000000:  # Check if the first bit is set
                n_bytes = 1
                mask = 0b11000000
                while mask & num:
                    n_bytes += 1
                    mask >>= 1
                if n_bytes == 1 or n_bytes > 4:
                    return False
            continue
        else:
            if not (num & 0b10000000 and not (num & 0b01000000)):
                return False
        n_bytes -= 1
    return n_bytes == 0
