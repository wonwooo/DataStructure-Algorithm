import sys
sys.setrecursionlimit(10000)

r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * c for _ in range(r)]

def dfs(x, y):
    global wolf, sheep
    if a[x][y] == 'v':
        wolf += 1
    elif a[x][y] == 'o':
        sheep += 1
    visited[x][y] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if a[nx][ny] != '#' and not visited[nx][ny]:
               dfs(nx, ny)

wolves = 0
sheeps = 0
for i in range(r):
    for j in range(c):
        if a[i][j] != '#' and not visited[i][j]:
            wolf, sheep = 0, 0
            dfs(i, j)
            if wolf < sheep:
                sheeps += sheep
            else:
                wolves += wolf

print(sheeps, wolves)
