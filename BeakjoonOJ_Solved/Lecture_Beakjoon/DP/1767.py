n = int(input())
m = int(input())
k = int(input())
d = [[[-1]*101 for j in range(101)] for i in range(101)]
def go(n, m, k):
    if k == 0:
        return 1
    if n <= 0 or m <= 0 or k < 0:
        return 0
    if d[n][m][k] != -1:
        return d[n][m][k]
    d[n][m][k] = go(n-1,m,k) + \
        go(n-1,m-1,k-1)*m + \
        go(n-1,m-2,k-2)*m*(m-1)//2 + \
        go(n-2,m-1,k-2)*m*(n-1)
    d[n][m][k] %= 1000001
    return d[n][m][k]
print(go(n,m,k))
