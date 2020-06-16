n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
ans = 0
for i in range(n):
    ans += 1
    a[i] -= b
    if a[i] < 0:
        a[i] = 0
    ans += a[i]//c
    if a[i]%c != 0:
        ans += 1
print(ans)