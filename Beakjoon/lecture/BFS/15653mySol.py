'''
빨간구슬, 파란구슬의 위치를 정점으로 하는 BFS구현
4가지 방향의 기울이기를 통해 인접한 정점으로간다.
정점 이동 할 때마다 방문배열에 몇 번의 이동을 통해 왔는지(깊이)를 기록한다
더 이상 구슬이 이동하지 않으면 탐색을 마친다(4방향 시뮬레이션 결과 구슬의 이동이 없을때)

'''
import copy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
visited = [[[[-1]*m for _ in range(n)] for j in range(m)] for i in range(n)]#m*n*m*n
for i in range(n):
    for j in range(m):
        if a[i][j] == 'O':
            hi, hj = i,j
            a[i][j] == '.'
        if a[i][j] == 'R':
            rx, ry = i, j
            a[i][j] = '.'
        if a[i][j] == 'B':
            bx, by = i, j
            a[i][j] = '.'

def simulation(a, rx, ry, bx, by, k):
    '''
    계속 진행하다가 벽 # 를 만나면 끝
    R,B가 연속으로 붙어있을 때 처리하는 방법은 일단 앞에 있으면 멈추고 둘다 moved = False일때까지 while문을 돌리는것
    '''
    b = copy.deepcopy(a)
    b[rx][ry] = 'R'
    b[bx][by] = 'B'
    rmoved, bmoved = True, True
    rhole = False
    bhole = False
    while True:
        if not rmoved and not bmoved:
            break
        nrx, nbx = rx + dx[k], bx + dx[k]
        nry, nby = ry + dy[k], by + dy[k]


        if (nrx,nry) == (hi, hj):
            rhole = True
            rmoved = True
            b[rx][ry] = '.'  #공 빠짐처리
            rx, ry = nrx, nry

        if b[nrx][nry] == '.':
            rmoved = True
            b[nrx][nry], b[rx][ry] = b[rx][ry], b[nrx][nry]
            rx, ry = nrx, nry

        if b[nrx][nry] == '#':
            rmoved = False
            rx, ry = rx, ry
        if b[nrx][nry] == 'B':
            rmoved = False
            rx, ry = rx, ry
        #파란공
        if (nbx, nby) == (hi, hj):
            bhole = True
            bmoved = True
            b[bx][by] = '.' #공 빠짐처리
            bx, by = nbx, nby
        if b[nbx][nby] == '.':
            bmoved = True
            b[nbx][nby], b[bx][by] = b[bx][by], b[nbx][nby]
            bx, by = nbx, nby
        if b[nbx][nby] == '#':
            bmoved = False
            bx, by = bx, by
        if b[nbx][nby] == 'R':
            bmoved = False
            bx, by = bx, by
    return rhole, bhole, rx, ry, bx, by

def go(a, rx, ry, bx, by):
    global visited
    q=[]
    q.append((rx, ry, bx, by))
    visited[rx][ry][bx][by] = 0
    while q:
        rx, ry, bx, by = q.pop(0)
        for k in range(4):
            rhole, bhole, nrx, nry, nbx, nby = simulation(a, rx, ry, bx, by, k)
            if bhole:
                continue
            if rhole:
                visited[nrx][nry][nbx][nby] = visited[rx][ry][bx][by] + 1
                break
            if visited[nrx][nry][nbx][nby] != -1: #이동이 불가능하면 위치 변화가 없을것이고 que에 들어가지 않고 pop만 반복되다가 자연스레 끝난다.
                continue
            else:
                visited[nrx][nry][nbx][nby] = visited[rx][ry][bx][by] + 1
                q.append((nrx,nry, nbx, nby))



go(a, rx, ry, bx, by)
ans = -1
for i in range(n):
    for j in range(m):
        if visited[hi][hj][i][j] != -1:
            ans = visited[hi][hj][i][j]
print(ans)








