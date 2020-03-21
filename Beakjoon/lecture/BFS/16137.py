from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = -1
def bfs():
    dist = [[[-1]*20 for j in range(n)] for i in range(n)]
    q = deque()
    q.append((0,0,0))
    dist[0][0][0] = 0
    while q:
        x,y,t = q.popleft()
        if a[x][y] >= 2 and t%a[x][y] != 0:
            nt = (t+1)%a[x][y]
            if dist[x][y][nt] == -1:
                dist[x][y][nt] = dist[x][y][t] + 1
                q.append((x,y,nt))
        else:
            for k in range(4):
                nx,ny = x+dx[k], y+dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[x][y] >= 2 and a[nx][ny] >= 2:
                        continue
                    if a[nx][ny] >= 1:
                        nt = (dist[x][y][t]+1)%a[nx][ny]
                        if dist[nx][ny][nt] == -1:
                            dist[nx][ny][nt] = dist[x][y][t] + 1
                            q.append((nx,ny,nt))
    ans = -1
    for i in range(20):
        if dist[n-1][n-1][i] == -1:
            continue
        if ans == -1 or ans > dist[n-1][n-1][i]:
            ans = dist[n-1][n-1][i]
    return ans
def can(i,j):
    garo = False
    if j-1 >= 0 and a[i][j-1] == 0:
        garo = True
    if j+1 < n and a[i][j+1] == 0:
        garo = True
    sero = False
    if i-1 >= 0 and a[i-1][j] == 0:
        sero = True
    if i+1 < n and a[i+1][j] == 0:
        sero = True
    return not (garo and sero)
for i in range(n):
    for j in range(n):
        if a[i][j] == 0 and can(i,j):
            a[i][j] = m
            now = bfs()
            if now != -1:
                if ans == -1 or ans > now:
                    ans = now
            a[i][j] = 0
print(ans)
