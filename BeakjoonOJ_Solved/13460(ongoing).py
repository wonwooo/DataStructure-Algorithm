'''

충분한 설계의 중요성
구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음
빨간 구슬을 구멍을 통해 빼내는 게임이다
보드의 세로는 N 가로는 M  바깥행 바깥열은 모두 막혀있고,
파란 /빨간 구슬은 1칸을 가득 채우는 사이즈/하나씩 들어가 있다
목표는 빨간 구슬을 구멍을 통해서 빼는것. 단 파란구슬은 구멍에 들어가지 않아야함
구슬을 손으로 건드릴 수는 없고 중력을 이용해 이리저리 굴려야 한다
왼쪽으로, 오른쪽으로 위로, 아래로 4방향으로 기울일 수 있다
공은 동시에 움직이고, 빨간 구슬이 구멍에 빠지면 성공이지만 파란 구슬이 구멍에 빠지면 실패
동시에 구멍에 빠져도 실패.
동시에 같은 칸에 있을 수 없고 동작을 그만하는 건 더이상 구슬이 움직이지 않을 때
보드 상태가 주어졌을 때 '최소' 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지

[입력]
첫 줄에 세로, 가로를 의미하는 N,M이 주어진다 (N은 3이상, M은 10이하)
다음 N줄에 보드의 모양을 나타내는 길이 M의 문자열 '.', '#',, 'O', 'R', 'B' 이 온다
.빈칸 #벽 O구멍 R빨간 R파란
보드의 가장자리에는 모두 벽이 있다 / 구멍은 한개 / 구슬은 각 하나씩

[출력]
최소 몇 번 만에 빨간 구슬을 구멍을 통해 뺄 수 있는지 / 10번 이하로 못빼면 -1

5 5
#####
#..B#
#.#.#
#RO.#
#####

[설계]
'최소'이므로 BFS를 써야한다
빨간 공의 위치가 시작 노드가 되고, 4방향의 기울임으로 변하는 위치가 인접노드가 된다.
4차원 방문배열을 초기화 한다 : [rx][ry][bx][by]를 -1로, 시작 위치만 0으로
그 후 4방향으로 기울이는 simulation을 진행하고, simulation 결과 두 공의 새로운 위치를 구한다
파란 공이 빠진경우 : continue
두 공 모두 빠지는경우 : continue
빨간 공만 빠진 경우 : 이전 방문에서 +1 한 값을 answer로 정하고 break
두 공 모두 빠지지 않은 경우 : 현위치 방문+1처리하고 q에 집어넣기
4방향 bfs가 모두 끝나면 , 어떻게 해도 빨간구슬을 빼지 못한경우 answer가 -1일것이고
아니면 기울임 횟수가 answer가 될텐데 10이 넘어가면 역시 -1을 출력해야 한다.

"simulation 구현"
simulation함수로 인자를 두 공의 위치와 기울임 방향으로 받는다.
bx, by, rx, ry를 기억해둔다.
우선 두 공 모두 해당 방향으로 겹치는 경우 생각하지 말고 굴려 nbx, nby, nrx, nry를 구한다.
굴릴 때 구멍에 걸리면 바로 구멍에 넣는다.
굴리다가 두 공이 모두 구멍에 들어간 경우는 겹치는 경우에서 제외한다.
굴린 다음 위치가 같을 경우엔, 기억했던 두 공의 선후관계에 맞게 한칸 움직여준다.
두 공의 최종 위치를 return 한다.
'''

from collections import deque
n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
visited = [[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)] #여기 선언할때 절대 곱하기(*)로 하지 말것
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'B':
            bx, by = i, j
            a[i][j] = '.'
        if a[i][j] == 'R':
            rx, ry = i, j
            a[i][j] = '.'
        if a[i][j] == 'O':
            ox, oy = i,j

def simulation(rx, ry, bx, by, dir):
    crx, cry = rx, ry#초기위치 기억해둠
    cbx, cby = bx, by
    while True:
        nrx, nry = crx + dx[dir], cry + dy[dir]
        if (nrx, nry) == (ox, oy): #빈칸을 만나면 그 위치를 마지막 위치고 하고 break
            crx, cry = nrx ,nry
            break
        elif a[nrx][nry] == '#': #벽이면 현위치를 마지막 위치고 하고 종료
            break
        crx, cry = nrx, nry

    while True:
        nbx, nby = cbx + dx[dir], cby + dy[dir]
        if (nbx, nby) == (ox, oy):  # 빈칸을 만나면 그 위치를 마지막 위치고 하고 break
            cbx, cby = nbx, nby
            break
        elif a[nbx][nby] == '#':  # 벽이면 현위치를 마지막 위치고 하고 종료
            break
        cbx, cby = nbx, nby

    if (crx, cry) == (cbx, cby): #겹치는 경우
        if (crx, cry) == (ox, oy):
            return crx, cry, cbx, cby
        if rx < bx:#원래 b가 더 아래에 있었다
            if dir == 0: #아래로 내려오다가 겹쳤다
                crx -= 1 #r을 위로 올려준다
            if dir == 1: #위로 올라가다가 겹쳤다
                cbx += 1 #b을 하나 내려준다
        else:#r가 아래있었다
            if dir == 0: #아래로 내려오다가 겹쳤다
                cbx -= 1 #b를 위로
            if dir == 1: #위로 올리다 겹쳤다
                crx += 1 #r을 아래로
        if ry < by: #원래 b가 오른편에 있었다
            if dir == 2: #오른쪽으로 가다가 겹쳤다
                cry -= 1
            if dir == 3: #왼쪽으로 가다가 겹쳤다
                cby += 1
        else:
            if dir == 2:
                cby -= 1
            if dir == 3:
                cry += 1

    return crx, cry, cbx, cby

q = deque()
q.append((rx,ry,bx,by))
visited[rx][ry][bx][by] = 0
done = False
answer = -1
while q:
    rx, ry, bx, by = q.popleft()
    for dir in range(4):
        nrx, nry, nbx, nby = simulation(rx, ry, bx, by, dir)
        if (nbx, nby) == (ox, oy):
            continue
        if (nrx, nry) == (ox, oy):
            answer = visited[rx][ry][bx][by] + 1
            done = True
            break
        else:
            if visited[nrx][nry][nbx][nby] == -1:
                visited[nrx][nry][nbx][nby] = visited[rx][ry][bx][by] + 1
                q.append((nrx, nry, nbx, nby))
    if done:
        break

print(answer if answer <= 10 else -1)
