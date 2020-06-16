n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]



def go(x, y, shape):
    global count
    if (x, y) == (n-1, n-1):
        count += 1
        return

    if shape == 1:
        if y+1 < n and a[x][y+1] == 0:
            go(x, y+1, 1)
        if x+1<n and y+1<n and a[x+1][y+1] == 0 and a[x][y+1] == 0 and a[x+1][y] == 0:
            go(x+1, y+1, 3)
    if shape == 2:
        if x + 1 < n and a[x+1][y] == 0:
            go(x+1, y, 2)
        if x + 1 < n and y + 1 < n and a[x + 1][y + 1] == 0 and a[x][y + 1] == 0 and a[x + 1][y] == 0:
            go(x+1, y+1, 3)
    if shape == 3:
        if y+1<n and a[x][y+1] == 0:
            go(x, y+1, 1)
        if x+1<n and a[x+1][y] == 0:
            go(x+1, y, 2)
        if x+1<n and y+1<n and a[x+1][y] == 0 and a[x][y+1] == 0 and a[x+1][y+1] == 0:
            go(x+1, y+1, 3)
    return

count = 0
go(0, 1, 1)
print(count)
