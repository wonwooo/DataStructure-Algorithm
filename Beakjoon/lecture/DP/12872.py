n,m,p = map(int,input().split())

d = []
for i in range(p+1):
    d.append([-1]*(n+1))

def go(position, x):
    y = n-x
    if position == p:
        if y == 0:
            return 1
        else:
            return 0
    ans = d[position][x]
    if ans != -1:
        return ans
    ans = 0
    if y > 0:
        ans += go(position+1, x+1) * y

    if x > m:
        ans += go(position+1, x) * (x-m)

    ans %= 1000000007
    d[position][x] = ans
    return ans


print(go(0,0))