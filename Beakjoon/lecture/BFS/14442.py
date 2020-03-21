''''
14442 벽 부수고 이동하기
최단 거리를 구해야해서 DFS는 안된다
'''

from collections import deque
a = [[0]*1000 for _ in range(1000)]#...?
d = [[[0]*11 for i in range(1000)] for j in range(1000)] #이렇게 짜야 11짜리를 맨 나중 index로 접근
dx = [0,0,1, -1]
dy = [1, -1, 0, 0]
n, m , l = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, list(input()))))
q = deque()
d[0][0][0] = 1
q.append((0,0,0))
while q:
    x, y, z = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y+ dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if a[nx][ny] == 0 and d[nx][ny][z] == 0:
            d[nx][ny][z] = d[x][y][z] + 1
            q.append((nx, ny, z))
        if z+1 <= l and a[nx][ny] == 1 and d[nx][ny][z+1] == 0:
            d[nx][ny][z+1] = d[x][y][z] + 1
            q.append((nx,ny,z+1))
ans = -1
for i in range(l+1):
    if d[n-1][m-1][i] == 0:
        continue
    if ans == -1: #몇번 부숴서라도 (n,m)에 간것이 처음 발견되면 ans = d[n-1][m-1][i]
        ans = d[n-1][m-1][i]
    elif ans > d[n-1][m-1][i]: #몇번 더 부숴서 (n,m)에 앞서 발견된것보다 더 적은 횟수만에 간것이 발견되면
        ans = d[n-1][m-1][i]

print(ans)

