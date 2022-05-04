n = int(input())

for i in range(n):
    m = int(input())
    data = list(map(int, input().split()))
    max_sell = data[-1]
    max_profit = 0
    for idx in range(len(data)-1, -1, -1):
        if data[idx]<max_sell:
            max_profit += max_sell-data[idx]
        elif data[idx]>max_sell:
            max_sell = data[idx]
    print(f"#{i+1} {max_profit}")