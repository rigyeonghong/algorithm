import sys

N = int(sys.stdin.readline())
error = 0
for _ in range(N):
    word = sys.stdin.readline()
    for idx in range(len(word)-1):
        if word[idx] != word[idx+1]:    #연달아 오는 문자가 다를 때
            new_word = word[idx+1:]     #이후 글자로 새문자열 만듦
            if new_word.count(word[idx]) > 0:   #새문자열에 현재 문자 있다면
                error += 1      # 카운팅하고 for문 끝내기
                break

print(N-error)