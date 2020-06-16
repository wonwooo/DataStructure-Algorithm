from collections import deque

n, m, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
rotations = [list(map(int, input().split())) for _ in range(t)]

def rotate(ls, dir, k):
    n = len(ls)
    if dir == 0:
        ls = ls[n-k:] + ls[:n-k]
    if dir == 1:
        ls = ls[k:] + ls[:k]
    return ls

def erase(x, y):
    global visited
    global a
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()

    sx, sy = x, y
    q.append((x, y))
    ls = []
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], (y+dy[k])%m #여기 나누기 4로 했었음... 열길이 m으로 했어야함
            if nx<0 or nx>=n:
                continue
            if a[nx][ny] == a[x][y] and not visited[nx][ny]:
                ls.append((nx, ny))
                visited[nx][ny] = True
                q.append((nx, ny))
    if ls:
        for i, j in ls:
            a[i][j] = 0
        a[sx][sy] = 0
        return True
    else:
        return False

for ro in rotations:
    x, dir, k = ro
    for i in range(x-1, n, x):
        a[i] = rotate(a[i], dir, k)
    #다돌린후에
    visited = [[False] * m for _ in range(n)]
    erased = False
    empty = True
    for i in range(n):
        for j in range(m):
            if a[i][j] != 0 and not visited[i][j]:
                empty = False
                visited[i][j] = True
                if erase(i, j):
                    erased = True #i,j 탐색하면서 어느 한곳에서라도 지워진게 있다면 True처리

    if not erased and not empty: #원판에 수가 남아있는데 지워지지 않은 경우
        s = []
        nonempty = []
        for i in range(n):
            for j in range(m):
                if a[i][j] != 0:
                    nonempty.append((i,j))
                    s.append(a[i][j])
        mean_ = sum(s) / len(s)
        for i, j in nonempty:
            if a[i][j] > mean_:
                a[i][j] -= 1
            elif a[i][j] < mean_: #eilf 쓰는거 매우중요..if썻다가 디버깅 한참..
                a[i][j] += 1


s = 0
for i in range(n):
    s += sum(a[i])
print(s)