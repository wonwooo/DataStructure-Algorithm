'''
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
'''

from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
wcheck = [[False]*m for _ in range(n)]
scheck = [[False]*m for _ in range(n)] #locations of one of swans
sx, sy, ex, ey = -1, -1, -1, -1 #
swan = deque()
nswan = deque()
water = deque()
nwater = deque()
a = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            if sx == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j
            a[i][j] = '.'

        if a[i][j] == '.':
            water.append((i,j))#water array에 물 위치정보
            wcheck[i][j] = True #wcheck에도 물 방문확인

swan.append((sx, sy))
scheck[sx][sy] = True

i = 0
while True:
    while water:
        x, y = water.popleft()
        a[x][y] = '.' #..?
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if wcheck[nx][ny]:
                continue
            if a[nx][ny] =='.':
                water.append((nx, ny))
                wcheck[nx][ny] = True
            else:
                nwater.append((nx, ny))
                wcheck[nx][ny] = True

    while swan:
        x, y = swan.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if scheck[nx][ny]:
                continue
            if a[nx][ny] == '.':
                swan.append((nx, ny))
                scheck[nx][ny] = True
            else:
                nswan.append((nx, ny))
                scheck[nx][ny] = True

    if scheck[ex][ey]:
        print(i)
        break
    i += 1
    water = nwater
    swan = nswan
    nwater = deque()
    nswan = deque()





