from collections import deque
n, m, t = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
rotations= [list(map(int, input().split())) for _ in range(t)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def rotate(ls, d, k):
    n = len(ls)
    k = k%m
    if d==0:
        ls = ls[n-k:] + ls[:n-k]
    elif d == 1:
        ls = ls[k:] + ls[:k]
    return ls

def bfs(x, y):
    global erased
    global visited
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    coords = [(x, y)]
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], (cy + dy[k])%m
            if nx<0 or nx>=n:
                continue
            if a[nx][ny] == a[cx][cy] and not visited[nx][ny]:
                q.append((nx, ny))
                coords.append((nx, ny))
                visited[nx][ny] = True
    if len(coords) > 1:
        erased = True
        for x, y in coords:
            a[x][y] = 0



for x, d, k in rotations:
    for i in range(x-1, n, x):
        a[i] = rotate(a[i], d, k)
    visited = [[False]*m for _ in range(n)]
    empty = True
    erased = False
    for i in range(n):
        for j in range(m):
            if a[i][j] and not visited[i][j]:
                empty = False
                bfs(i,j)
    if not erased and not empty:
        remain = []
        for i in range(n):
            for j in range(m):
                if a[i][j]:
                    remain.append(a[i][j])
        mean = sum(remain)/len(remain)
        for i in range(n):
            for j in range(m):
                if a[i][j]:
                    if a[i][j] > mean:
                        a[i][j] -= 1
                    elif a[i][j] < mean:

answer = sum([sum(a[i]) for i in range(n)])                        a[i][j] += 1

print(answer)