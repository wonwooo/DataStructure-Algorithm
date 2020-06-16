'''
테케는 다 맞는데 왜 틀리는지 아직 못찾았다.. 꼭 찾아보기
'''

from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
num = 1
visited = [[False]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y ,num):
    global a
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    a[x][y] = num
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if a[nx][ny] and not visited[nx][ny]:
                a[nx][ny] = num
                visited[nx][ny] = True
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if a[i][j] != 0 and not visited[i][j]:
            bfs(i, j, num)
            num += 1

num -= 1
edges = []
def find_edges(arr):
    global edges
    for row in arr:
        count = 0
        before = -1
        for i in range(len(row)):
            if row[i] == 0:
                count += 1
            elif row[i] != 0:
                if before == -1:
                    before = row[i]
                    count = 0
                    continue
                if row[i] != before:
                    if count >= 2:
                        edges.append((count, before, row[i]))
                        before = row[i]
                        count = 0
                    else:
                        before = row[i]
                        count = 0

find_edges(a)
a_t = [[a[i][j] for i in range(n)] for j in range(m)]
find_edges(a_t)
edges = list(set(edges))
edges.sort()
#print(edges)


parents = {i:i for i in range(1, num+1)}
#rank필요없음
def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(node1, node2):
    global parents
    p1 = find(node1)
    p2 = find(node2)
    if p1 > p2:
        parents[p1] = p2
    else:
        parents[p2] = p1

answer = 0
for dist, node1, node2 in edges:
    if find(node1) != find(node2):
        union(node1, node2)
        answer += dist

parentset = set([find(i) for i in range(1, num+1)]) #연결 되었는지 확인

print(answer if len(parentset) == 1 else -1)
