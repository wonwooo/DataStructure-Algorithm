from itertools import combinations

n, m, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
e = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            e.append((i,j))

def play(archers):
    enemy = e[:]
    count = 0
    archers = [(n, c) for c in archers]
    while True:
        #적제거
        eToRemove = []
        for ax, ay in archers:
            cand = []
            for ex, ey in enemy:
                dist = abs(ax-ex) + abs(ay-ey)
                if dist <= d:
                    cand.append((dist, ey, ex))
            if cand:
                cand.sort()
                r, c = cand[0][2], cand[0][1]
                eToRemove.append((r, c))
        eToRemove = set(eToRemove)
        count += len(eToRemove)
        for x, y in eToRemove:
            enemy.remove((x, y))
        tmp = []
        for ex, ey in enemy:
            if ex != n-1:
                tmp.append((ex+1, ey))
        if not tmp:
            return count
        enemy = tmp

arcsets = list(combinations(range(m), 3))

answer = 0
for archers in arcsets:
    answer = max(answer, play(archers))
print(answer)