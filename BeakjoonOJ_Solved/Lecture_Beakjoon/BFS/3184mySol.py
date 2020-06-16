'''
여러 개의 구역이 있는데, 구역마다 양과 늑대가 몇마리씩 있는지 알아내야 한다.
BFS를 사용하여 알아낼 수도 있고, DFS를 사용하여 알아낼 수도 있지만
핵심은 : 탐색함수에 위치를 전달하면, 그 위치가 포함 된 구역을 모두 탐색하고 구역 내 좌표가 모두 방문처리 되면서 늑대와 양의 갯수를 세도록 해야한다.
그래서 2중 for문을 통해 탐색을 할때 방문처리가 되어있으면 이미 탐색이 끝난 구역임을 알고 넘어갈 수 있어야 한다.
'''


r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global visited
    ov = [0, 0]
    q = []
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.pop(0)
        if a[x][y] in 'ov':
            if a[x][y] == 'o':
                ov[0] += 1
            else:
                ov[1] += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx<0 or nx >= r or ny<0 or ny >= c:
                continue
            if visited[nx][ny]:
                continue
            if a[nx][ny] == '#':
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
    return ov

remain = []
for i in range(r):
    for j in range(c):
        if not visited[i][j] and a[i][j] != '#':
            ov = bfs(i,j)
            remain.append(ov)

o, v = 0,0
for ov in remain:
    if ov[0] > ov[1]:
        o += ov[0]
    else:
        v += ov[1]

print(o,v)




