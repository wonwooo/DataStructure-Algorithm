from collections import deque
import copy


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
viruses = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            viruses.append((i,j))


def spread(b, cand):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    for i in range(n):
        for j in range(n):
            if b[i][j] ==0:
                b[i][j] = -1
            if b[i][j] ==1:
                b[i][j] = '-'
    deact = []
    for i, virus in enumerate(viruses):
        x, y = virus
        if i in cand:
            b[x][y] = 0
            q.append((x, y))
        else:
            b[x][y] = -1
            deact.append((x, y))
    maxtime = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if b[nx][ny] == -1:
                b[nx][ny] = b[x][y] + 1
                if b[nx][ny] > maxtime:
                    maxtime = b[nx][ny]
                q.append((nx, ny))

    '''
    checklist = []
    for i in range(len(b)):
        checklist += b[i]

    if not -1 in checklist:
        time = max([t for t in checklist if not t in ['-', '*']])
        break
    '''

    check = True
    maxlist = []
    for i in range(n):
        for j in range(n):
            if b[i][j] == -1:
                check = False
                #2중 for문에서 break잘쓸것..여기서 break하면 나머지 i,j에 대해서는 아래에 있는 조건문 check할 수가 없다
            elif b[i][j] == maxtime:
                if not (i,j) in deact:
                    maxlist.append((i,j))
    if not check:
        return -1
    else:
        if maxlist:
            return maxtime
        else:
            return maxtime-1



    #다 퍼트리고도 False이 있다면 -1 return


def go(idx, cand):
    global times
    if len(cand) == m:
        time = spread(copy.deepcopy(a), cand)
        if time != -1:
            times.append(time)
        return
    if idx < len(viruses):
        go(idx+1, cand+[idx])
        go(idx+1, cand)
    return

empty = False
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] == 0:
            empty = True

if empty:
    times = []
    go(0, [])
    if not times:
        print(-1)
    else:
        print(min(times))
else:
    print(-1)
