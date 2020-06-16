import sys
sys.setrecursionlimit(100000)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x, y, c, group):
    if a[x][y] == '.':
        return
    if c[x][y]:
        return
    c[x][y] = True
    group.append((x,y))
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            dfs(nx,ny,c,group)
def simulate():
    c = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if a[x][y] == '.':
                continue
            if c[x][y]:
                continue
            group = []
            dfs(x,y,c,group)
            low = [-1]*m
            for gx,gy in group:
                low[gy] = max(low[gy],gx)
                a[gx][gy] = '.'
            lowest = n
            for j in range(m):
                if low[j] == -1:
                    continue
                i = low[j]
                while i < n and a[i][j] == '.':
                    i += 1
                lowest = min(lowest, i-low[j]-1)
            for gx,gy in group:
                gx += lowest
                a[gx][gy] = 'x'
                c[gx][gy] = True
n,m = map(int,input().split())
a = [list(input()) for _ in range(n)]
k = int(input())
heights = list(map(int,input().split()))
for i,height in enumerate(heights):
    height = n-height
    if i%2 == 0:
        for j in range(m):
            if a[height][j] == 'x':
                a[height][j] = '.'
                break
    else:
        for j in range(m-1, -1, -1):
            if a[height][j] == 'x':
                a[height][j] = '.'
                break
    simulate()
for row in a:
    print(''.join(row))
