# Problem: Captain's Room
# HackerRank: https://www.hackerrank.com/challenges/captaing-room/problem
def average(array):
    # your code goes here
    my_set= list(set(array))
    #print(my_set)
    Total = 0
    l = len(my_set)
    for i in range(0,l,1):
        Total += my_set[i]
    avg = Total/l
    return avg  

arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
result = average(arr)
print(result)
