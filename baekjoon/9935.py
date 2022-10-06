import sys
string = sys.stdin.readline().rstrip()
boom = sys.stdin.readline().rstrip()

stack = []
lastChar = boom[-1] #폭탄 문자열 마지막 글자
length = len(boom)

for s in string:
    stack.append(s)
    if s == lastChar and ''.join(stack[-length:]) == boom:
        del stack[-length:]
    
answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)