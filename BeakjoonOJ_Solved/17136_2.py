'''
백트래킹을 사용해서 , 들어온 색중이 개수가 이미 정답보다 많으면 모두 cut한다.
색종이는 큰 것 부터 두어야 backtracking이 많이 이루어질 수 있다.
재귀함수로 가능한 모든 경우를 탐색한다.
처음에 1인 위치를 locs에 기억 해 두고 갯수도 기억 해 둔다.
idx를 통해서 locs를 돌면서, 5,4,3,2,1 색종이를 둘 수 있는지 확인하고 그 순서대로 둔다.
k사이즈 색종이 둘수 있는지 확인법 : count가 5 보다 작은 지 확인하고, k*k 사이즈가 모두 비어있는 지 확인한다.
확인 되면 해당 구역을 0으로 채우고, idx를 하나 키워서 재귀함수를 쏜 후에 다시 1로 만든다.


idx가 locs의 길이에 다 다랐을 때에 filled 갯수를 확인하고 filled가 처음 빈칸갯수와같으면
answer를 갱신한다
재귀함수 받을때마다 count들의 합을 구하고 answer보다 크면 바로 return해서 backtracking
'''
a = [list(map(int, input().split())) for _ in range(10)]
locs = []
for i in range(10):
    for j in range(10):
        if a[i][j] == 1:
            locs.append((i, j))
def go(counts, idx, filled):
    global a, answer, locs
    if sum(counts) > answer:#백트래킹
        return
    if filled == len(locs):
        answer = min(answer, sum(counts))
        return
    if idx>=len(locs):
        return
    cx, cy = locs[idx]
    if not a[cx][cy]:
        go(counts, idx+1, filled)
    else:
        for k in range(5, 0, -1):
            if counts[k-1] >= 5:
                continue
            if cx + k > 10 or cy + k > 10:
                continue
            s = 0
            for r in range(cx, cx+k):
                for c in range(cy, cy+k):
                    s+=a[r][c]
            if s!=k**2:
                continue
            counts[k-1] += 1
            for r in range(cx, cx+k):
                for c in range(cy, cy+k):
                    a[r][c] = 0
            go(counts, idx+1, filled+(k**2))
            counts[k - 1] -= 1
            for r in range(cx, cx + k):
                for c in range(cy, cy + k):
                    a[r][c] = 1
answer = 26
go([0, 0, 0, 0, 0], 0, 0)
print(-1 if answer == 26 else answer)