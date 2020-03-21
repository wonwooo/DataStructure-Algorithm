m, n = map(int,input().split())
start, end, delete, add = map(int,input().split())
start -= 1
end -= 1
a = [0]
for i in range(n):
    temp = int(input())
    a.append(temp-1)
d = [[1000000000]*m for _ in range(n+1)]
for i in range(m):
    if i == start:
        d[0][i] = 0
    else:
        d[0][i] = abs(start-i)*add
for i in range(1, n+1):
    for j in range(m):
        for k in range(m):
            if k == j and (a[i] == k or a[i]+1 == k):
                if d[i][j] > d[i-1][k] + delete:
                    d[i][j] = d[i-1][k] + delete
            elif (k <= a[i] <= j-1) or (j <= a[i] <= k-1):
                if d[i][j] > d[i-1][k] + (abs(k-j)-1)*add:
                    d[i][j] = d[i-1][k] + (abs(k-j)-1)*add
            else:
                if d[i][j] > d[i-1][k] + abs(k-j)*add:
                    d[i][j] = d[i-1][k] + abs(k-j)*add
print(d[n][end])