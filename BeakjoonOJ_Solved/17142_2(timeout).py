import copy
from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
empty = []
enum = 0
viruses = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            empty.append((i,j))
            enum += 1
        if a[i][j] == 2:
            viruses.append((i,j))
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def spread(cand):
    global a, enum
    #바이러스를 우선 cand에 맞게 배치
    spreaded_num = 0

    visited = [[-1]*n for _ in range(n)]

    q = deque()
    for cx, cy in cand:
        q.append((cx, cy))
        visited[cx][cy] = 0
    mtime = 0
    while q:
        if enum == spreaded_num:
            break
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx+dx[k], cy+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if a[nx][ny] != 1 and visited[nx][ny] == -1:
                if a[nx][ny] == 0:
                    spreaded_num += 1
                visited[nx][ny] = visited[cx][cy] + 1
                mtime = visited[cx][cy] + 1
                q.append((nx,ny))


    if enum == spreaded_num:
        return mtime
    else:
        return -1





def go(idx, cand):
    global answer
    global viruses
    if len(cand) == m:
        time = spread(cand)
        if time != -1:
            answer.append(time)
        return

    if idx < len(viruses):
        x, y = viruses[idx]
        a[x][y] = 0
        go(idx+1, cand + [viruses[idx]])
        a[x][y] = 2
        go(idx+1, cand)
    return

answer = []
go(0, [])
print(min(answer) if answer else -1)


'''

바이러스를 유출
활성/ 비활성 상태가 있다.
처음 모든 바이러스는 비활성
활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시 복제되며 1초가 걸린다
바이러스 중 m개를 활성 상태로 변경하려 한다

연구소는 크기가 n*n인 정사각형
빈 칸/ 벽/ 바이러스
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다

*비활성 바이러스가 활성되지 않아도 빈 칸으로 모두 퍼졌다면 전염이 완료된다

[입력]
첫줄에 연구소 크기 N (4이상 50이하)
놓을 바이러스 M(1이상 10이하)
둘째줄부터 N개의 줄에 연구소 상태(0빈칸 1벽 2바이러스)
2의 갯수는 M이상 10이하

[출력]
모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다
바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우 -1

[설계]

바이러스 3개가 정해졌다면
BFS를 한번(1초) 진행 할 때마다 빈 칸이 모두 없어졌는지 확인해야 한다
0초부터 빈칸이 없을 수 있으므로 바로 체크한다
그러기위해서 처음에 빈칸들의 위치를 LIST로 기록하고 , BFS에서 바이러스 전염 시킬때마다 
해당 좌표 remove한다
그럼 list가 비어있는지만 체크하면 되니까 2중for문으로 빈칸탐색 할 필요 없다 
bfs가 모두 끝나도 list가 남아있다면, 이렇게 놓아서는 모두 퍼뜨릴 수 없는 경우이므로
answer =[]에 추가하지 않는다

함수는 바이러스 조합 만드는 재귀함수 + spread함수(bfs) 2개 구현
재귀함수 내부에서 벽이 3개가 완성 '되면' spread에 벽위치 넘기고 퍼지는 시간을 받아서 answer에 넣는다
시간이 -1이면 추가하지 않고 그외에 추가한다 

모든 바이러스의 조합에 대해서 answer = []이라면 -1출력 아니면 min값출력

'''