#1 62% O(N*M) timeout error
def solution(S, P, Q):
    answer = []
    for i in range(len(P)):
        new = S[P[i]:Q[i]+1]
        if min(new) == "A":
            answer.append(1)
        elif min(new) == "C":
            answer.append(2)
        elif min(new) == "G":
            answer.append(3)
        elif min(new) == "T":
            answer.append(4)
    return answer

#2 62% O(N*M) timeout error
def solution(S, P, Q):
    answer = []
    while P:
        p = P.pop(0)
        q = Q.pop(0)
        new = S[p:q+1]
        if min(new) == "A":
            answer.append(1)
        elif min(new) == "C":
            answer.append(2)
        elif min(new) == "G":
            answer.append(3)
        elif min(new) == "T":
            answer.append(4)
    return answer

#3 62% O(N*M) timeout error
def solution(S, P, Q):
    answer = []
    while P:
        p = P.pop()
        q = Q.pop()
        new = S[p:q+1]
        if min(new) == "A":
            answer.insert(0,1)
        elif min(new) == "C":
            answer.insert(0,2)
        elif min(new) == "G":
            answer.insert(0,3)
        elif min(new) == "T":
            answer.insert(0,4)
    return answer

#4 O(N+M)
def solution(S, P, Q):
    answer = []
    for i in range(len(P)):
        tmp = S[P[i]:Q[i]+1]
        if "A" in tmp:
            answer.append(1)
        elif "C" in tmp:
            answer.append(2)
        elif "G" in tmp:
            answer.append(3)
        else:
            answer.append(4)
    return answer