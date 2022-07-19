#1 33% WRONG ANSWER, TIMEOUT
def solution(A):
    n = len(A)
    size = 0
    leader = 0
    for a in A:
        if size ==0:
            size += 1
            leader = a
        else:
            if leader != a:
                size -= 1
            else:
                size += 1
    
    B = []
    cnt = 0
    for i in range(len(A)):
        p = A.pop(0)
        B.append(p)

        a_leader = 0
        a_size = 0
        for a in A:
            if a_size ==0:
                a_size += 1
                a_leader = a
            else:
                if a_leader != a:
                    a_size -= 1
                else:
                    a_size += 1
        if a_size > 0 and a_leader == leader:
            b_leader = 0
            b_size = 0      
            for b in B:
                if b_size ==0:
                    b_size += 1
                    b_leader = b
                else:
                    if b_leader != b:
                        b_size -= 1
                    else:
                        b_size += 1
            if b_size > 0 and b_leader == leader:
                cnt += 1
    return cnt
        
#2 O(N)
def solution(A):
    cnt = 0

    r_dict = {}
    r_len = len(A)

    for a in A:
        if a in r_dict:
            r_dict[a] += 1
        else:
            r_dict[a] = 1

    l_leader = 0
    l_leader_cnt = 0     
    l_dict = {}
    l_len = 0

    for a in A: 
        r_dict[a] -= 1
        r_len -= 1

        if a in l_dict:
            l_dict[a] += 1
        else:
            l_dict[a] = 1
        l_len += 1

        if l_dict[a] > l_leader_cnt:
            l_leader = a
            l_leader_cnt = l_dict[a]

        if l_leader_cnt > l_len/2 and r_dict[l_leader] > r_len/2:
            cnt +=1
    return cnt      
