import sys
n, k = map(int, sys.stdin.readline().split()) # 멀티탭 구멍개수(1<=k<=100), 전기 용품 사용 횟수(1<=k<=100)
sequence = list(map(int, sys.stdin.readline().split()))
multitab= set()

cnt = 0
for idx, s in enumerate(sequence):
    if len(multitab) < n: # 콘센트 비어있을 때
        multitab.add(s)
    elif s in multitab: 
        continue
    else: # 콘센트 꽉차고 새로운 거 넣어야할 때
        cnt += 1
        try:
            far = 0 # 가장 인덱스 먼 친구의 인덱스
            who_far = 0
            for m in multitab:
                how_far = sequence[idx+1:].index(m)
                if  how_far > far:
                    far = how_far
                    who_far = m
            multitab.remove(who_far)
            multitab.add(s)

        except:
            multitab.remove(m)
            multitab.add(s)
print(cnt)