#!/usr/bin/python3
"""
a script that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    '''
    function that validates a utf-8 encoding
    '''
    # Initialize the number of bytes that are expected in the current character
    expected_bytes = 0

    # Iterate through the data
    for num in data:
        # Convert the byte to a binary string representation (8 bits)
        bin_num = format(num, '08b')

        # Check the number of leading 1's in the byte
        if expected_bytes == 0:
            # If no bytes are expected,
            # determine how many bytes this character needs
            if bin_num[:3] == '110':
                expected_bytes = 1  # 2-byte character
            elif bin_num[:4] == '1110':
                expected_bytes = 2  # 3-byte character
            elif bin_num[:5] == '11110':
                expected_bytes = 3  # 4-byte character
            elif bin_num[0] == '0':
                expected_bytes = 0  # 1-byte character (ASCII)
            else:
                return False  # Invalid byte sequence
        else:
            # For continuation bytes, they must start with '10'
            if bin_num[:2] != '10':
                return False
            expected_bytes -= 1  # We've consumed one continuation byte

    # If there are still expected bytes left,
    # it means the sequence is incomplete
    return expected_bytes == 0
