#1 27% WRONG ANSWER
def solution(A):
    cnt = 1
    if len(A) == 0:
        return 0
    peak = [] 
    tmp = [[0,0]]
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            if i == 0:
                tmp[0] = [1, A[1]]
            elif tmp[0][1] < A[i+1]:
                tmp[0] = [i+1,A[i+1]]
        elif A[i] > A[i+1]:
            if i != 0 and tmp[0][0] == i:
                peak.append(i)
                tmp[0] = [i-1, A[i-1]]
            elif i == 0:
                peak.append(i)   
    for i in range(len(peak)-1):
        if peak[i+1] - peak[i] >= 2:
            cnt += 1
    return cnt

#2 45% WRONG ANSWER
def solution(A):
    if len(A) == 0:
        return 0
    peak = [] 
    tmp = [[0,0]]
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            if i == 0:
                tmp[0] = [1, A[1]]
            elif tmp[0][1] < A[i+1]:
                tmp[0] = [i+1,A[i+1]]
        elif A[i] > A[i+1]:
            if i != 0 and tmp[0][0] == i:
                peak.append(i)
                tmp[0] = [i-1, A[i-1]]
            elif i == 0:
                peak.append(i)   
    return len(peak)

#3 36% WRONG ANSWER
def solution(A):
    if len(A) == 0:
        return 0
    peak = [] 
    tmp = [[0,0]]
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            if i == 0:
                tmp[0] = [1, A[1]]
            elif tmp[0][1] < A[i+1]:
                tmp[0] = [i+1,A[i+1]]
        elif A[i] > A[i+1]:
            if i != 0 and tmp[0][0] == i:
                peak.append(i)
                tmp[0] = [i-1, A[i-1]]
            elif i == 0:
                peak.append(i)   
    if len(peak) == 0 :
        return 0
    else:
        # len(A) 가 소수
        if len(A) % 2 != 0:
            return 1
        # len(A) 가 소수 아님
        else:
            return len(peak)

#ref O(N * log(log(N)))
def solution(A):
    peaks = []
    
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(i)

    for i in range(len(peaks),0,-1):
        if len(A) % i == 0:
            block_size = len(A) // i
            block = [False] * i
            block_cnt = 0
            for j in range(len(peaks)):
                idx = peaks[j] // block_size
                if block[idx] == False:
                    block[idx] = True
                    block_cnt += 1

            if block_cnt == i:
                return block_cnt
    
    return 0