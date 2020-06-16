from collections import deque
m, n, h = map(int, input().split())
a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
visited = [[[-1] * m for _ in range(n)] for _ in range(h)]
t = []
q = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if a[z][x][y] == 0:
                t.append((z, x, y))
            if a[z][x][y] == 1:
                q.append((z,x,y))
                visited[z][x][y] = 0
print(visited)
while q:
    z, x, y = q.popleft()

    for k in range(6):
        nz, nx, ny =  z+dz[k], x+dx[k], y+dy[k] #어이없는 실수..
        if nx<0 or ny<0 or nz<0 or nx>=n or ny>=m or nz>=h:
            continue
        if a[nz][nx][ny] == 0 and visited[nz][nx][ny] == -1:
            visited[nz][nx][ny] = visited[z][x][y] + 1
            q.append((nz, nx, ny))


answer=0
for z, x, y in t:
    if visited[z][x][y] == -1:
        answer = -1
        break
    answer = max(answer, visited[z][x][y])

print(answer)

'''
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
'''