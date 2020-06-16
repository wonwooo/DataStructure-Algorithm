n = int(input())

def check(queens, col):
    row = len(queens)
    for r in range(row):
        if queens[r] == col or row-r == abs(queens[r]-col):
            return False
    return True

def go(N, queens):
    global count
    if len(queens) == n:
        count += 1
        return
    for c in range(n):
        if check(queens, c):
            go(N, queens + [c])
    return

count = 0
go(n, [])
print(count)
