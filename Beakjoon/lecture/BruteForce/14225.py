
'''
비트마스크
n = int(input())
a = list(map(int,input().split()))
c = [False]*(n*100000+10)
for i in range(1<<n):
    s = 0
    for j in range(n):
        if (i&(1<<j)):
            s += a[j]
    c[s] = True
i = 1
while True:
    if c[i] == False:
        break
    i += 1
print(i)
'''

n = int(input())
a = list(map(int,input().split()))
c = [False]*(n*100000+10)
def go(i, sum):
    if i == n:
        c[sum] = True
        return
    go(i+1,sum+a[i])
    go(i+1,sum)
go(0,0)
i = 1
while True:
    if c[i] == False:
        break
    i += 1
print(i)