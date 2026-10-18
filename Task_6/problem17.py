# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())

n = int(input())

is_strict_superset = True
for _ in range(n):
    other_set = set(input().split())
    if not (a.issuperset(other_set) and a > other_set):
        is_strict_superset = False
        break

print(is_strict_superset)