# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    words = input_data[1:n+1]
    
    word_counts = Counter(words)
    
    print(len(word_counts))
    print(*(word_counts.values()))

if __name__ == '__main__':
    solve()