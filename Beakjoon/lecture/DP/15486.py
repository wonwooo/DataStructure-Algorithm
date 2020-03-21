'''
15486 퇴사 2
K일까지의 수익의  최대값만이 중요하고, 나머지 값들은 최대 수익에 영향을 주지 못한다

d[i + t[i]] : i일에 배정된 상담을 하지 않고 시간이 흘러 i+t[i]일이 되었을 때의 최대수익; 이것은 i-1까지의
과정을 통해 구해 놓은 값
d[i] + p[i] : i일에 배정된 상담을 할 경우에 i+t[i]일이 되었을 때에 최대 수익
max를 취해서 둘 중 더 큰 수익을 d[i+t[i]]의 값으로 갱신해간다


'''
n = int(input())
t = [0]*n
p = [0]*n
for i in range(n):
    t[i], p[i] = map(int, input().split())
d = [0]*(n+50) #상담소요시간이 최대 50일이기 떄문에
for i in range(n):
    d[i+t[i]] = max(d[i + t[i]], d[i]+p[i])
    d[i+1] = max(d[i+1], d[i])
print(d[n])