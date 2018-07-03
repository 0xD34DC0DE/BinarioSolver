import sys
import numpy as np


# Decode the the data in the file and return array with usable data
def decode_file(file):
    # Remove newLines and whitespaces
    lines = [line.rstrip('\n').replace(' ', '') for line in file]
    # Convert list of strings to list of integer and replace character '.' by -1
    decoded = [list(map(lambda c: -1 if c == '.' else int(c), list(charlist))) for charlist in lines]
    # Add 1 to every number
    normalized = [list(map(lambda x: x + 1, row)) for row in decoded]
    shaped = np.array(normalized)
    return shaped

