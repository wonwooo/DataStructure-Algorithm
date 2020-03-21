n,a,b,c = map(int,input().split())
d = [[[[-1]*51 for k in range(51)] for j in range(51)] for i in range(51)]
def go(n, a, b, c):
    if n == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
    if a < 0 or b < 0 or c < 0:
        return 0
    ans = d[n][a][b][c]
    if ans != -1:
        return ans
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i+j+k == 0:
                    continue
                ans += go(n-1, a-i, b-j, c-k)
    ans %= 1000000007
    d[n][a][b][c] = ans
    return ans
print(go(n,a,b,c))
