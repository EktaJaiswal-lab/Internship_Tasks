#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    # Write your code here
    changes = 0
    i = 0
    n = len(b)
    
    while i <= n - 3:
        if b[i:i+3] == "010":
            changes += 1
            # Skip the next 2 characters since we fixed this '010' 
            # by changing the character at i + 2
            i += 3
        else:
            i += 1
            
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
