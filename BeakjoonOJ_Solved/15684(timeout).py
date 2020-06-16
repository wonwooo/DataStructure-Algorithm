import copy
import sys
sys.setrecursionlimit(10000)
n, m ,h = map(int, input().split())
l = [[False]*n for _ in range(h)]
visited =[[False]*n for _ in range(h)]
for _ in range(m):
    r, c = map(int, input().split())
    l[r-1][c-1] = 'L'
    l[r-1][c] = 'R'


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def play(lad):
    for i in range(n):
        x, y = 0, i
        while x < h:

            if lad[x][y] == 'L':
                y += 1
            elif lad[x][y] == 'R':
                y -= 1
            x += 1
        if y != i:
            return False
    return True

answer = 4
def go(cand,idx):
    global answer
    if len(cand) >= answer:
        return

    b = copy.deepcopy(l)

    for x, y in cand:
        b[x][y], b[x][y+1] = 'L', 'R'
    if play(b):

        answer = min(len(cand), answer)

    if idx < n*h:
        x = idx // n
        y = idx % n
        if y < n-1 and not l[x][y] and not l[x][y+1]:
            go(cand + [(x, y)], idx+2)
        go(cand, idx+1)

go([], 0)
print(answer if answer<4 else -1)
