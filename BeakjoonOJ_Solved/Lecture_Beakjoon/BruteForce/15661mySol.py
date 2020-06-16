'''
N명의 사람이 2개의 팀에 배분되는 모든 경우를 재귀를 통해 구현한다.
각 팀에는 한 명 이상이 있어야 한다.
'''

def go(a, team1, team2, idx):
    if idx == n:
        if len(team1) < 2 or len(team2) < 2:
            return -1
        s1 = 0
        s2 = 0
        for i in team1:
            for j in team1:
                if i == j:
                    continue
                s1 += a[i][j]
        for i in team2:
            for j in team2:
                if i==j:
                    continue
                s2 += a[i][j]
        return abs(s1-s2)

    ans = 10000000
    # idx번째 사원이 team1으로 갔을 때의 능력치 차이
    temp1 = go(a, team1+[idx], team2, idx+1)
    if temp1 != -1:
        if ans > temp1:
            ans = temp1
    # idx번째 사원이 team2로 갔을 때의 능력치 차이
    temp2 = go(a, team1, team2+[idx], idx+1)
    if temp2 != -1:
        if ans > temp2:
            ans = temp2
    return ans

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

print(go(a,[],[], 0))


