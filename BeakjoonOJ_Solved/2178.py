from collections import deque
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited[0][0] = 1
q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if not visited[nx][ny] and a[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


print(visited[n-1][m-1])
