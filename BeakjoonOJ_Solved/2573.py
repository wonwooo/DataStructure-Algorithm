from collections import deque
import copy
n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ices = []
for i in range(n):
    for j in range(m):
        if a[i][j]:
            ices.append((i,j))


visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    global count
    global visited
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if a[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))

time = 0

while ices: #가장 큰 빙산의 크기만큼 시간이 지나는것이 모든 빙산이 녹는 조건이 아닌데 착각했다. 문제 조건 그대로 빙산이 모두 녹는지를 넣으면 된다.
    count = 0
    visited = [[False]*m for _ in range(n)] #visited 배열 매번 초기화 하는것 잊지말것
    for x, y in ices:
        if not visited[x][y]:
            count += 1
            bfs(x, y)
    if count >= 2: #두 덩어리 '이상' 이었음..
        break

    #녹이기
    b = copy.deepcopy(a)
    remain = []
    for x, y in ices:
        num = 0
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if a[nx][ny] == 0:
                num +=1
        if num >= a[x][y]:
            b[x][y] = 0
        else:
            b[x][y] = a[x][y] - num
            remain.append((x, y))
    a = b
    ices = remain
    time += 1

print(time if ices else 0)



'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''


'''
5 5
0 0 0 0 0
0 3 2 0 0
0 3 0 6 0
0 5 1 5 0
0 0 0 0 0
'''