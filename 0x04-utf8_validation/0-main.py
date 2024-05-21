#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

# 4 Bytes valid
data = [0b11110000, 0b10000000, 0b10000000, 0b10000000]
print(validUTF8(data))

data = [0b11110000, 0b10000000, 0b10000000, 0b11000000]
print(validUTF8(data))

# 3 Bytes valid
data = [0b11100000, 0b10000000, 0b10000000]
print(validUTF8(data))

data = [0b11100000, 0b10000000, 0b11000000]
print(validUTF8(data))

# 2 Bytes valid
data = [0b11000010, 0b10000010]
print(validUTF8(data))

# 1 Byte valid
data = [0b0101]
print(validUTF8(data))

# empty dataset valid
data = []
print(validUTF8(data))

# 4,3 Bytes valid
data = [0b11110000, 0b10000000, 0b10000000,
        0b10000000, 0b11100000, 0b10000000, 0b10000000]
print(validUTF8(data))
