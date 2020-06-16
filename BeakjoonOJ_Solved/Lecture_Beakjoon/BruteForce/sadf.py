dx = [0,1,0,-1]
dy = [1,0,-1,0]
def check(a, b, x, y, dir):
    n = len(a)
    m = len(a[0])
    i,j = x,y
    while 0 <= i < n and 0 <= j < m:
        if a[i][j] == 6:
            break
        b[i][j] = a[x][y]
        i += dx[dir]
        j += dy[dir]
def go(a, cctv, index, dirs):
    if len(cctv) == index:
        n = len(a)
        m = len(a[0])
        b = [row[:] for row in a]
        for i,(what,x,y) in enumerate(cctv):
            if what == 1:
                check(a,b,x,y,dirs[i])
            elif what == 2:
                check(a,b,x,y,dirs[i])
                check(a,b,x,y,(dirs[i]+2)%4)
            elif what == 3:
                check(a,b,x,y,dirs[i])
                check(a,b,x,y,(dirs[i]+1)%4)
            elif what == 4:
                check(a,b,x,y,dirs[i])
                check(a,b,x,y,(dirs[i]+1)%4)
                check(a,b,x,y,(dirs[i]+2)%4)
            elif what == 5:
                check(a,b,x,y,dirs[i])
                check(a,b,x,y,(dirs[i]+1)%4)
                check(a,b,x,y,(dirs[i]+2)%4)
                check(a,b,x,y,(dirs[i]+3)%4)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if b[i][j] == 0:
                    cnt += 1
        return cnt
    ans = 100
    print('ans : ', ans, 'index : ', index, 'dirs : ', dirs)
    for i in range(4):
        temp = go(a, cctv, index+1, dirs+[i])
        print('ans : ', ans, 'index : ', index + 1, 'dirs : ', dirs + [i], 'temp : ', temp)
        if ans > temp:
            ans = temp
    return ans


n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
cctv = []

for i in range(n):
    for j in range(m):
        if 1 <= a[i][j] <= 5:
            cctv.append((a[i][j], i, j))
print(go(a, cctv, 0, []))