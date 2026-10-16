# Problem: Set Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

result = sorted(a ^ b)

for num in result:
    print(num)