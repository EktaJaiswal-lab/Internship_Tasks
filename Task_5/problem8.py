# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
stamps = set()

for i in range(0,n,1):
    stamps.add(input().strip())
print(len(stamps))    
