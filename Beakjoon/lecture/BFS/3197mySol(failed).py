'''
런타임 에러 원인 못찾음

'''
def melt(a):
    newWater = []
    for x in range(n):
        for y in range(m):
            if a[x][y] == '.':
                continue
            for k in range(4):
                nx , ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == '.':
                        newWater.append((x, y))

    for x, y in newWater:
        a[x][y] = '.'

    return a

def mark(a, sx1, sy1):
    global visited

    for k in range(4):
        nx, ny = sx1 + dx[k], sy1 + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and a[nx][ny] == '.':
                visited[nx][ny] = True
                mark(a, nx, ny)
    return

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
sx1, sy1, sx2, sy2 = -1,-1,-1,-1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            if sx1 == -1:
                sx1, sy1 = i, j
                a[sx1][sy1] = '.'
            else:
                sx2, sy2 = i, j
                a[sx2][sy2] = '.'




ans = 0
while True:
    
    visited = [[False]*m for _ in range(n)]
    mark(a, sx1, sx2)

    if visited[sx2][sy2]:
        print(ans)
        break
    a = melt(a)
    ans += 1


