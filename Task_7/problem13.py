#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter  # <--- Add this import

def isValid(s):
    # Write your code here
    char_counts = Counter(s)
    
    freq_counts = Counter(char_counts.values())
    
    if len(freq_counts) == 1:
        return "YES"
    
    if len(freq_counts) > 2:
        return "NO"
    
    freqs = list(freq_counts.keys())
    f1, count1 = freqs[0], freq_counts[freqs[0]]
    f2, count2 = freqs[1], freq_counts[freqs[1]]
    
    if (f1 == 1 and count1 == 1) or (f2 == 1 and count2 == 1):
        return "YES"
        
    if (abs(f1 - f2) == 1) and (count1 == 1 or count2 == 1):
        if (f1 > f2 and count1 == 1) or (f2 > f1 and count2 == 1):
            return "YES"
            
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()