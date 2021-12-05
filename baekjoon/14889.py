# import sys

# n = int(sys.stdin.readline())
# s = []
# for i in range(n):
#     s.append(list(map(int, sys.stdin.readline().split())))
# #4 [[0, 1, 2, 3], [4, 0, 5, 6], [7, 1, 0, 2], [3, 4, 5, 0]]

# # output 최솟값!!

# result = []

# visited = [False]*(n+1)

# def bfs(depth, n, start, link, current):
#     if depth == (n/2):
#     #깊이까지 탐색 완료
#         for i in range(n):
#             for j in range(i, n): 
#                 if visited[i] and visited[j]:
#                     start += s[i][j] + s[j][i]
#                 elif not visited[i] and not visited[j]:
#                     link += s[i][j] + s[j][i]
#                 result.append(abs(start-link))
#                 return
    
#     for i in range(current, n):
#         if not visited[i]:
#             visited[i] = True
#             bfs(depth+1, n ,start, link, i)
#             visited[i] = False
            

# bfs(0, n, 0, 0, 1)
# print(min(result))
       

import sys
# sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())
data = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

visited = [0] * N
ans = int(1e9)

def get_ans(num, cursor):
    global ans
    team_zero = 0
    team_one = 0
    if num == N // 2:
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team_one += data[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    team_zero += data[i][j]

        ans = min(ans, abs(team_one - team_zero))

        return

    for i in range(cursor, N):
        if visited[i]:
            continue

        visited[i] = 1
        get_ans(num+1, i+1)
        visited[i] = 0

get_ans(0, 0)
print(ans)