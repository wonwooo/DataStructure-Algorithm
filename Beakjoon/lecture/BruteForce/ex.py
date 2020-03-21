n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False]*m for _ in range(n)]
def go(x, y, cnt, sum):
    global ans
    if cnt == 4:
        if sum > ans:
            ans = sum
        return #이거 안하면 무한 recursion
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                go(nx, ny, cnt+1, sum + a[x][y])
    visited[x][y] = False

ans = 0
for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)#ans 갱신
        if i+2 <= n-1:
            if j+1 <= m-1:
                s = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j+1]
                if s > ans:
                    ans = s
            if j-1 >= 0:
                s = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j-1]
                if s > ans:
                    ans = s
        if i+1 <= n-1:
            if j+2 <= m-1:
                s = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1]
                if s > ans:
                    ans = s
        if i-1 >= 0:
            if j+2 <= m-1:
                s = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+1]
                if s > ans:
                    ans = s

print(ans)


