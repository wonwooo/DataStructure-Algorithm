n, m = map(int, input().split())
a = [[False]*n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    a[u-1][v-1] = a[v-1][u-1] = True
ans = 0
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if a[i][j] or a[i][k] or a[j][k]:
                continue
            ans += 1

print(ans)