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

    def performSorting(self,lstValues,lstKeys):
        if len(lstValues) <= 1:
            return lstKeys,lstValues
        leftValues = []
        leftKeys = []
        rightValues = []
        rightKeys = []
        pivotValues = [lstValues[0]]
        pivotKeys = [lstKeys[0]]
        for i in range(1,len(lstKeys)):
            if lstValues[i] > pivotValues[0]:
                leftValues.append(lstValues[i])
                leftKeys.append(lstKeys[i])
            elif lstValues[i] < pivotValues[0]:
                rightValues.append(lstValues[i])
                rightKeys.append(lstKeys[i])
            elif lstValues[i] == pivotValues[0]:
                pivotValues.append(lstValues[i])
                pivotKeys.append(lstKeys[i])
        leftKeys, leftValues = self.performSorting(leftValues,leftKeys)
        rightKeys, rightValues = self.performSorting(rightValues, rightKeys)
        # you can concatenate lists through addition
        # [1] + [2] + [3,4] --> [1,2,3,4]
        return leftKeys+pivotKeys+rightKeys,leftValues+pivotValues+rightValues


if __name__ == "__main__":
    lstValues = [1,3,2]
    lstKeys = ['a','b','c']

    #sorting = SelectionSort()
    sorting = QuickSort()
    lstKeys,lstValues = sorting.performSorting(lstValues,lstKeys)

    print("Keys : "+str(lstKeys))
    print("Values : " + str(lstValues))

