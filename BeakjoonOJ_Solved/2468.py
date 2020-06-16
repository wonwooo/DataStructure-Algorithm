from collections import deque
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
max_ = 0
for i in range(n):
    for j in range(n):
        max_ = max(a[i][j], max_)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global visited
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if nx<0 or nx>=n or ny<0 or ny >= n: #또 여기서실수..
                continue
            if not visited[nx][ny] and b[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return


answer = 0
for h in range(max_+1):
    b = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[i][j] = a[i][j] if a[i][j] > h else 0

    count = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if b[i][j] and not visited[i][j]:
                count += 1
                bfs(i,j)
    answer = max(answer, count)
print(answer)

'''
copy해서 새로운 배열 b 만들어놓고 뒤에서 생각없이 a참조하는점
nx, ny할때 index벗어남 처리 잊는거

'''