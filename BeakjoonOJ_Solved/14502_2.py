from collections import deque
import copy
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
virus = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            virus.append((i,j))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def spread(b, walls):
    for wx, wy in walls:
        b[wx][wy] = 1
    for v in virus:
        vx, vy = v
        q = deque()
        q.append((vx, vy))
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y+dy[k]
                if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
                    b[nx][ny] = 2
                    q.append((nx,ny))
    s = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                s += 1
    return s


def go(idx, walls):
    global answer
    if len(walls) == 3:
        res = spread(copy.deepcopy(a), walls)
        answer = max(res, answer)
        return
    for i in range(idx, n*m):
        x = i // m
        y = i % m
        if a[x][y] == 0:
            go(i+1, walls +[(x, y)])
    return

answer = 0
go(0, [])
print(answer)