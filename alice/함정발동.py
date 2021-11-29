people = [list(input()) for _ in range(8)]

count = 0

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0: 
            if people[i][j] == 'H':
                count += 1
            else:
                continue
        else:
            continue
print(count)