import sys
n = int(sys.stdin.readline())
products = [int(sys.stdin.readline()) for _ in range(n)]
products.sort(reverse=True)
free = 0
for i in range(2, len(products), 3):
    free += products[i]
print(sum(products) - free)