a = [list(map(int, input().split())) for _ in range(5)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []

def go(x, y, cnt, num):
    global result
    if cnt == 6:
        result.append(str(num))
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx<0 or nx>=5 or ny < 0 or ny >= 5:
            continue
        go(nx, ny, cnt+1, num+[a[x][y]])

for i in range(5):
    for j in range(5):
        go(i, j, 0, [])

print(len(set(result)))