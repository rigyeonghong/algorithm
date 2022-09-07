#ref
from collections import deque
def solution(tickets):
    graph = dict()
	
    for (start, end) in tickets:
        graph[start] = graph.get(start, []) + [end]
    
    for g in graph.keys():
        graph[g].sort()
    print(graph)
    stack = ["ICN"]
    path = []
    
    while stack:
        top = stack[-1]
        
        if top not in graph or len(graph[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(graph[top][0])
            graph[top] = graph[top][1:]

    return path[::-1]