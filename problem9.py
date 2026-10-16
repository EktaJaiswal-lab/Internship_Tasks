# Problem: Python Mutations
# HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    
    return string
