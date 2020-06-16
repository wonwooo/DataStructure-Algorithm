n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dirchange = {0:1, 1:2, 2:3, 3:0}

def make_curve(c, dirs, g):
    curve = c
    x, y = c[-1]

    '''
    시작점 x, y를 잡는다
    이전의 dirs를 설정한다
    newdirs를 설정한다
    시작점 x, y에서 newdirs만큼 새 점을 만든 addlist를 만든다
    마지막 점은 새로운 시작점 x, y가 된다
    curve에 addlist를 더한다
    dirs에 newdirs를 더해서 dirs를 갱신한다
    
    위 과정을 g번 반복한다    
    '''

    for _ in range(g):
        added = []
        newdir = [dirchange[dir] for dir in dirs[::-1]]
        for d in newdir:
            nx, ny = x+dx[d], y+dy[d]
            added.append((nx, ny))
            x, y = nx, ny
        dirs += newdir
        curve += added

    return curve

total = []
for y, x, dir, g in info: #x가 row가 아님에 주의하자..
    ex, ey = x+dx[dir], y+dy[dir]
    curvelist = make_curve([(x, y), (ex, ey)], [dir], g)
    total += curvelist

total = set(total)
check = [[False]*101 for _ in range(101)]
for i, j in total:
    if i<0 or i>100 or j<0 or j>100:
        continue
    check[i][j] = True
count = 0
for i in range(100):
    for j in range(100): #101로잡으면 runtime error..
        if check[i][j] and check[i+1][j+1] and check[i+1][j] and check[i][j+1]:
            count += 1

print(count)

'''
[설계]
커브를 우선 시작점 0,0으로 만들고 시작점만큼 +r, +c 한 뒤에 격자 안에 들어갈 수있는것만 넣는다
모든 커브의 좌표 합은 set으로 만들어서 최종 체크
1. 커브 생성
시작점 x, y
curve = [(x, y)]

1 이상이면 curve에 시작 끝 넣고 시작
dirs = []
newdirs = [dirs 역순으로 반시계 90도 회전]

#더해야 할 curve 만들기
이전의 end를 start로 잡고 
newdirs 따라가면서 
nx, ny 만들어가면서 added에 추가/갱신

dirs = dirs + newdirs
end기록

make_curve([start, end], [첫 dir], 세대수-1):
 return 생성된 total curve point list

total = []

세대가 0이면 그 점만 total에 추가
세대가 1 이상이면 [start, end]만들어서 make_curve에 전달해서 list 받고 total에 추가

모두 추가해서 set으로 만들고 2차원 배열 탐색후 4방향 모두 있는지 체크


'''