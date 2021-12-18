# 1부터 N까지 자연수 중에
# 중복없이 M개를 고른 수열
# ex. 4 2 => 1 2 3 
# 4개중에 중복없이 2개 고른 것


# def BT(index, letter):
#     num = array[index]
#     chars = hassmap[num]

# output_array= []
# def BT(index, letter):
#     if index >= len(array) : 
#         output_array.add(letter)
#     for i in array:
#         # 1
#         BT(index+1, letter+1)

#bfs 인데 아니면 나오는 조건을 걸면되지?!

# array = []
# for i in range(1, N+1): 
#     array += i 
# # [1,2,3,4]

import sys

N, M = map(int, sys.stdin.readline().split())

result = []
#[1,2]
visited = [False]*(N+1)
# [False, True, True, False, False]

# M = depth
def BT(depth, N, M):
    if depth == M+1 : 
    #깊이까지 탐색 완료
        for i in range(0, len(result)):
            print(result[i],end=" ")
        print()
        return 
    for num in range(1, N+1):
        if not visited[num]:
            # visited[1] 방문한적이 없으면
            visited[num] = True
            # 지금 방문한걸로 True로 바꿔줘
            result.append(num)
            # 방문했으니까 결과(result)에 num(1)넣어줘
            BT(depth+1, N, M)
            # 1하나 넣고 1에 대응하는 다음 거 BT로 또 돌려 : 2번째꺼 구하러
            visited[num] = False
            # visite[2] = False로 만들고
            result.pop()
            # result에서 2를 pop (맨마지막 요소 돌려주고 요소 삭제) -> result엔 [1]만
            # ... 4를 pop -> result[1]만 -> 이전에 진행하던 함수 for문에서 1다음 2로 돌아와

BT(1,N,M)

# BT라는 함수 자체가 진행 중간에 재귀함수로 BT를 또 부른거니까 그게 (1 2 print하고) return으로 빠져나가면
# 그전에 진행하던 BT함수로 돌아오는 stack구조
# depth = 1 일때, num = 3으로 진행되서 1 3 print하고 return ...

