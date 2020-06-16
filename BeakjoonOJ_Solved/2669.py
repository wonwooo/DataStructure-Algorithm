import sys


block = [[0 for i in range(101)] for j in range(101)]


for sqr in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            block[x][y] = 1

sum = 0

for i in range(101):
    for j in range(101):
        if block[i][j] == 1:
            sum += 1

print(sum)




