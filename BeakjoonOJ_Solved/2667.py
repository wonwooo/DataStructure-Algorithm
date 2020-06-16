n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global count
    global visited
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if not visited[nx][ny] and a[nx][ny] == 1:
            visited[nx][ny] = True
            count += 1
            dfs(nx,ny)
    return

areas = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            count = 1
            dfs(i, j)
            areas.append(count)
areas.sort()
print(len(areas))
for c in areas:
    print(c)