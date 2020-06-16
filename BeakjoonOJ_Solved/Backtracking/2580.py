a = [list(map(int, input().split())) for _ in range(9)]
locs = []
regions = [[[] for _ in range(3)] for _ in range(3)]
for i in range(9):
    for j in range(9):
        if a[i][j] == 0:
            locs.append((i, j))
        x = i // 3
        y = j // 3
        regions[x][y].append(a[i][j])
N = len(locs)


def go(count, idx):
    global a,solved, regions
    if solved:
        return
    if count == N:
        solved = True
        for l in a:
            print(*l)
        return

    row, col = locs[idx]
    r = row // 3
    c = col // 3
    reg = regions[r][c]
    horizon = a[row]
    vertical = [a[i][col] for i in range(9)]
    for k in range(1, 10):
        if k not in reg and k not in horizon and k not in vertical:
            a[row][col] = k
            regions[r][c].append(k)
            go(count+1, idx+1)
            a[row][col] = 0
            regions[r][c].pop()
    return
solved = False
go(0, 0)