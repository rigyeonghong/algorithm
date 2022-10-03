import sys
n = int(sys.stdin.readline()) 
dots = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
dots.sort()

def dist(dot1, dot2):
    return (dot1[0] - dot2[0]) **2 + (dot1[1] - dot2[1]) **2

def rec(start, end):
    if start == end:
        return float('inf')
    
    if end - start == 1:
        return dist(dots[start], dots[end])
    
    mid = (start + end) // 2
    min_dist = min(rec(start, mid), rec(mid,end))

    candidate_dot = []
    for i in range(start, end+1):
        if (dots[mid][0] - dots[i][0]) ** 2 < min_dist:
            candidate_dot.append(dots[i])
    
    candidate_dot.sort(key=lambda x: x[1])

    t = len(candidate_dot)
    for i in range(t-1):
        for j in range(i+1, t):
            if (candidate_dot[i][1] - candidate_dot[j][1]) ** 2 < min_dist:
                min_dist = min(min_dist, dist(candidate_dot[i], candidate_dot[j])) 
            else:
                break

    return min_dist

print(rec(0, n-1))