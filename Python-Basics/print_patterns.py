rows = 5
x = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    x += 1
    #nested loop (for columns)
    for j in range(1, i + 1):
        print(x, end=' ')
    print('\r')
