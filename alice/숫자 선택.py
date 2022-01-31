import sys

def main():
    n = input()
    data = list(map(int, sys.stdin.readline().split()))
    # [1, 7, 2, 6, 5, 4]
    
    result = 0
    
    for i in range(1, len(data)):
        if i % 2 == 1 and data[i] % 2 == 0 :
            result += data[i]
    
    print(result)

if __name__=="__main__":
    main()