def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left = num
        elif num in [3,6,9]:
            answer += 'R'
            right = num
        else:
            num = 11 if num == 0 else num
            
            absL = abs(num - left)
            absR = abs(num-right)
            
            if sum(divmod(absL,3)) > sum(divmod(absR,3)):
                answer += 'R'
                right = num
            elif sum(divmod(absL,3)) < sum(divmod(absR,3)):    
                answer += 'L'
                left = num
            elif hand == "left":
                answer += 'L'
                left = num
            else: 
                answer += 'R'
                right = num
    return answer