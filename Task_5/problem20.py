# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        blocks = deque(map(int, input().split()))
        
        last_block = float('inf')
        possible = True
        
        while blocks:
            if blocks[0] >= blocks[-1]:
                current = blocks.popleft()
            else:
                current = blocks.pop()
            if current <= last_block:
                last_block = current
            else:
                possible = False
                break
                
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()