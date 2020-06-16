'''
풀다가 포기한 이유 : 치킨집 중에서 일정한 갯수만 폐업 시키는 조합을 찾는 방법을 구현 못함
Brute Force 문제
'''


def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
people = []
store = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            people.append((i,j))
        elif a[i][j] == 2:
            store.append((i,j))
'''
이부분 핵심아이디어 : store 길이에 맞는 list를 만들어서, 선택된 store를 1로 기록하면서
permutation을 d만 바꿔가면서 구해나감
'''

d = [0]*len(store)
for i in range(m):
    d[i] = 1
d.sort()
ans = -1

while True: #모든 조합에 대해서 loop를 다 돌려야 끝남
    s = 0
    for px,py in people:
        dists = []
        for i,(sx,sy) in enumerate(store):
            if d[i] == 0:
                continue
            d1 = abs(px-sx)
            d2 = abs(py-sy)
            dists.append(d1+d2)
        dists.sort()
        s += dists[0]
    if ans == -1 or ans > s:
         ans = s
    if not next_permutation(d):
        break
print(ans)