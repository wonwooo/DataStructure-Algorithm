import copy
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, -0] #0동 1남 2서 3북
for i in range(n):
    for j in range(m):
        if a[i][j] != 0 and a[i][j] != 6:
            c.append([a[i][j], (i, j)])

def supervise(b, cx, cy, dirs):
    for dir in dirs:
        x, y = cx, cy
        while True:
            x, y = x+dx[dir], y+dy[dir]
            if x<0 or x>=n or y<0 or y>=m:
                break
            if a[x][y] == 6:
                break
            b[x][y] = '#'

def count(a, c, rotate):
    b = copy.deepcopy(a)
    for i in range(len(c)):

        kind, (cx, cy) = c[i]
        k = rotate[i]

        if kind == 1: #기준 0
            supervise(b, cx, cy, [k])
        if kind == 2: #기준 0, 2
            supervise(b, cx, cy, [k, (2+k)%4])
        if kind == 3: #기준 0, 3
            supervise(b, cx, cy, [k, (3+k)%4])
        if kind == 4: #기준 0, 2, 3
            supervise(b, cx, cy, [k, (2+k)%4, (3+k)%4])
        if kind == 5: #기준 0,1,2,3
            supervise(b, cx, cy, [0, 1, 2, 3])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt+=1
    return cnt




def go(a, c, cnt, rotate):#c(cctv종류와 위치정보), cnt(몇개 방향 할당했는지), rotate(시계 방향으로 90도씩 몇회 돌릴건지)
    if cnt == len(c): #모든 cctv의 방향 설정이 끝난다면

        safe = count(a, c, rotate)
        return safe

    ans = n*m
    for k in range(4):
        temp = go(a ,c, cnt+1, rotate + [k])
        if ans > temp:
            ans = temp

    return ans

print(go(a, c, 0, []))
