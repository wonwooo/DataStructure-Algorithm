r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
refresher = []
for i in range(r):
    for j in range(c):
        if a[i][j] == -1:
            refresher.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def spread():
    global a
    b = [[0]*c for _ in range(r)]
    for rx, ry in refresher:
        b[rx][ry] = -1

    for x in range(r):
        for y in range(c):
            if a[x][y] and a[x][y] != -1:#미세먼지가 있다면 확산시작, 공기 청정기도 넘겨야함
                vol = a[x][y] // 5
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if nx<0 or nx>=r or ny<0 or ny>=c or a[nx][ny]==-1:
                        continue
                    #빼면서 1/5 구하지않고 한번에 1/5를 구해함
                    b[nx][ny] += vol
                    a[x][y] -= vol
                b[x][y] += a[x][y] #여기서 큰실수...옆칸에서 퍼져있을 수 있기 때문에 =이 아니라 더해줘야 한다
    a = b

def refresh():
    global a
    r1 = refresher[0]
    r2 = refresher[1]

    x, y = r1
    for i in range(x-1,0,-1):
        a[i][0] = a[i-1][0]
    for j in range(0, c-1):
        a[0][j] = a[0][j+1]
    for i in range(0,x):
        a[i][c-1] = a[i+1][c-1]
    for j in range(c-1, 1, -1):
        a[x][j] = a[x][j-1]
    a[x][1] = 0

    x, y= r2
    for i in range(x+1, r-1):
        a[i][0] = a[i+1][0]
    for j in range(0, c-1):
        a[r-1][j] = a[r-1][j+1]
    for i in range(r-1, x, -1):
        a[i][c-1] = a[i-1][c-1]
    for j in range(c-1, 1, -1):
        a[x][j] = a[x][j-1]
    a[x][1] = 0


for i in range(t):
    spread()
    refresh()

answer = 0
for i in range(r):
    for j in range(c):
        if a[i][j] != -1:
            answer += a[i][j]
print(answer)