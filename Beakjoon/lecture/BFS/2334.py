from collections import deque
dx = [0,-1,0,1]
dy = [-1,0,1,0]
m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*m for _ in range(n)]
def bfs(x, y, rooms):
    q = deque()
    q.append((x,y))
    d[x][y] = rooms
    cnt = 0
    while q:
        x,y = q.popleft()
        cnt += 1
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] != 0:
                continue
            if (a[x][y] & (1<<k)) > 0:
                continue
            q.append((nx,ny))
            d[nx][ny] = rooms
    return cnt
rooms = 0
room = [0]
for i in range(n):
    for j in range(m):
        if d[i][j] == 0:
            rooms += 1
            room.append((bfs(i,j,rooms)))
print(rooms)
ans = 0
for i in range(1,rooms+1):
    if ans < room[i]:
        ans = room[i]
print(ans)
ans = 0
for i in range(n):
    for j in range(m):
        x,y = i,j
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] == d[x][y]:
                continue
            if (a[x][y] & (1<<k)) > 0:
                if ans < room[d[x][y]]+room[d[nx][ny]]:
                    ans = room[d[x][y]]+room[d[nx][ny]]
print(ans)
