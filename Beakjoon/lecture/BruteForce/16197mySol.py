
def go(cx1, cy1, cx2, cy2, cnt):

    if cnt > 10:
        return -1
    c1 = True
    c2 = True
    if cx1 < 0 or cx1 > n - 1 or cy1 < 0 or cy1 > m - 1:
        c1 = False
    if cx2 < 0 or cx2 > n - 1 or cy2 < 0 or cy2 > m - 1:
        c2 = False
    if c1 + c2 == 1:
        return cnt
    if c1 + c2 == 0:
        return -1
    ans = -1
    for k in range(4):
        nx1, nx2 = cx1 + dx[k], cx2 + dx[k]
        ny1, ny2 = cy1 + dy[k], cy2 + dy[k]
        # and 앞 조건문으로 index error 안잡히게 하는 부분 중요
        if 0 <= nx1 < n and 0 <= ny1 < m and a[nx1][ny1] == '#':
            nx1, ny1 = cx1, cy1
        if 0 <= nx2 < n and 0 <= ny2 < m and a[nx2][ny2] == '#':
            nx2, ny2 = cx2, cy2

        tmp = go(nx1, ny1, nx2, ny2, cnt+1)
        if tmp == -1:
            continue
        if tmp < ans or ans == -1:
            ans = tmp
    return ans

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
coins = []

for i in range(0,n):
    for j in range(0,m):
        if a[i][j] == 'o':
            coins.append((i, j))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

cx1, cy1 = coins[0]
cx2, cy2 = coins[1]

print(go(cx1, cy1, cx2, cy2, 0))
