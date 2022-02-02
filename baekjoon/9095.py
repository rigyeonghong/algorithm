import sys

n = int(sys.stdin.readline())
      
def sums(x):
    if x == 1:
        return(1)
    elif x == 2:
        return(2)
    elif x == 3:
        return(4)
    else:
        return sums(x-1) + sums(x-2) + sums(x-3) 
        
for _ in range(n):
    x = int(sys.stdin.readline())
    print(sums(x))