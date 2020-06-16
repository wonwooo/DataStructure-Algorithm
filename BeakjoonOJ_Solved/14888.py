'''
첫번째는 모든 연산 순열을 구한 다음 계산하는 방법인데
list자료형에 더해가며 중복을 허용해서 순열을 구하니 메모리 초과가 떠서 못풀었다.
예를 들어서 (+ - - * +)와 (+ - - * +)는 같은경우인데 순열로 구하면 list에 둘다 들어간다.
그래서 set에 tuple로 add하는 방법을 썼더니 메모리 초과를 면했음(set에는 list를 더할 수 없다)

두 번째처럼 dfs로 중복없이 탐색 하는 풀이가 가장 좋다
'''

import sys
sys.setrecursionlimit(100000)
from itertools import permutations
n = map(int, input())
nums = list(map(int, input().split()))
a, m, p, d = map(int, input().split())
cal = ['+']*a + ['-']*m + ['*']*p + ['/']*d
def calculate(operator, num1, num2):
    if operator == '-':
        return num1 - num2
    if operator == '+':
        return num1 + num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        if num1 == 0:
            return 0
        if num1 < 0 and num2 < 0 :
            return abs(num1) // abs(num2)
        elif num1 < 0 and num2 > 0:
            return -(abs(num1) // num2)
        elif num1 >0 and num2 < 0:
            return -(num1 // abs(num2))
        elif num1 > 0  and num2 > 0:
            return num1 // num2


def make_permutation(cal, n):
    ret = set()
    if len(cal) < n:
        return ret
    if n == 1:
        for c in cal:
            ret.append((c,))
        return ret
    for c in cal:
        temp = cal[:]
        temp.remove(c)
        for perm in make_permutation(temp, n-1):
            ret.append((c,) + perm)
    return ret

def go(nums, cal):
    ls = make_permutation(cal, len(cal))
    #ls = set(permutations(cal, len(cal)))
    results = []
    for operators in ls:
        temp = nums[:]
        for i in range(len(operators)):
            temp[i+1] = calculate(operators[i], temp[i], temp[i+1])
        results.append(temp[-1])

    return set(results)
answer = go(nums, cal)
print(max(answer))
print(min(answer))

'''

n = int(input())
nums = list(map(int, input().split()))
a, s, p, d = map(int, input().split())
#해당 숫자만큼 dfs연산 하면 순열만들때처럼 중복 없이 탐색할 수 있다..

maxval = -1000000000
minval = 1000000000

def go(idx , res, a, s, p, d):
    global maxval
    global minval
    if idx == n:
        if res > maxval:
            maxval = res
        if res < minval:
            minval = res
        return
    if a:
        go(idx+1, res+nums[idx], a-1, s, p, d)
    if s:
        go(idx+1, res-nums[idx], a, s-1, p, d)
    if p:
        go(idx+1, res*nums[idx], a, s, p-1, d)
    if d:
        go(idx+1, int(res/nums[idx]), a, s, p, d-1)

go(1, nums[0], a, s, p, d)

print(maxval)
print(minval)
'''