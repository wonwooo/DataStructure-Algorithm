n, m = map(int, input().split())
a = list(map(int, input().split()))
d = [False] * 360
d[0] = True
for i in range(n):
    for k in range(360):
        for j in range(360):
            if not d[j]:
                continue
            # d[j]기준으로 a[i]를 더하고 빼고 한번씩 해서 방문기록함
            # a[i]를 더하고 빼는것은 더이상 a[i]로 만들 수 있는 각이 없을 때까지 반복해야함
            # a[i]가 최소 1일경우는 360번을 반복해야 a[i]를 더하고 빼서 구할 수 있는 모든각이 구해짐
            # 그것이 k를 360번 반복하는 이유
            d[(j-a[i]+360)%360] = True
            d[(j+a[i])%360] = True

xx = list(map(int, input().split()))
for x in xx:
    print('YES' if d[x] else 'NO')