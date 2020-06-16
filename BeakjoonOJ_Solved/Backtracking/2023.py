n = int(input())
'''
재귀적으로 숫자를 만들고 backtracking을 통해 가능한 경우만 탐색한다
홀수에 대해서만 접근한다
앞 자리들에 현재 숫자를 더한 숫자를 제곱근까지 3부터 홀수에 대해서만 나눠보고
한번도 안 나누어떨어지면 재귀함수 호출
'''
def go(num):
    if len(num) == n:
        pNums.append(num)
        return

    for k in range(1, 10):
        cand = int(num + str(k))
        if cand == 1:
            continue
        root = int(cand**1/2)
        prime = True
        for d in range(2, root+1):
            if cand % d == 0:
                prime = False
                break
        if prime:
            go(str(cand))
    return

pNums = []
go('')
for prime in pNums:
    print(prime)