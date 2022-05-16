import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, sys.stdin.readline().split())))

visited = [False]*N
pick = []

def find():
    if len(pick) == M:
        print(*pick)
        return
    
    remember_me = 0

    for i in range(N):
        if not visited[i] and remember_me != data[i]:
            visited[i] = True
            pick.append(data[i])
            remember_me = data[i]
            find()
            visited[i] = False
            pick.pop()

find()