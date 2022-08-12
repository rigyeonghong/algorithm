#1 90%
def solution(n, lost, reserve):
    answer = 0
    l = set(lost)
    r = set(reserve)
    intersection = l & r
    if intersection:
        for i in intersection:
            lost.remove(i)
            reserve.remove(i)
            
    answer += n- len(lost)
    
    if lost:
        for l in lost:
            if l-1 in reserve:
                idx = reserve.index(l-1)
                answer += 1
                reserve.pop(idx)
                continue
            if l+1 in reserve:
                idx = reserve.index(l+1)
                answer += 1
                reserve.pop(idx)
        
    return answer

#2 100%
def solution(n, lost, reserve):
    answer = 0
    l = set(lost)
    r = set(reserve)
    intersection = l & r
    if intersection:
        for i in intersection:
            lost.remove(i)
            reserve.remove(i)
            
    answer += n- len(lost)
    
    if lost:
        lost.sort()
        reserve.sort()
        for l in lost:
            if l-1 in reserve:
                idx = reserve.index(l-1)
                answer += 1
                reserve.pop(idx)
                continue
            if l+1 in reserve:
                idx = reserve.index(l+1)
                answer += 1
                reserve.pop(idx)
        
    return answer