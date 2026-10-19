#!/bin/python3

import math
import os
import random
import re
import sys

def separateNumbers(s):
    n = len(s)
    
    for i in range(1, n // 2 + 1):
       
        sub_str = s[:i]
        
       
        if sub_str[0] == '0' and len(sub_str) > 1:
            continue
            
        num = int(sub_str)
        first_num = num
        
        
        built = str(num)
        while len(built) < n:
            num += 1
            built += str(num)
            
        
        if built == s:
            print(f"YES {first_num}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        separateNumbers(s)