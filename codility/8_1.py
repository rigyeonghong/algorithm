#1 O(N)
def solution(A):
    n = len(A)
    size = 0
    tmp = 0
    for a in A:
        if size ==0:
            size += 1
            tmp = a
        else:
            if tmp != a:
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = tmp
    leader = -1
    count = 0

    for idx, value in enumerate(A):
        if value == candidate:
            leader = idx
            count += 1

    if count > (n//2):
        return leader
    else:
        return -1