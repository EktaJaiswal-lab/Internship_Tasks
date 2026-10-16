# Problem: Happiness
# HackerRank: https://www.hackerrank.com/challenges/happiness/problem
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    arr = input_data[2:n+2]
    
    a = set(input_data[n+2:n+2+m])
    b = set(input_data[n+2+m:n+2+2*m])
    
    happiness = sum((x in a) - (x in b) for x in arr)
    
    print(happiness)

if __name__ == '__main__':
    solve()
