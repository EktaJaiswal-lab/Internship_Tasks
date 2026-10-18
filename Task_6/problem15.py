# Enter your code here. Read input from STDIN. Print output to STDOUT
n_english = int(input())
english_roll_numbers = set(map(int, input().split()))

n_french = int(input())
french_roll_numbers = set(map(int, input().split()))

only_english = english_roll_numbers.difference(french_roll_numbers)

print(len(only_english))