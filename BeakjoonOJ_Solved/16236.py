'''
더 큰 물고기들한테 막혀서 해당 물고기에게 갈 수 없는 경우를 생각 못했다..
진짜 욕나온다 꼼꼼하게 생각해야함
'''

from collections import deque


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
shark = {'loc':0, 'size':2, 'ate':0}
fishes = {}
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            if a[i][j] == 9:
                shark['loc'] = [i,j]
                a[i][j] = 0
            else:
                if not a[i][j] in fishes:
                    fishes[a[i][j]] = [[i,j]]
                else:
                    fishes[a[i][j]].append([i,j])

def distance(arr, size, shark, fish):
    n = len(arr)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0]*n for _ in range(n)]
    sx, sy = shark
    fx, fy = fish
    q = deque()
    q.append([sx, sy])
    while q:

        sx, sy = q.popleft()
        for k in range(4):
            nx, ny = sx + dx[k], sy + dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny] and arr[nx][ny] <= size:
                visited[nx][ny] = visited[sx][sy] + 1
                q.append([nx,ny])
    return visited[fx][fy]



time = 0
while True:


    candidates = {}
    for size, locs in fishes.items():
        if size < shark['size'] and locs:
            for loc in locs:
                dist = distance(a, shark['size'], shark['loc'], loc)
                if dist != 0:
                    if not dist in candidates:
                        candidates[dist] = [loc]
                    else:
                        candidates[dist].append(loc)

    if not candidates:
        break
    mdist = min(candidates.keys())
    x, y = sorted(candidates[mdist])[0]
    fishes[a[x][y]].remove([x, y])
    a[x][y] = 0
    shark['loc'] = [x, y]
    shark['ate'] += 1
    if shark['size'] == shark['ate']:
        shark['size'] += 1
        shark['ate'] = 0
    time += mdist

print(time)




