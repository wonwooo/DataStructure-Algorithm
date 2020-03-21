r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
s1, s2 = -1, 0

def diffuse():
    global a
    b = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if a[i][j] >= 5:
                d = a[i][j]//5
                for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < r and 0 <= nj < c and a[ni][nj] != -1:
                        b[ni][nj] += d
                        a[i][j] -= d
    for i in range(r):
        for j in range(c):
            a[i][j] += b[i][j]

def purify():
    for i in range(s1-2, -1, -1):
        a[i+1][0] = a[i][0]
    for i in range(c-1):
        a[0][i] = a[0][i+1]
    for i in range(s1):
        a[i][c-1] = a[i+1][c-1]
    for i in range(c-2, -1, -1):
        a[s1][i+1] = a[s1][i]
    a[s1][1] = 0
    for i in range(s2+1, r-1):
        a[i][0] = a[i+1][0]
    for i in range(c-1):
        a[r-1][i] = a[r-1][i+1]
    for i in range(r-2, s2-1, -1):
        a[i+1][c-1] = a[i][c-1]
    for i in range(c-2, -1, -1):
        a[s2][i+1] = a[s2][i]
    a[s2][1] = 0

def solve():
    for _ in range(t):
        diffuse()
        purify()
    print(sum(map(sum, a))+2)

for i in range(r):
    for j in range(c):
        if a[i][j] == -1:
            if s1 == -1:
                s1 = i
            else:
                s2 = i
solve()