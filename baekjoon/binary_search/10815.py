import sys
n = int(sys.stdin.readline())
card = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binary_search(card, check[i], 0, n-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')


'''
    if c == card[0] or card[-1]:
        answer.append(1)
        break
    else:
        l, r = 0, n
        while r >= l:
            mid = (l+r) //2
            if c == card[mid]:
                answer.append(1)
                break
            elif c < card[mid]:
                l = mid +1
            elif c > card[mid]:
                r = mid -1
'''