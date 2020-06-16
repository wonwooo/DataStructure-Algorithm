n = int(input())
numbers = []
operators = []
eq = input()
for i in range(len(eq)):
    if i%2 == 0:
        numbers.append(int(eq[i]))
    elif i%2 != 0:
        operators.append(eq[i])

def calc_rest(nums, opers):
    i = 0
    while i<len(opers):
        if opers[i] == '*':
            oper = opers.pop(i)
            nums[i] *= nums.pop(i+1)
        else:
            i += 1


    while opers:
        if opers[0] == '+':
            opers.pop(0)
            nums[0] += nums.pop(1)
        elif opers[0] == '-':
            opers.pop(0)
            nums[0] -= nums.pop(1)

    return nums[0]

def calc(nums, opers, i):
    oper = opers.pop(i)
    if oper == '*':
        nums[i] *= nums.pop(i+1)
    if oper == '+':
        nums[i] += nums.pop(i+1)
    if oper == '-':
        nums[i] -= nums.pop(i+1)

ans = -float('inf')
def go(nums, opers, idx):
    global ans
    if idx >= len(opers):

        res = calc_rest(nums[:], opers[:])
        ans = max(ans, res)
        return
    go(nums, opers, idx+1)

    tempn, tempo = nums[:], opers[:]
    calc(tempn, tempo, idx)
    go(tempn, tempo, idx+1)


go(numbers, operators, 0)
print(ans)