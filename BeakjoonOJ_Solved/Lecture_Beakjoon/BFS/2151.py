from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
s = [input() for _ in range(n)]
b = [[0]*n for _ in range(n)]
v = []
start,end = -1,-1
for i in range(n):
    for j in range(n):
        if s[i][j] == '#':
            if start == -1:
                start = len(v)
            else:
                end = len(v)
            v.append((i,j))
            b[i][j] = len(v)-1
        elif s[i][j] == '!':
            v.append((i,j))
            b[i][j] = len(v)-1
m = len(v)
a = [[False]*m for _ in range(m)]
for i in range(len(v)):
    for k in range(4):
        x,y = v[i]
        x += dx[k]
        y += dy[k]
        while 0 <= x < n and 0 <= y < n:
            if s[x][y] == '*':
                break
            if s[x][y] == '!' or s[x][y] == '#':
                a[i][b[x][y]] = True
            x += dx[k]
            y += dy[k]
q = deque()
dist = [-1] * m
q.append(start)
dist[start] = 0
while q:
    now = q.popleft()
    for i in range(m):
        if a[now][i] != 0 and dist[i] == -1:
            dist[i] = dist[now] + 1
            q.append(i)
print(dist[end]-1)
