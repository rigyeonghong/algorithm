# 예외처리 추가로 생각하고 수정해본 sol
def solution(grade):
    answer = 0
    min_value = 100000
    for i in range(1,len(grade)):
        if grade[i-1] > grade[i]:
            tmp = grade[i-1]
            grade[i-1] = grade[i]
            min_value = min(min_value, grade[i-1])
            answer += abs(grade[i-1] - tmp)
    
    find_idx = grade.index(min_value)
    if find_idx != None and find_idx != 0:
        for i in range(0, find_idx):
            if grade[i] > min_value:
                answer += grade[i] - min_value
                grade[i] = min_value

    return answer

print(solution(grade))