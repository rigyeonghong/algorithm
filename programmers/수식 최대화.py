import re
from itertools import permutations

def solution(expression):
    answer = [] 
    a = ''
    for ex in expression:
        if ex == "+" or ex == "-" or ex == "*":
            answer.append(a)
            a = ''
            answer.append(ex)
        else:
            a += ex
    answer.append(a)
            
    dict = {"-":0,"+":0,"*":0}
    cnt = 0
    m = []
    for d in dict:
        if d in answer:
            cnt += 1
            m.append(d)

    max_value = 0
    for p in permutations(m, cnt):
        result = answer[:]
        print(result, p, answer)
        for i in p:
            while i in result:
                idx = result.index(i)
                if i == "+":
                    tmp = int(result[idx-1]) + int(result[idx+1])
                elif i == "-":
                	tmp = int(result[idx-1]) - int(result[idx+1])
                else:
                    tmp = int(result[idx-1]) * int(result[idx+1])
                result[idx-1] = tmp
                result.pop(idx)
                result.pop(idx)
            
        max_value = max(max_value, abs(int(result[0])))
                
    return max_value

# ref
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)