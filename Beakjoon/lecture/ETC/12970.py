n,k = map(int,input().split())
for a in range(0, n+1):
    b = n-a
    if a*b < k:
        continue
    cnt = [0]*(b+1)
    for i in range(a):
        x = min(b, k)
        cnt[x] += 1
        k -= x
    for i in range(b, -1, -1):
        for j in range(cnt[i]):
            print('A', end='')
        if i > 0:
            print('B', end='')
    print()
    exit()
print(-1)

