#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    r = s[::-1]
    s_diff = [abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)]
    r_diff = [abs(ord(r[i]) - ord(r[i + 1])) for i in range(len(r) - 1)]
    
    if s_diff == r_diff:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
