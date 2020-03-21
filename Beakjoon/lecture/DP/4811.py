d = [[-1]*31 for _ in range(31)]
def calc(f, h):
    if d[f][h] != -1:
        return d[f][h]
    if f == 0:
        return 1
    if h == 0:
        d[f][h] = calc(f-1,h+1)
        return d[f][h]
    d[f][h] = calc(f-1,h+1) + calc(f,h-1)
    return d[f][h]
while True:
    n = int(input())
    if n == 0:
        break
    print(calc(n,0))
