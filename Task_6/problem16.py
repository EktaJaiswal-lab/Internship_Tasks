# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a_size = int(input())
    set_a = set(map(int, input().split()))
    b_size = int(input())
    set_b = set(map(int, input().split()))
    
    print(set_a.issubset(set_b))