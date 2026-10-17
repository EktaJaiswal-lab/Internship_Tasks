# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

result = sorted(a ^ b)

for num in result:
    print(num)
