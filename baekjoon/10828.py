import sys
n = int(sys.stdin.readline()) 
instructions = [list(sys.stdin.readline().split())for _ in range(n)]
stack = []

for i in instructions:
    if i[0] == "push":
        stack.append(i[1])
    elif i[0] == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif i[0] == "size":
        print(len(stack))
    elif i[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else: # top
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)