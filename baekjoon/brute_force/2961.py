import sys
from itertools import combinations

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

com = []
for i in range(1, N+1):
    com.append(combinations(data, i))

answer = 1000000000
for line in com:
    for each in line:
        print(each)
        s = 1
        b = 0
        for e in each:
            s *= e[0]
            b += e[1]
        answer = min(answer, abs(s-b))

# print(answer)