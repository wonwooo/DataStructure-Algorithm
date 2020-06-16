#BFS, DFS 둘다 적용 가능

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def can(blind, u, v):
    if u == v:
        return True
    if blind:
        if u == 'R' and v == 'G':
            return True
        if u == 'G' and v == 'R':
            return True
    return False

def go(a, blind):
    n = len(a)
    check = [[False]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                continue
            ans += 1
            q = []
            q.append((i,j))
            check[i][j] = True
            #같은 구역은 while문 돌면서 모두 방문(True) 처리됨.
            while q:
                x, y = q.pop(0)
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if check[nx][ny]:
                            continue
                        if can(blind, a[x][y], a[nx][ny]):
                            check[nx][ny] = True
                            q.append((nx, ny))

    return ans

n = int(input())
a = [input() for _ in range(n)]
print(str(go(a, False)) + ' ' + str(go(a, True)))
