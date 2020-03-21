'''
파스칼의 삼각형으로 푸는 이항계수 문제
'''

n,m = map(int,input().split())
d = [[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    d[i][0] = d[i][i] = 1
    for j in range(1, i):
        d[i][j] = (d[i-1][j-1] + d[i-1][j]) % 10007
print(d[n][m])
