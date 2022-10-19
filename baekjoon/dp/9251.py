import sys
input = sys.stdin.readline
word1, word2 = input().strip(), input().strip()
l1, l2 = len(word1), len(word2)
cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:          # 해당 인덱스가 누적변수보다 크다면 
            cnt = cache[j]          # 누적변수 cnt = 해당 인덱스값
        elif word1[i] == word2[j] : # 같은 문자가 나온다면
            cache[j] = cnt + 1      # 해당 인덱스에 누적변수 +1
print(max(cache))