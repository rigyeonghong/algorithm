import sys
k, n = map(int, sys.stdin.readline().split())
data = [ int(sys.stdin.readline()) for _ in range(k) ]
start = 1
end = max(data)
answer = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for d in data:
        cnt += d // mid 

    if cnt < n:
        end = mid - 1
    else: # cnt >= n
        answer = mid
        start = mid + 1
print(answer)