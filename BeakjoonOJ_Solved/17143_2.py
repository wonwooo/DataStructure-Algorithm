locs = []
dirchange = {0:1, 1:0, 2:3, 3:2}
r, c, m = map(int, input().split())
a = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    r_, c_, s, d, z = map(int, input().split())
    a[r_-1][c_-1].append((z, s, d-1))
    locs.append((r_-1, c_-1))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

col = 0
got = []
while col<c:
    for x in range(r):
        if a[x][col]:
            locs.remove((x, col))
            got.append(a[x][col].pop())
            break
    #이동
    tmplocs = []
    for x, y in locs:
        cx, cy = x, y
        size, speed, dir = a[x][y].pop(0)
        if dir in [0, 1]:
            dist = speed % ((r-1)*2)
        elif dir in [2, 3]:
            dist = speed % ((c-1)*2)
        for _ in range(dist):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                dir = dirchange[dir]
                nx, ny = cx+dx[dir], cy+dy[dir]
            cx, cy = nx, ny
        a[cx][cy].append((size, speed, dir))
        tmplocs.append((cx, cy))
    locs = set(tmplocs)
    for x_, y_ in locs:
        if len(a[x_][y_]) >= 2:
            a[x_][y_] = [sorted(a[x_][y_])[-1]]
    col += 1

s = 0
for i in range(len(got)):
    s+= got[i][0]
print(s)