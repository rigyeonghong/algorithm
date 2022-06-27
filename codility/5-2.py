#1 O(B-A) runtime error
def solution(A, B, K):
    div = 1
    count = 0
    for i in range(A,B+1,div):
        if i % K == 0:
            count += 1
            div = K
    return count

#2 success
def solution(A, B, K):
    QA = A//K
    QB = B//K
    RA = A%K
    count = QB - QA
    if RA == 0:
        count += 1
    return count