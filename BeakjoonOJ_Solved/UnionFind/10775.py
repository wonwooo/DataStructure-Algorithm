G = int(input())
P = int(input())
planes = [int(input()) for _ in range(P)]
import sys
sys.setrecursionlimit(100000)
def find_empty(g, gates):
    if not g in gates:
        gates[g] = g-1
        return g
    empty = find_empty(gates[g], gates)
    gates[g] = empty-1
    return emptyd
gates = {}
ans = 0
for g in planes:
    empty_gate = find_empty(g, gates)
    if empty_gate == 0:
        break
    ans += 1
print(ans)
