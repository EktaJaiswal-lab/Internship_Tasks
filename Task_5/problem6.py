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

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)