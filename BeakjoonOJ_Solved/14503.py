'''
로봇 청소기는 다음과 같이 작동한다.

1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

d : 0북 1동 2남 3서
'''
N, M = map(int, input().split()) #행 N 열 M
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

dx = [-1, 0, 1, 0] #0북 1동 2남 3서로 후진할 경우 생각해서 배열함
dy = [0, 1, 0, -1]


def countClean():
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 1:
                count += 1
    return count


def leftTurn(d):
    if d == 0:
        return 3
    else:
        return d-1


def clean(x, y, d, turnCount):
    while True:

        if turnCount == 4: #4방향 탐색 후 뒤가 벽인지 확인후 후진 혹은 종료
            backX = x - dx[d]#후진위치
            backY = y - dy[d]

            if arr[backX][backY] == 1: #뒤가 벽이면
                print(countClean()) #갯수 프린트하고 종료
                return
            else:
                x, y, d, turnCount = backX, backY, d, 0 #벽 아니면 후진한 뒤 turnCount 0으로만들고 아래로 진행

        ## 현위치 청소
        if arr[x][y] == 0:
            arr[x][y] = 2

        #왼쪽탐색
        ld = leftTurn(d)
        nx = x + dx[ld]
        ny = y + dy[ld]

        if arr[nx][ny] == 0:
            x, y, d, turnCount = nx, ny, ld, 0
        else:
            x, y, d, turnCount = x, y, ld, turnCount +1


clean(r, c, d, 0)

