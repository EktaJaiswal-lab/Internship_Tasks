# Problem: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem
from collections import OrderedDict

def solve():
    n = int(input().strip())
    word_counts = OrderedDict()
    
    for _ in range(n):
        word = input().strip()
        word_counts[word] = word_counts.get(word, 0) + 1
        
    print(len(word_counts))
    print(*(word_counts.values()))

if __name__ == '__main__':
    solve()
