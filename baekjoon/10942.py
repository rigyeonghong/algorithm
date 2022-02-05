import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
# Q = []
for _ in range(M):
    # Q.append(list(map(int, sys.stdin.readline().split())))
    Q = list(map(int, sys.stdin.readline().split()))
    start = Q[0]
    end = Q[1]

    # data[start] ~ data[end]
    tmp = data[start-1:end]
    if tmp == tmp[::-1]:
        print(1)
    else:
        print(0)    