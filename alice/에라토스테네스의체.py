def eratosthenes(n):
    # n개의 True 값이 들어있는 목록을 준비 
    # (True는 소수, False는 합성수를 의미)
    sieve = [True] * n # 0 ~ n-1
    
    # 2부터 n까지 하나씩 순차적으로 소수 여부를 판단
    for i in range(2, n):
        # 1. i가 소수인 경우 i의 배수를 False로 변경
        for j in range(i+i,n,i):
            # i+i 에서 시작해서 n에서 종료하고 i씩 증가하라
            sieve[j] = False
        
    # 값이 True인 숫자를 추려낸다
    result = []
    for i in range(2, n):
        if sieve[i] == True :
            result.append(i)
    return result    

print(eratosthenes(10))