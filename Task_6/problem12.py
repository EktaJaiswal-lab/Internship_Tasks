n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    parts = input().split()
    command = parts[0]
    if command == "pop":
        s.pop()
    elif command == "remove":
        s.remove(int(parts[1]))
    elif command == "discard":
        s.discard(int(parts[1]))

print(sum(s))