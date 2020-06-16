n = int(input())
plans = []
for _ in range(n):
    plans.append(list(map(int, input().split())))

def go(day, profit):
    global answer
    if day == n:
        answer = max(profit, answer)
        return
    if day + plans[day][0] < n+1:
        go(day + plans[day][0], profit+plans[day][1])
    go(day+1, profit)

answer = 0
go(0, 0)
print(answer)