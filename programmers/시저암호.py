# s : 문자열 : 공백도 포함, 대소문자
from collections import deque

def solution(s, n):
    answer = ''
    
    deq = deque()
    for i in s:
        deq.append(i)
    
    while deq:
        poped = deq.popleft()
        if poped == ' ':
            answer += poped

        #대문자일 때
        elif ord(poped) < 91 and ord(poped) + n > 90:
            char = chr(64 + ord(poped) + n - 90)
            answer += char
        elif ord(poped) < 91:
            char = chr(ord(poped) + n)
            answer += char

        #소문자일 때
        elif ord(poped) + n > 122:
            char = chr(96 + ord(poped) + n - 122)
            answer += char
        else:
            char = chr(ord(poped) + n)
            answer += char
    
    return answer