#1 25% WRONG ANSWER
def solution(S):
    stack = [S[0]]
    diff = {"}":"{","]":"[",")":"("}
    for i in range(1,len(S)):
        s = S[i]
        if s not in diff:
            stack.append(s)
        elif diff[s] != stack.pop():
            return 0
    return 1

#2
def solution(S):
    stack = []
    diff = {"{":"}","[":"]","(":")"}
    for s in S:
        if diff.get(s):
            stack.append(s)
        else:
            if not stack or diff[stack.pop()] != s:
                return 0
    # {{{ 인 경우
    if stack:
        return 0
    return 1