n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]


answer = 100*(n**2)
def diff(team1, team2):
    t1, t2 = 0, 0
    for i in team1:
        for j in team1:
            t1 += s[i][j]
    for i in team2:
        for j in team2:
            t2 += s[i][j]
    return abs(t1-t2)

def go(idx, team1, team2):
    global answer
    if len(team1) == n // 2 and len(team2) == n // 2:
        diff_ = diff(team1, team2)
        if diff_ < answer:
            answer = diff_
        return

    if idx < n and len(team1) < n//2:
        go(idx+1, team1 + [idx], team2)
    if idx < n and len(team2) < n//2:
        go(idx+1, team1, team2 + [idx])
    return

go(0, [], [])
print(answer)


