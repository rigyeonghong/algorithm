from collections import defaultdict

def isAnagram(str1, str2):
   # 1. 딕셔너리로 문제를 풀어보자
   # 일단 첫번째 단어 각각 알파벳 글자수 세자
   # elice -> {'e': 2, 'c' : 1, 'l':1,'i':1}
   
#     _dict = {}
#     for c in str1:
#         if c in _dict:
#             _dict[c] += 1
#         else:
#             _dict[c] = 1
            
    # 2. 두번째 단어에 대해 똑같이 만들고, 둘이 같은지 보면 되?
    # 예약어 그대로 쓸때 _씀
    
#     _dict2 = {}
#     for c in str2:
#         if c in _dict2:
#             _dict2[c] += 1
#         else:
#             _dict2[c] = 1

    #2. list('elice') -> ['e','l','i','c','e']
    
    # return  sorted(str1) == sorted(str2)
    
#3. key/value value의 기본값 설정
    # int = 0 
    # list = []
    
    _dict = defaultdict(int)
    _dict2 = defaultdict(int)

    for c in str1:
        _dict[c] += 1
        
    for c in str2:
        _dict2[c] += 1
        
    return _dict == _dict2

    
    

def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()