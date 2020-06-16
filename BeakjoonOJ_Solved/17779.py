#내가 직접 푼 버전

#1. 선거구 나누는 함수 partition
#2. 선거구 별 인구 세는 함수 count
#3. X, Y, d1, d2 모든 가능 조합마다 (1,2) 반복해서 minCount 갱신

import copy

N = int(input())
city = [list(map(int, input().split())) for i in range(N)]
def count(x, y, d1, d2, tmpCity): #구역 나누기가 가능한 x,y, d1, d2를 전달받음
    pop = [0] * 5
    boundary = {x: [] for x in range(x,x+d1+d2+1)}
    for diff in range(0, d1):
        boundary[x+diff].append(y-diff)
        boundary[x+d2+1+diff].append(y+d2-1-diff)
    for diff in range(0, d2):
        boundary[x+1+diff].append(y+1+diff)
        boundary[x+d1+diff].append(y-d1+diff)

    for r, cList in boundary.items():
        for c in range(min(cList), max(cList)+1):
            pop[4] += tmpCity[r][c]
            tmpCity[r][c] = 0

    for r in range(N):
        for c in range(N):
            if tmpCity[r][c] == 0:
                continue
            else:
                if 0<=r<=x+d1-1 and 0<=c<=y:
                    pop[0] += tmpCity[r][c]
                elif 0 <= r <= x + d2 and y < c <= N-1:
                    pop[1] += tmpCity[r][c]
                elif x+d1 <= r <= N-1 and 0 <= c < y-d1+d2:
                    pop[2] += tmpCity[r][c]
                elif x+d2 < r <= N-1 and y-d1+d2 <= c <= N-1:
                    pop[3] += tmpCity[r][c]

    return max(pop)-min(pop)


result = []
def solve():
    for x in range(N):
        for y in range(N):
            for d1 in range(1, y+1):
                for d2 in range(1, N-y):
                    if x+d1+d2<=N-1:
                        tmp = copy.deepcopy(city)
                        result.append(count(x, y, d1, d2, tmp))

solve()
print(min(result))




