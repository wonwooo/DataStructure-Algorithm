'''
[2146] 다리만들기1

항상 두개 이상의 섬이 있는 데이터만 입력으로 주어진다 .
0바다 1육지. 두 섬을 연결하는 가장 짧은 다리 하나의 길이를 구한다. 섬 개수 관계없이 두 섬 연결하는 가장 짧은 거리만 구하면된다.
N은 100이하

섬을 모두 masking하고, 모든 섬을 차례로 돌면서 해당 섬에서 다른 섬까지의 최단거리를 기록한다.

방법 : 기준 섬의 모든 좌표를 q에 넣고 visited에서 그 좌표는 모두 0처리한다
그리고 bfs를 통해 바다도 아니고, 자기 자신도 아닌 땅이 나오면 visited에 저장 된 방문값을 새로 만난 섬과의 거리로 갱신한다.
dictionary사용하면 쉽게 할 수 있을듯

모든 섬에 대해 탐색이 끝나면 가장 짧은 다리를 출력한다.
'''
from collections import deque
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
islands = []
visited = [[False]*n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, num):
    visited[x][y] = True
    a[x][y] = num
    q = deque()
    q.append((x, y))
    ls = [(x, y)]
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny] and a[nx][ny]:
                a[nx][ny] = num
                visited[nx][ny] = True
                q.append((nx, ny))
                ls.append((nx,ny))
    islands.append(ls)
num = 1
for i in range(n):
    for j in range(n):
        if a[i][j] and not visited[i][j]:
            bfs(i, j, num)
            num += 1

answer = float('inf') #answer를 어설프게 n으로 설정했다가 디버깅했다..n보다 훨씬 큰 값이 답으로 나올 수 있는데.
for i in range(1, num):
    countarray = [[-1] * n for _ in range(n)]
    q = deque()
    for x, y in islands[i-1]:
        q.append((x, y))
        countarray[x][y] = 0
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx+dx[k], cy+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if a[nx][ny] == 0 and countarray[nx][ny] == -1:
                countarray[nx][ny] = countarray[cx][cy] + 1
                q.append((nx, ny))
            elif a[nx][ny] != 0 and countarray[nx][ny] == -1:
                answer = min(answer, countarray[cx][cy])

print(answer)



