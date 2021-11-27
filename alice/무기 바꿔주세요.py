n = int(input())

def change(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (n-1)*(change(n-1) + change(n-2))
print(change(n))