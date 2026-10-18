# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_a = set(map(int, input().split()))
num_operations = int(input())

for _ in range(num_operations):
    operation, length = input().split()
    other_set = set(map(int, input().split()))
    
    if operation == "update":
        set_a.update(other_set)
    elif operation == "intersection_update":
        set_a.intersection_update(other_set)
    elif operation == "difference_update":
        set_a.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        set_a.symmetric_difference_update(other_set)

print(sum(set_a))