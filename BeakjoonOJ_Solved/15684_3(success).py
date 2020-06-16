
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
    if count > 3:
        return
    if play(l):
        answer = min(count, answer)
    for i in range(idx, n*h):
        x = i // n
        y = i % n
        #포함 하고 안하고에 따라 idx의 증가가 +1, +2로 다른 경우는
        #for문으로 idx를 1씩 증가시키고 재귀함수는 한번만 호출한다(호출 된 다음 for문은 idx부터 탐색한다)
        if y < n-1 and not l[x][y] and not l[x][y+1]:
            l[x][y], l[x][y+1] = 'L', 'R'
            go(count+1, i+2)
            l[x][y], l[x][y+1] = False, False
    return

go(0, 0)
print(answer if answer<4 else -1)
