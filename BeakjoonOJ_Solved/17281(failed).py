n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
from itertools import permutations

def score(order):
    s = 0
    idx = 0
    for performance in innings:
        out = 0
        bases = []
        while True:
            idx = idx % 9
            player = order[idx]
            if performance[player] == 0:
                out += 1
            else:
                for i in range(len(bases)):
                    bases[i] += performance[player] #나가있던 선수들 진루
                bases.append(performance[player]) #타자 진루

            idx += 1
            if out == 3:
                break

            for b in bases:
                if b >= 4: #홈 들어온 선수들만큼 +1
                    s += 1
            bases = [b for b in bases if b<4]
    return s


answer = 0
for order in permutations(range(1, 9), 8):
    order = order[0:3] + (0,) + order[3:]
    answer = max(score(order), answer)

print(answer)