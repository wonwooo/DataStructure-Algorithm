n, m =map(int, input().split())
x, y, dir = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]
visited[x][y] = True


changedir = 0
while True:

    if changedir == 4:
        nx, ny = x-dx[dir], y-dy[dir]
        if a[nx][ny] == 1:
            break
        else:
            x, y = nx, ny
            changedir = 0
            continue

    dir = (dir-1)%4
    changedir += 1
    nx, ny = x + dx[dir], y + dy[dir]
    if not visited[nx][ny] and a[nx][ny] == 0:
        visited[nx][ny] = True
        x, y = nx, ny
        changedir = 0
        continue
    else:
        continue

ans = 0
for row in visited:
    ans += sum(row)

print(ans)

