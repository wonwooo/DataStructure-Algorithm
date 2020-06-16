'''
1. 바이러스 위치, 벽을 놓을 수 있는 후보위치 저장
2. go() ; 후보군에 대해서 3개의 벽을 모두 놓아보면서 ans(최댓값) 갱신
'''

import copy
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cand = []
virus = []
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            cand.append((i,j))
        if a[i][j] == 2:
            virus.append((i,j))

def spread(b, vx, vy):
    for k in range(4):
        nx, ny = vx+dx[k], vy+dy[k]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if b[nx][ny] == 1 or b[nx][ny] == 2:
            continue
        b[nx][ny] = 2
        spread(b, nx, ny)

def count(a, wall):
    b = copy.deepcopy(a)
    for (x, y) in wall:
        b[x][y] = 1
    for (vx, vy) in virus:
        spread(b, vx, vy)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt

def go(a, cand, wall, cnt, idx): #cand(빈칸들), wall(벽세운곳), cnt(벽갯수) idx(cand내부 진행상황)
    global ans
    if cnt != 3 and idx == len(cand):
        return
    if cnt == 3:
        tmp = count(a, wall)
        if tmp > ans:
            ans = tmp
        return
    go(a, cand, wall + [cand[idx]], cnt + 1, idx + 1)
    go(a, cand, wall, cnt, idx + 1)

go(a, cand, [], 0, 0)
print(ans)






