def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor != 0:
            continue;
        else :
            answer.append(i);
            
    answer.sort();
    if answer == []:
        answer.append(-1);
    return answer