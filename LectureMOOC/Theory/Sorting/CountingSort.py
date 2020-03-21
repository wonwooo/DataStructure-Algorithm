import random

N = 10
lstNumbers = list(range(N))
random.shuffle(lstNumbers)

print(lstNumbers)

def performCountingSort(seq):
    max = -9999
    min = 9999
    for itr in range(len(seq)):
        if seq[itr] > max:
            max = seq[itr]
        if seq[itr] < min:
            min = seq[itr]
    counting = [0] * (max-min+1)
    #max-min+1 = seq에 존재하는 서로 다른 숫자 갯수

    #perform counting
    for itr in range(len(seq)):
        value = seq[itr]
        counting[value - min] += 1

    #conting에는 작은 값 순서로 갯수가 저장되어있음
    cnt = 0
    for itr1 in range(max-min+1):
        for itr2 in range(counting[itr1]):
            seq[cnt] = itr1 + min
            cnt += 1
    return seq

print(performCountingSort(lstNumbers))