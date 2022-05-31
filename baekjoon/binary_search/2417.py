import sys
n = int(sys.stdin.readline())

l, r = 0, n

while l <= r:
    mid = (l+r) // 2
    if mid ** 2 < n:
        l = mid + 1
    else:
        r = mid -1 

print(r+1)