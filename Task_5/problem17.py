# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    
    arr = list(map(int, input_data[2:n+2]))
    
    A = set(map(int, input_data[n+2:n+2+m]))
    B = set(map(int, input_data[n+2+m:n+2+2*m]))
    
    happiness = sum((1 if x in A else -1 if x in B else 0) for x in arr)
    
    print(happiness)

if __name__ == '__main__':
    solve()