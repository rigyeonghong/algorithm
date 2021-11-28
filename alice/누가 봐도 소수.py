N = int(input())

def is_prime(k: int):
    n = 2
    while n * n <= k:
        if k % n == 0:
            # print('no')
            return False # 나눠떨어져버리면 False를 return하고 함수 종료
        n += 1
    return True # 위에서 반복문이 한번도 안나눠떨어지고 끝나면 소수!

def solution(N):
    if is_prime(N) is False:
        return False # 뒤집어보기 전에도 소수가 아니면 main solution 함수가 False를 return하고 함수 종료!

    str_N = str(N) # 1234 => '1234' type 변경 (문자 하나씩 반복문으로 돌리려고)
    temp = '' # str 문자 하나씩 여기다 더해줄거라서 temp를 선언하고 '' 빈 문자열로 초기화
    
    for i in range(len(str_N)): # i 는 0 , 1, 2, 3, 4, 5 로 돌아가지만
        j = len(str_N) - (i + 1) # j 는 5, 4, 3, 2, 1, 0 로 j를 거꾸로 뒤에서부터 앞으로 오게 반복문이 돌게함

        if str_N[j] == '3' or str_N[j] == '4' or str_N[j] == '7':
            return False # 뒤집는 과정에 3, 4, 7 이 등장하면 즉시 함수 False return하면서 종료. 이후 과정은 안해도 됨
        elif str_N[j] == '6': # 6이면 9로 바꿔서 넣고
            temp += '9'
        elif str_N[j] == '9': # 9면 6으로 바꿔서 넣고
            temp += '6'
        else:   # 그 외는 그대로 집어넣음
            temp += str_N[j]

    reverse_int = int(temp) # ex) '34124' => 34124 다시 타입을 int로

    if is_prime(reverse_int): # 뒤집어 진 숫자가 소수인지 아닌지 다시 판별
        return True
    else:
        return False  

#################################

answer = solution(N)

if answer:
    print('yes')
else:
    print('no')