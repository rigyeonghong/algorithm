#1 O(N**3) TIMEOUT ERROR
def solution(A):
    min_pointer = 0
    min_avg = 10000000000000000000000

    # P를 차례대로 증가시키며 반복
    for P in range(len(A)-1):
        # Q 이동시키기
        Q = P + 1
        while Q < len(A):
            if min_avg > sum(A[P:Q+1]) / (Q+1-P):
                min_avg = sum(A[P:Q+1]) / (Q+1-P)
                min_pointer = P
            Q += 1
    return min_pointer

#2 70% wrong answer
# 전체 array의 평균값 >= subarray 평균값 중 작은 값
# subarray 평균값 중 작은 값을 구함 : len(subarray)가 2 or 3
def solution(A):
    minAvg = (A[0] + A[1]) / 2
    minIdx = 0

    for i in range(2,len(A)):
        if (A[i-2] + A[i-1] + A[i]) / 3 < minAvg:
            minAvg = (A[i-2] + A[i-1] + A[i]) / 3
            minIdx = i-2
        
        if (A[i-1] + A[i]) / 2 < minAvg:
            minAvg = (A[i-1] + A[i]) / 2
            minIdx = i-1
        
    return minIdx