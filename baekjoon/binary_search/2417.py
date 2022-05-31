import sys
n = int(sys.stdin.readline())

l, r = 0, n

while True:
    mid = (l+r) // 2
    if r < l:
        break
    if mid ** 2 < n:
        l = mid + 1
    else:
        r = mid -1 

print(r+1)