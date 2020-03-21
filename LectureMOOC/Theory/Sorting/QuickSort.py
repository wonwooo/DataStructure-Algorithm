import random

N = 10
lstNumbers = list(range(N))
random.shuffle(lstNumbers)

def performQuickSort(seq, pivot = 0):
    if len(seq) <= 1:
        return seq
    pivotValue = seq[pivot]
    less = []
    greater = []
    for itr in range(len(seq)):
        if itr == pivot:
            continue
        elif seq[itr] > pivotValue:
            greater.append(seq[itr])
        elif seq[itr] <= pivotValue:
            less.append(seq[itr])
    ret = performQuickSort(less) + [pivotValue] + performQuickSort(greater) #recursive calls
    return ret

print(lstNumbers)
print(performQuickSort(lstNumbers))