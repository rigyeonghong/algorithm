import sys
n = int(sys.stdin.readline()) 
stack = []
for _ in range(n):
    jaehyun = int(sys.stdin.readline())
    stack.pop() if jaehyun == 0 else stack.append(jaehyun)
print(sum(stack))