import sys
n, m = map(int, sys.stdin.readline().split())
dict = set()
result = []
for _ in range(n):
    dict.add(sys.stdin.readline().strip())
for _ in range(m):
    input = sys.stdin.readline().strip()
    if input in dict:
        result.append(input)
result.sort()
print(len(result))
for r in result:
    print(r)