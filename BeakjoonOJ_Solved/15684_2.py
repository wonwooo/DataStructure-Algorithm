import copy
import sys
sys.setrecursionlimit(10000)
n, m ,h = map(int, input().split())
l = [[False]*n for _ in range(h)]
for _ in range(m):
    r, c = map(int, input().split())
    l[r-1][c-1] = 'L'
    l[r-1][c] = 'R'


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
def go(count,idx):
    global answer
    if count > answer:
        return
    if play(l):
        answer = min(count, answer)
    if count == 3:
        return

    if idx < n*h:
        x = idx // n
        y = idx % n

        if y < n-1 and not l[x][y] and not l[x][y+1]:
            l[x][y], l[x][y+1] = 'L', 'R'
            go(count+1, idx+2)
            l[x][y], l[x][y+1] = False, False
        go(count, idx+1)
    return

go(0, 0)
print(answer if answer<4 else -1)
