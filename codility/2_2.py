def solution(A):
    s = set()
    for a in A:
        if a in s:
            s.remove(a)
        else:
            s.add(a)
    return s.pop()