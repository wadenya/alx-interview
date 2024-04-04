#:/usr/bin/python3

"""UTF-8 Validation"""

def validUTF8(data) -> bool:
    """
    determines if a given data set represents a valid UTF-8 encoding.
    """
    numb_bytes = 0
    for byte in data:
        mask = 1 << 7
        if not num_bytes:
            while byte & mask:
                numb_bytes += 1
                mask >>= 1
            if not numb_bytes:
                continue
            if numb_bytes == 1 or numb_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        numb_bytes -= 1
    return numb_bytes == 0
