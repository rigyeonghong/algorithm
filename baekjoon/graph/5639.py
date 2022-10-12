import sys
sys.setrecursionlimit(10**6)
graph = []
while True:
    try:
        graph.append(int(sys.stdin.readline()))
    except:
        break

def post_order(start, end):
    if start > end:
        return
    mid = end + 1

    # 서브 트리 찾기 
    for i in range(start + 1, end+1):
        if graph[start] < graph[i]:
            mid = i
            break
    
    post_order(start+1, mid-1)
    post_order(mid, end)
    print(graph[start])

post_order(0, len(graph)-1)
