def solution(left, right):
    answer = []
    num = []
    
    for i in range(left, right+1):
        num.append(i)
        count = 0 
        for j in range(1, i+1):
            if i == j:
                count += 1
            elif i % j == 0:
                count += 1
        answer.append(count)
    
    #answer = [약수의 개수, 약수의 개수, 약수의 개수, 약수의 개수...]
    
    divisor = []
    for i in zip(num,answer):
        divisor.append(i)
    # divisor = [(13,2),(14,4)....]
    
    result = 0
    for i in divisor:
        if i[1] % 2 == 0:
            result += i[0]
        else:
            result -= i[0]
            
    return result