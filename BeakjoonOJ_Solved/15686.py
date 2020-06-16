from itertools import combinations
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
h = []
c = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            c.append((i,j))
        if a[i][j] == 1:
            h.append((i,j))


#comb = list(combinations(c, m))
answer = []

def calculate_dist(chickens, h):
    chicken_dist = 0
    for house in h:
        dist = 10000
        for chicken in chickens:
            temp = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            if temp < dist:
                dist = temp
        chicken_dist += dist
    return chicken_dist

def go(count, idx, chickens):
    global answer
    if count == m:
        answer.append(calculate_dist(chickens, h))
        return

    for i in range(idx, len(c)):
        go(count+1, i+1, chickens+[c[i]])
    '''
    go(idx+1, chickens+[c[i]])
    go(idx+1, chickens)
    이렇게도 가능
    '''



answer = []
go(0, 0, [])
print(min(answer))