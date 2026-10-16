# Problem: Find the Runner-Up Score!
# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maximum = float("-inf")
    sec_max = float("-inf")
    l = len(arr)
    for i in range(0,n):
        maximum = max(maximum,arr[i])
    for i in range(0,n):
        if arr[i] > sec_max and arr[i] != maximum: 
            sec_max = arr[i]    
    print(sec_max)
