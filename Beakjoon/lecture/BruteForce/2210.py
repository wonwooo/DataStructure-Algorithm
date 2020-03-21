arr = [list(map(int, input().split())) for _ in range(5)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
numList = []
def go(r, c, cnt, num):
    global arr, numList
    if cnt == 6:
        n = ''
        for e in num:
            n += str(e)
        numList.append(int(n))
        return

    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if nr >= 0 and nc>= 0 and nr <= 4 and nc<=4:
            go(nr, nc, cnt+1, num+[arr[r][c]])

for i in range(5):
    for j in range(5):
        go(i, j, 0, [])

ans = len(set(numList))
print(ans)





