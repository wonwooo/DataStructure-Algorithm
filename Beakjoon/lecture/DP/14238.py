s = input()
n = len(s)
limit = [0, 0, 0]
for ch in s:
    limit[ord(ch)-ord('A')] += 1
d = [[[[[-1]*3 for l in range(3)] for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]

def go(a, b, c, p1, p2):
    ans = d[a][b][c][p1][p2]
    if a+b+c == 0:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]
    if ans != -1:
        return ans
    if a > 0 and go(a-1, b, c, 0, p1) == 1:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]
    if b > 0 and p1 != 1 and go(a, b-1, c, 1, p1) == 1:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]
    if c > 0 and p1 != 2 and p2 != 2 and go(a, b, c-1, 2, p1) == 1:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]
    d[a][b][c][p1][p2] = 0
    return d[a][b][c][p1][p2]

def back(a, b, c, p1, p2):
    if a+b+c == 0:
        return ''
    if a > 0 and go(a-1, b, c, 0, p1) == 1:
        return 'A' + back(a-1, b, c, 0, p1)
    if b > 0 and p1 != 1 and go(a, b-1, c, 1, p1) == 1:
        return 'B' + back(a, b-1, c, 1, p1)
    if c > 0 and p1 != 2 and p2 != 2 and go(a, b, c-1, 2, p1) == 1:
        return 'C' + back(a, b, c-1, 2, p1)
    return ''

ans = go(limit[0], limit[1], limit[2], 0, 0)
if ans == 0:
    print(-1)
else:
    print(back(limit[0], limit[1], limit[2], 0, 0))
