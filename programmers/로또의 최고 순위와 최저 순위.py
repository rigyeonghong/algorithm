#1 93.3%
def solution(lottos, win_nums):
    same_count = 0
    for num in lottos:
        if num in win_nums:
            same_count += 1
    zero_count = lottos.count(0)
    
    grade = [0,0]
    if same_count == 6:
        grade[1] = 1
    elif same_count == 5:
        grade[1] = 2
    elif same_count == 4:
        grade[1] = 3
    elif same_count == 3:
        grade[1] = 4
    elif same_count == 2:
        grade[1] = 5
    else:
        grade[1] = 6
        
    if same_count+zero_count == 6:
        grade[0] = 1
    elif same_count+zero_count == 5:
        grade[0] = 2
    elif same_count+zero_count == 4:
        grade[0] = 3
    elif same_count+zero_count == 3:
        grade[0] = 4
    elif same_count+zero_count == 2:
        grade[0] = 5
    else:
        grade[1] = 6
        
    return grade

#2 100%
def solution(lottos, win_nums):
    same_count = 0
    for num in lottos:
        if num in win_nums:
            same_count += 1
    zero_count = lottos.count(0)
    
    grade = [0,0]
    if same_count == 6:
        grade[1] = 1
    elif same_count == 5:
        grade[1] = 2
    elif same_count == 4:
        grade[1] = 3
    elif same_count == 3:
        grade[1] = 4
    elif same_count == 2:
        grade[1] = 5
    else:
        grade[1] = 6
    
    if zero_count ==0:
        grade[0] = grade[1]
        return grade
        
    if same_count+zero_count == 6:
        grade[0] = 1
    elif same_count+zero_count == 5:
        grade[0] = 2
    elif same_count+zero_count == 4:
        grade[0] = 3
    elif same_count+zero_count == 3:
        grade[0] = 4
    elif same_count+zero_count == 2:
        grade[0] = 5
    else:
        grade[1] = 6
        
    return grade

# better solution
def solution(lottos, win_nums):

    rank = [6,6,5,4,3,2,1]
    same_count = 0
    for num in lottos:
        if num in win_nums:
            same_count += 1
    zero_count = lottos.count(0)

    return rank[zero_count + same_count], rank[same_count]