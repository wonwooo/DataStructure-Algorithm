import copy
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')
def calc(x, y, d1, d2, b):
    global answer
    boundary = {x:[] for x in range(x, x+d1+d2+1)}
    for diff in range(d1):
        boundary[x+diff].append(y-diff)
        boundary[x+d2+1+diff].append(y+d2-1-diff)
    for diff in range(d2):
        boundary[x+d1+diff].append(y-d1+diff)
        boundary[x+1+diff].append(y+1+diff)
    pops = [0]*5
    for r, section in boundary.items():
        for c in range(min(section), max(section)+1):
            pops[4] += b[r][c]
            b[r][c] = 0

    #1,2,3,4구역 합산
    for r in range(n):
        for c in range(n):
            if b[r][c]:#0이 아니면 5구역이 아님
                if 0<=r<x+d1 and 0<=c <=y:
                    pops[0] += b[r][c]
                elif 0<=r<=x+d2 and y<c<=n-1:
                    pops[1] += b[r][c]
                elif x+d1<=r<=n-1 and 0<=c<y-d1+d2:
                    pops[2] += b[r][c]
                elif x+d2<r<=n-1 and y-d1+d2<=c<=n-1:
                    pops[3] += b[r][c]

    answer = min(answer, (max(pops) - min(pops)))







for x in range(n):
    for y in range(n):
        for d1 in range(1, y+1):
            for d2 in range(1, n-y):
                if x + d1 + d2 < n:
                    calc(x, y, d1, d2, copy.deepcopy(a))
print(answer)

