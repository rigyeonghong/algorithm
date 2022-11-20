import sys
n = int(sys.stdin.readline())
customer =[]
for _ in range(n):
    customer.append(int(sys.stdin.readline()))
customer.sort(reverse=True)

total = 0
for i in range(n):
    tip = customer[i] - (i)
    if tip > 0:
        total += tip
print(total)    