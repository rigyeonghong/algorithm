import sys

n = sys.stdin.readline()
a = list(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
b = list(map(int, sys.stdin.readline().split()))

a.sort()

def bs(x, arr):
    left = 0; right = len(arr)-1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    
    return (left + right) // 2

for num in b:
    idx = bs(num, a)
    if a[idx] != num :
        print(0)
    else:
        print(1)
        