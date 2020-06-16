n,m = map(int,input().split())
a = [0] + list(map(int,input().split()))
s = [0]*(n+1)
for i in range(1, n+1):
    s[i] = s[i-1] + a[i]
for _ in range(m):
    x,y = map(int,input().split())
    print(s[y]-s[x-1])