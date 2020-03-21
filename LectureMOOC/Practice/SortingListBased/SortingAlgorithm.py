import csv
import abc

class Sorting(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def performSorting(self,lstValues,lstKeys):
        sortedKeys = None
        sortedValues = None
        return sortedKeys, sortedValues

class SelectionSort(Sorting):

    def performSorting(self,lstValues,lstKeys):
        for i in range(len(lstValues)):
            for j in range(i,len(lstValues)):
                if lstValues[i] < lstValues[j]:
                    tempValue = lstValues[i]
                    lstValues[i] = lstValues[j]
                    lstValues[j] = tempValue

                    tempKey = lstKeys[i]
                    lstKeys[i] = lstKeys[j]
                    lstKeys[j] = tempKey
        return lstKeys,lstValues

class QuickSort(Sorting):
    '''
    Descending-order sorting
    Returns keys and values
        Keys : words - attachment to values
        Values : scores - target for sorting
    '''

    def performSorting(self,lstValues,lstKeys):
        if len(lstValues) <= 1:
            return lstKeys,lstValues
        leftValues = []
        leftKeys = []
        rightValues = []
        rightKeys = []
        pivotValues = [lstValues[0]] #뒤에서 list간 덧셈처리 하기 위해서 미리 list형태로 변환한것으로 추측
        pivotKeys = [lstKeys[0]]
        for i in range(1,len(lstKeys)): #pivot idx 0을 제외한 1에서 시작
            if lstValues[i] > pivotValues[0]:
                rightKeys.append(lstKeys[i])
                rightValues.append(lstValues[i])
            elif lstValues[i] < pivotValues[0]:
                leftKeys.append(lstKeys[i])
                leftValues.append(lstValues[i])
            elif lstValues[i] == pivotValues[0]:
                leftKeys.append(lstKeys[i])
                leftValues.append(lstValues[i])
        rightKeys, rightValues = self.performSorting(rightValues, rightKeys)
        leftKeys, leftValues = self.performSorting(leftValues, leftKeys)
        # you can concatenate lists through addition
        # [1] + [2] + [3,4] --> [1,2,3,4]
        return leftKeys + pivotKeys + rightKeys, leftValues + pivotValues + rightValues


if __name__ == "__main__":
    lstValues = [1,3,2]
    lstKeys = ['a','b','c']

    #sorting = SelectionSort()
    sorting = QuickSort()
    lstKeys,lstValues = sorting.performSorting(lstValues,lstKeys)

    print("Keys : "+str(lstKeys))
    print("Values : " + str(lstValues))



