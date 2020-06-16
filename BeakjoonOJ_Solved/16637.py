import copy
n = int(input())
eq = list(input())
numbers = []
operators = []
for i in range(len(eq)):
    if i%2 == 0:
        numbers.append(int(eq[i]))
    else:
        operators.append(eq[i])

def calc(numlist,oplist,idx):
    operator = oplist.pop(idx)
    if operator == '+':
        numlist[idx] += numlist.pop(idx+1)
    if operator == '-':
        numlist[idx] -= numlist.pop(idx+1)
    if operator == '*':
        numlist[idx] *= numlist.pop(idx+1)


answer = -float('inf')
def go(nums, opers, idx):
    global answer
    if idx >= len(opers):
        n, o = nums[:], opers[:] #여기도매우 중요
        while o:
            calc(n, o, 0)
        answer = max(answer, n[0])
        return

    go(nums, opers, idx+1)

    tmpn, tmpo = nums[:], opers[:] #매우중요
    calc(tmpn, tmpo, idx)
    go(tmpn, tmpo, idx+1)

go(numbers, operators, 0)
print(answer)
'''
괄호 추가하기
괄호 안에 하나의 연산자만이 존재해야 한다. 
수식을 계산할 때는 왼 쪽 부터 순서대로 계산해야 한다. 

[설계]
문제 이해가 중요하다..
괄호를 직접 칠 필요는 없는 문제다
순서대로 연산자를 탐색 하면서 , 해당 연산자를 수행 하면 괄호를 치는 것이고
수행 하지 않고 다음 연산자로 넘어가면 괄호를 안치는 것이다. 
재귀함수는 

재귀함수 탈출조건 : 
count가 최초 연산자의 횟수까지 올라가면, 괄호치기가 끝났기 때문에
남은 연산을 모두 수행한다. 그 결과를 answer와 비교한다. 

숫자와 연산자를 list로 따로 저장하고, 
idx를 통해 연산자에 접근한다.

1) 계산을 지금 하면(괄호를 치면) calc함수에 넘겨서 해당 위치의 2개의 숫자와 연산자로 계산을 하고
숫자 리스트와 연산자 list가 하나씩 줄어든 상태로 idx를 하나만 올려 재귀를 쏜다. idx를 올리지 않으면 다음 연산자로 자동으로 넘어가는데,
한 괄호에 하나의 연산자만 잇어야 하기 때문에 괄호를 쳤다면 다다음 연산자로 가야하기 때문에 idx를 하나 올려줘야한다.

2) 계산을 하지 않으면(괄호를 안치면) 그냥 숫자 list, 연산자 list그대로 두고 idx만 하나 올린다. 연산을 안했으니 하나 올려서 다음 선택을 하면 된다.

연산 함수 : 숫자리스트, 연산자 리스트, 연산할 idx 전달받음
연산자 list 의 해당idx를 pop하고
숫자 리스트의 idx+1를 pop하고 idx와 곱해서 idx를 갱신한다.
그러면 숫자 list가 해당위치만 계산되어 하나 줄어들고 연산자 list도 해당 idx만 없어진다.

9
3+8*7-9*2

괄호치지 않은 나머지 연산을 할 땐 idx를 0으로 두고 계속 연산함수에 넘기면 된다.

'''