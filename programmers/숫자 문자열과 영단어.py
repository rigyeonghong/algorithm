#1
def solution(s):
    answer = 0
    num = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for n in num:
        if n in s:
            s = s.replace(n,num[n])
    return int(s)

#ref
num = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

def solution(s):
    answer = s
    for key, value in num.items():
        answer = answer.replace(key, value)
    return int(answer)