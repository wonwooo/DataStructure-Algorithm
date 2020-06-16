from collections import deque
import copy
n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def merge(x, y):
    global a
    global visited
    q = deque()
    union = [(x, y)]
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if l <= abs(a[x][y] - a[nx][ny]) <= r and not visited[nx][ny]:
                visited[nx][ny] = True
                union.append((nx, ny))
                q.append((nx, ny))
    s = 0
    for x, y in union:
        s += a[x][y]
    for x, y in union:
        a[x][y] = int(s/len(union))

count = 0
while True:
    tmp = copy.deepcopy(a)
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                merge(i,j)
    if tmp == a:
        break
    count += 1
print(count)