d = [[[[False]*436 for k in range(31)] for j in range(31)] for i in range(31)]
n, k = map(int,input().split())
ans = ''
def go(i, a, b, p):
    if i == n:
        if p == k:
            return True
        else:
            return False
    if d[i][a][b][p]:
        return False
    d[i][a][b][p] = True
    global ans
    temp = ans
    ans = temp + 'A'
    if go(i+1, a+1, b, p):
        return True
    ans = temp + 'B'
    if go(i+1, a, b+1, p+a):
        return True
    ans = temp + 'C'
    if go(i+1, a, b, p+a+b):
        return True
    return False
if go(0,0,0,0):
    print(''.join(ans))
else:
    print(-1)

