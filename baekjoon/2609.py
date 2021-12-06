import sys

n, m = map(int, sys.stdin.readline().split())


def gcd(n,m):
    if m == 0:
        return n
    return gcd(m, n%m)

# 최대공약수 구하기 2. 유클리드 호제법 O(logN)
# 최소공배수는 최대공약수 * n/최대공약수 * m/최대공약수
# n*m /최대공약수
if n > m:
    result = gcd(n,m)
    print(result)
    print(int(n*m/result))
else :
    result = gcd(m,n)
    print(result)
    print(int(n*m/result))


# 첫번째 풀이법
# 최대공약수 : 두개 중 더 작은 것을 -1씩 하면서 n,m을 각각 나눠봤을때 둘다 나머지 0면
# 1. 작은 수로 큰 수가 나눠 떨어지면 그 값이 최대공약수
# 최소공배수 : 두개 중 더 큰 것을 +1씩 하면서 n,md을 각각 나눴을 때 둘 다 나머지 0면

# pass는 조건문에서 넣어줄 조건 딱히 없는 경우
# continue는 해당 순번 loop 넘어가 다음번 loop로 들어감
# break는 해당 반복문 멈추고 밖으로 나감

# if n >= m:
#     if n % m == 0:
#         print(m) #작은게 최대공약수
#         print(n) #큰게 최소공배수
#     else:
        # 최대공약수 구하기 O(n)
        # for i in range(m, 0, -1):
        #     if n % i ==0 and m % i ==0:
        #         print(i)
        #         break

        
#         # 최소 공배수 구하기
#         # 24 18 
#         for i in range(n,(m*n)+1 ):
#             if i % n ==0 and i % m ==0:
#                 print(i)
#                 break
# else:
#     # m이 n보다 클 때 
#     if m % n == 0:
#         print(n) #작은게 최대공약수
#         print(m) #큰게 최소공배수
#     else:
#         # 최대공약수 구하기
#         for i in range(n, 0, -1):
#             if n % i ==0 and m % i ==0:
#                 print(i)
#                 break
            
        # 최소 공배수 구하기
        # for i in range(m,(m*n)+1 ):
        #     if i % n ==0 and i % m ==0:
        #         print(i)
        #         break

