#1 75% WRONG ANSWER
def solution(S):
    stack = []
    
    for s in S:
        if s == "(":
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            p = stack.pop()
            if p == ")":
                return 0
    return 1

#2 
def solution(S):
    stack = []
    
    for s in S:
        if s == "(":
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            p = stack.pop()
            if p == ")":
                return 0
    if len(stack) == 0: 
        return 1
    else:
        return 0