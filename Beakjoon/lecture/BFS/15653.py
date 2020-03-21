'''
BFS와 DFS는 임의의 정점에서 시작하여 모든 정점을 1번씩 방문하는 목적이 동일한데 방문 방법이 다르다.
BFS는 방문 특성 상 최단거리를 구할 수 있는 문제에 사용이 가능하다. 단 정점을 잇는 간선의 가중치가 1이라는 조건이 필요하다.
따라서 BFS로 문제를 푸는것은 그래프문제를 풀어야 하는 것이므로 그래프 문제임을 파악하고, 정점과 간선이 무엇인지 파악하고 스스로 만들어 풀어야 한다.
문제에 나와있는 정보를 정점과 간선으로 나타내고 가중치가 어떤것인지 찾아본다. 가중치가 1이라면 BFS를 이용한다.

BFS - 구슬탈출 4 문제
'최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지' 에서 BFS임을 캐치하는것이 좋다
구슬을 기울이면, 구슬의 상태가 변한다는 점을 이용해서 GRAPH로 만든다


보드의 상태는 빈칸, 벽, 구멍, 구슬인데, 앞의 3가지는 어떻게 해도 변하지 않고, 구슬만 위치가 변한다.
따라서 빨간 구슬과 파란구슬의 위치가 정점이 되고, 구슬의 이동은 간선을 타고 다른 정점으로 이동하는 것이 된다.

5 5
#####
#..B#
#.#.#
#RO.#
#####
'''
from collections import deque
import copy
dx = [0,0, 1, -1]
dy = [1,-1,0,0]
def simulate(a, k, x, y):
    if a[x][y] == '.':
        return (False, False, x, y)
    n = len(a)
    m = len(a[0])
    moved = False
    while True:
        nx, ny = x + dx[k], y+dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return (moved, False, x, y)
        if a[nx][ny] == '#':
            return (moved, False, x, y)
        elif a[nx][ny] in 'RB':
            return (moved, False, x, y)
        elif a[nx][ny] == '.':
            a[x][y], a[nx][ny] = a[nx][ny], a[x][y]
            x, y = nx, ny
            moved = True
        elif a[nx][ny] == '0':
            a[x][y] = '.'
            moved = True
            return (moved, True, x, y)

def go(b, rx, ry, bx, by, direction):
    a = copy.deepcopy(b)
    a[rx][ry] = 'R'
    a[bx][by] = 'B'
    hole1 = False
    hole2 = False
    while True:
        rmoved, rhole, rx, ry = simulate(a, direction, rx, ry)
        bmoved, bhole, bx, by = simulate(a, direction, bx, by)
        if not rmoved and not bmoved:
            break
        if rhole:
            hole1 = True
        if bhole:
            hole2 = True
    return (hole1, hole2, rx, ry, bx, by)

n,m = map(int, input().split())
a = [list(input()) for _ in range(n)]
d = [[[[-1]* m for k in range(n)] for j in range(m)] for i in range(n)] #m x n 을 m x n 개 만듦
ans = -1
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == '0':
            hx, hy = i,j
        elif a[i][j] == 'R':
            rx, ry = i,j
            a[i][j] = '.'
        elif a[i][j] == 'B':
            bx, by = i,j
            a[i][j] = '.'
q.append((rx, ry, bx, by))
d[rx][ry][bx][by] = 0
found = False
while q:
    rx, ry, bx, by = q.popleft()
    for k in range(4): #k는 기울임 4방향
        hole1, hole2, nrx, nry, nbx, nby = go(a, rx, ry, bx, by, k)
        '''
        여기서 return되는 nrx, nry, nbx, nby는  rx, ry, bx, by의 인접 노드가 된다.
        '''
        if hole2:
            continue
        if hole1: #hole1에서 안걸리면, 반환받은 (nrx, nry, nbx, nby) 정점을 이용해서 탐색을 계속 해 나가야한다.
            found = True
            ans = d[rx][ry][bx][by] + 1
            break
        if d[nrx][nry][nbx][nby] != -1: #윗줄의 hole1에서 안걸렸는데 처음 방문도 아니므로 pass
            continue
        q.append((nrx, nry, nbx, nby))
        d[nrx][nry][nbx][nby] = d[rx][ry][bx][by] + 1 #이 정점이 몇번째 방문이었는지 기억한다.
    if found:
        break
print(ans)