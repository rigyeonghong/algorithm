#1 12% Wrong Answer
def solution(A):
    # A를 돌면서 원을 하나씩 만들고
    # 원이 만들어질 때마다 이전에 있던 원이랑 겹치면 counting

    circle = [] 
    result = 0
    # idx 는 중심점 / value는 길이
    # value - idx + value
    for idx, value in enumerate(A):
        start = idx - value
        end = idx + value
        circle.append((start, end))
    circle.sort()
    for i in range(len(circle)):
        for j in range(i+1,len(circle)):
            if circle[j][0] < circle[i][1]:
                result += 1
    if result > 10000000:
        return -1
    return result

#2 12% 
def solution(A):
    circle = []
    result = 0
    for idx, value in enumerate(A):
        start = idx - value
        end = idx + value
        circle.append((start, end))
    circle.sort()
    for i in range(len(circle)):
        for j in range(i+1,len(circle)):
            if circle[j][0] < circle[i][1]:
                result += 1
            elif circle[i][0] == circle[j][0] and circle[i][1] != circle[j][1]:
                result += 1
    if result > 10000000:
        return -1
    return result

#3 
def solution(A):
    circle = []
    result = 0
    for idx, value in enumerate(A):
        start = idx - value
        end = idx + value
        circle.append((start, end))
    circle.sort()
# [(-4, 6), (-1, 1), (0, 4), (0, 8), (2, 4), (5, 5)]
    for i in range(len(circle)):
        for j in range(i+1,len(circle)):
            if circle[j][0] < circle[i][1]:
                result += 1
            elif circle[i][0] == circle[j][0] and circle[i][1] != circle[j][1]:
                result += 1
            elif circle[i][1] == circle[j][1] and circle[i][0] != circle[j][0]:
                result += 1
    if result > 10000000:
        return -1
    return result

#4 56% O(N**2)
def solution(A):
    result = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if i + A[i] >= j - A[j]:
                result+=1
    if result > 10000000:
        return -1
    return result

#5 
def solution(A):
    circle = []
    
    for i,v in enumerate(A):
        circle.append((i+v,1))
        circle.append((i-v,-1))
    circle.sort()
    
    result = 0
    intervals = 0
    
    for i,v in enumerate(arr):
        if v[1] == 1:
            intervals -= 1
        if v[1] == -1:
            result += intervals
            intervals += 1
    
    if intersect > 10000000:
        return -1
    
    return result