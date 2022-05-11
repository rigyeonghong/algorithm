import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
data = map(str, sorted(list(map(int, sys.stdin.readline().split()))))

print('\n'.join(map(' '.join, permutations(data, M))))

# for p in permutations(data, M):
#     print(p)
    # for num in p:
    #     print(num, end=' ')
    # print()