#시뮬레이션 구현문제
'''
문제에 주어진 조건을 그대로 구현하는 문제다. 크게 두 단계로 나눠서 설계해야 한다. 첫 번째, 미세먼지가 확산되는 과정, 두 번째 공기청정기의 바람이 순환하는 과정이다.

1. 모든 미세먼지는 5 이상의 양이 남아있으면, 상하좌우로 확산할 수 있다.
확산할 때 상하좌우에 이미 먼지가 있는 경우가 있으므로, 별도의 배열을 만들어서 확산되는 먼지의 양을 저장해야 한다. 값을 바로 업데이트하면 다음 먼지 확산에 영향을 주기 때문에, 이 과정이 필요하다.
현재 먼지의 양을 5로 나눈 후, 그 양을 상하좌우 칸에 더한다. 위에서 만든 별도의 배열 B에 더한다.
모든 과정이 끝나면, 원래 먼지 배열 A에 확산 배열 B 값을 업데이트한다.

2. 미세먼지가 바람 방향에 따라 순환한다.
입력받을 때 공기청정기의 위치를 S1, S2에 저장한다.
위쪽 공기청정기는 S1을 기준으로 반시계 방향으로 회전한다.
아래쪽 공기청정기는 S2를 기준으로 시계 방향으로 회전한다.
역순으로 회전하면서, 현재 값에 다음 값을 저장하면 된다.

출처: https://rebas.kr/848 [PROJECT REBAS]
'''


#pypy로 통과 ,python3로 통과 못함. 변수명만 바꾸면 python에서도 통과하는데.. 왜 그런지 이해 못함

r, c, t = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(r)]
cleaner1, cleaner2 = -1, 0



def diffuse(): #확산
    global dust
    tmp = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if dust[x][y] >= 5:
                diffusion = dust[x][y]//5
                for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
                    xNew, yNew = x + dx, y + dy
                    if 0<=xNew<=r-1 and 0<=yNew<=c-1 and dust[xNew][yNew] != -1:
                        tmp[xNew][yNew] += diffusion
                        dust[x][y] -= diffusion
    for x in range(r):
        for y in range(c):
            dust[x][y] += tmp[x][y]

def purify():
    #위에서 아래 - 우에서 좌 - 아래에서 위 - 좌에서 우
    for x in range(cleaner1-2, -1, -1): #1번 청정기 위에서 아래
        dust[x+1][0] = dust[x][0]
    for y in range(c-1): #1번 우에서 좌
        dust[0][y] = dust[0][y+1]
    for x in range(cleaner1): #1번 아래에서 위
        dust[x][c-1] = dust[x+1][c-1]
    for y in range(c-2, -1, -1): #번 좌에서 우로 1칸씩 이동
        dust[cleaner1][y+1] = dust[cleaner1][y]
    dust[cleaner1][1] = 0
    for x in range(cleaner2+1, r-1):
        dust[x][0] = dust[x+1][0]
    for y in range(c-1):
        dust[r-1][y] = dust[r-1][y+1]
    for x in range(r-2, cleaner2-1, -1):
        dust[x+1][c-1] = dust[x][c-1]
    for y in range(c-2, -1, -1):
        dust[cleaner2][y+1] = dust[cleaner2][y]
    dust[cleaner2][1] = 0

def solve():
    for _ in range(t):
        diffuse()
        purify()
    print(sum(map(sum, dust))+2)

for x in range(r):
    for y in range(c):
        if dust[x][y] == -1:
            if cleaner1 == -1:
                cleaner1 = x
            else:
                cleaner2 = x
solve()


