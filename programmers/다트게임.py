# * 해당점수와 바로 전 점수 각 2배  # -해당점수
def solution(dartResult):
    sign = {'*':2,'#':-1}
    squared = {'S':1,'D':2,'T':3}
    answer = []
    point = 0

    for i in range(len(dartResult)):
        d = dartResult[i]

        if d in squared:
            point = int(point) ** squared[d]
            answer.append(point)

        elif d in sign:
            a = answer.pop()
            tmp = a * sign[d]
            if d == '*':
                if len(answer) != 0:
                    b = answer.pop()
                    b = b * 2 
                    answer.append(b)
            answer.append(tmp)
        else:
            if d == str(0) and dartResult[i-1] == str(1):
                point = 10
            else:
                point = d
    return sum(answer)

#ref
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer