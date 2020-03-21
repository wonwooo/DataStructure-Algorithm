'''
나올수 있는 최대 부분 합의 길이만큼 방문 array생성
재귀함수로 모든 조합 구해가면서 idx끝까지 가면 sum 구해서 방문 array에 방문처리
모두 처리한 뒤에 가장먼저 False 나오는 위치 반환
'''
n = int(input())
s = list(map(int, input().split()))
visited = [False]*(sum(s)+2)
def go(frac, idx):
    global s
    global visited
    if idx == len(s):
        visited[sum(frac)] = True
        return
    temp1 = go(frac + [s[idx]], idx + 1)
    temp2 = go(frac, idx+1)


go([], 0)

ans = 1
for i, visit in enumerate(visited):
    if not visit:
        ans = i
        break
print(ans)




'''
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