n,m = map(int,input().split())
a = list(map(int,input().split()))
a = [x%m for x in a]
cnt = [0]*m
cnt[0] = 1
s = 0
for i in range(n):
    s += a[i]
    s %= m
    cnt[s] += 1
ans = 0
for i in range(m):
    ans += cnt[i]*(cnt[i]-1)//2
print(ans)
