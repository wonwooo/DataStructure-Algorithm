#못풀어서 다른 사람 블로그 참조(출처 : https://hongsj36.github.io/2020/02/16/BOJ_16637/)
'''
사칙 연산의 우선 순위와 상관없이 괄호만 먼저 계산하고 나머지는 순서대로
원래 후위 표기법을 사용하는 스택계산기를 구현하여 풀 수있다고 한다
숫자가 1자리이고 순서대로 피연산자와 연산자가 나오기 때문에 연산자의 개수는
(N-1) // 2
(N-1) // 2개의 연산자를 고르는 가지수는 2^(N-1)//2
'''

# 부분 계산
def my_calc(n, c, i):
    calc = c.pop(i)
    if calc == '+':
        n[i] += n.pop(i + 1)
    elif calc == '-':
        n[i] -= n.pop(i + 1)
    elif calc == '*':
        n[i] *= n.pop(i + 1)


N = int(input())
nums = []  # 숫자 리스트
calcs = []  # 기호 리스트

# 입력 받기
cnt = 0
for i in input():
    if cnt % 2 == 0:
        nums.append(int(i))
    else:
        calcs.append(i)
    cnt += 1

# DFS
stack = [(nums, calcs, 0)]
result = -float('inf')
while stack:
    n, c, cnt = stack.pop()
    if cnt >= len(c):  # 괄호 다 쳤을 때
        while c:  # 남은 기호로 다 계산 후
            my_calc(n, c, 0)
        if result < n[0]:  # 결과 갱신
            result = n[0]
    else:
        # 괄호 안침
        stack.append((n, c, cnt + 1))
        # 괄호 침 (부분 계산 후 다음 기호로)
        nn = n[:]
        nc = c[:]
        my_calc(nn, nc, cnt)
        stack.append((nn, nc, cnt + 1))

print(result)