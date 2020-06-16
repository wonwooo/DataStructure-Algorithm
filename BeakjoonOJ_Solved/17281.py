n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
#반복문 안에서 remove쓰면 안된다..! 길이가 줄어드는데 index는 그대로 참조하기 때문에 out of range error난다
from itertools import permutations
def score(ord):#순서 받아서 플레이하고 점수 return
    '''
    while문을 사용해서, 선수를 계속 나누기연산으로 돌려 가면서 out이 3이 되기 전까지 계속 진행한다
    while문은 각 선수에 대해서 한번 돌고, out이 발생하면 out+1 한다
    그 while문을 이닝 수만큼 진행 하면서 이닝 별 score를 기록한다
    '''
    s = 0
    idx = 0 #idx : idx번타자; 첫이닝은 0번타자로 시작
    for perform in innings:
         #이닝별 선수들 performance
        out = 0 #out 초기화
        b1, b2, b3 = 0, 0, 0
        while True: #out 3이면 break
            idx = idx % 9
            player = ord[idx]
            if perform[player] == 0:
                out += 1
            elif perform[player] == 1:
                s += b3
                b1, b2, b3 = 1, b1, b2
            elif perform[player] == 2:
                s += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif perform[player] == 3:
                s += (b1 + b2 + b3)
                b1, b2, b3 =  0, 0, 1
            elif perform[player] == 4:
                s += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            idx += 1
            if out == 3:
                break
    return s
answer = 0
for order in permutations(range(1, 9), 8):
    order = order[0:3] + (0,) + order[3:]
    answer = max(score(order), answer)

print(answer)