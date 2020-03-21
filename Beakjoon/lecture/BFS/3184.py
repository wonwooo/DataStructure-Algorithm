'''
최소값을 구하는 문제가 아니지만, 모든 인접노드를 탐색한다는 점에서 BFS를 사용할 수있다.
물론 DFS도 사용할 수 있다.

BFS를 이용하여 구역을 나누고 구역의 갯수를 구하고 구역마다 양과 늑대의 수를 비교한다.
'''

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(sx, sy):#출발위치. 어느곳에서 시작해도 bfs를 거치면 한 구역 내부가 모두 visited(True)처리된다.
    q = deque()
    q.append((sx, sy))
    check[sx][sy] = True
    cnt = [0,0]
    while q:
        x, y = q.popleft()
        if a[x][y] == 'v':
            cnt[0] += 1
        elif a[x][y] == 'o':
            cnt[1] += 1

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if a[nx][ny] == "#":
                continue
            if check[nx][ny]:
                continue
            q.append((nx, ny))
            check[nx][ny] = True
        #점점 구역내 방문(True)가 많아지면 que에 추가 되는 것 없이 빠지기만 하면서 while문이 종료된다.
    return cnt


n, m = map(int, input().split())
a = [input() for _ in range(n)] #string형태로 입력되기때문에
check = [[False] * m for _ in range(n)]
d = []
for i in range(n):
    for j in range(m):
        if a[i][j] != '#' and not check[i][j]:
            #check[i][j]가 False라는것은 새 구역에 들어왔다는 뜻이다. dfs한번 거치면 구역전체가 True처리되기때문
            d.append(bfs(i,j))
v, o = 0, 0
for cnt in d:
    if cnt[0] >= cnt[1]:
        v += cnt[0]
    else:
        o += cnt[1]
print(f"{o} {v}")
