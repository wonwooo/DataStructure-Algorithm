from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [1, -1 ,0, 0]
dy = [0, 0, 1, -1]
islands = []

def bfs(x, y, num):
    global visited
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    a[x][y] = num
    ls = [(x, y)]
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy+dy[k]
            if nx<0 or nx >= n or ny<0 or ny >= m:
                continue
            if a[nx][ny] and not visited[nx][ny]:
                a[nx][ny] = num
                visited[nx][ny] = True
                q.append((nx, ny))
                ls.append((nx, ny))
    islands.append(ls)

num = 1
for i in range(n):
    for j in range(m):
        if a[i][j] and not visited[i][j]:
            bfs(i, j, num)
            num += 1

edges = []
for i in range(1, num): #이렇게 edge를 구하는 게 가장깔끔하다..! 복잡한 for문으로 구하지 말자
    for x, y in islands[i-1]:
        for k in range(4):
            cnt = 0
            cx, cy = x, y
            while True:
                nx, ny = cx + dx[k], cy+ dy[k]
                if nx<0 or nx>=n or ny<0 or ny>=m or a[nx][ny] == i:
                    break
                if a[nx][ny] == 0:
                    cnt += 1
                    cx, cy = nx, ny
                    continue
                if a[nx][ny] != 0 and a[nx][ny] != i:
                    if cnt >= 2:
                        if not (cnt, i, a[nx][ny]) in edges:
                            edges.append((cnt, i, a[nx][ny]))
                    break

parents = {i:i for i in range(1, num)}
edges.sort()
def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node]) #path compression
    return parents[node]

def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)
    if parent1 > parent2:
        parents[parent1] = parent2
    else:
        parents[parent2] = parent1

answer = 0
for dist, node1, node2 in edges:
    if find(node1) != find(node2):
        union(node1, node2)
        answer += dist

check = [find(i) for i in range(1, num)]
if len(set(check)) == 1:
    print(answer)
else:
    print(-1)


