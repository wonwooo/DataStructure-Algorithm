'''
locs 따로 설정 안하면 시간초과 나는데 얼마나 크길래 시간초과 나는지 check해볼것
시간 초과 나는 이유는 상어의 이동에서 for문을 쓰는것
속도가 1000까지 가기 때문이다
이동 시간초과 해결했는데 틀린이유 찾기
'''

import copy
r, c, m = map(int, input().split())
a = [[[] for _ in range(c)] for _ in range(r)]
locs = []
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    a[x-1][y-1].append((z, d-1, s))
    locs.append((x-1, y-1))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
changedir = {0:1, 1:0, 2:3, 3:2}
#0북 1남 2동 3서

catched = []
for p in range(c):
    #상어잡기
    for i in range(r):
        if a[i][p]:
            catched.append(a[i][p][0])
            a[i][p] = []
            locs.remove((i,p))
            break

    b = [[[] for _ in range(c)] for _ in range(r)]
    tmp = []
    for x, y in locs:
        size, d, speed = a[x][y][0]
        if d in [0,1]: #이부분을 놓쳐서 실수함. 방향에 따라 나누어 주는 거리가 달라져야 한다.
            dist = speed % (2*(r-1))
        else:
            dist = speed % (2*(c-1))
        for _ in range(dist): #c-1의 2배로 나눠준 나머지만큼만 움직여주면 된다
            nx, ny = x+dx[d], y+dy[d]
            if nx<0 or nx>=r or ny<0 or ny>=c:
                d = changedir[d]
                nx, ny = x+dx[d], y+dy[d]
            x, y = nx, ny
        tmp.append((x, y))
        b[x][y].append((size, d, speed)) #tuple넣을때 괄호 안치고 넣는 습관 고치기
    locs = list(set(tmp))
    for x, y in locs:
        if len(b[x][y]) >1:
            b[x][y] = [sorted(b[x][y])[-1]] #[-1]을 sorted안에 넣어버리면어떻게해..
    a = b


answer = 0
for shark in catched:
    answer += shark[0]

print(answer)