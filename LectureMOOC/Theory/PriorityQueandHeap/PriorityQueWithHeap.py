class BinaryHeap: #Tree가 아닌 array의 형태로 binary heap을 구현하고, 그 binary heap을 priority queue로 사용

    arrPriority = {}
    arrValue = {}
    size = 0

    def __init__(self):
        self.arrPriority = {}
        self.arrValue = {}
        self.size = 0

    def enqueueWithPriority(self, value, priority):
        self.arrPriority[self.size] = priority
        self.arrValue[self.size] = value
        self.size = self.size + 1
        self.percolateUp(self.size-1)

    def percolateUp(self, idxPercolate):
        if idxPercolate == 0:
            return
        parent = int((idxPercolate-1) / 2)
        if self.arrPriority[parent] < self.arrPriority[idxPercolate]:
            self.arrPriority[parent], self.arrPriority[idxPercolate] = self.arrPriority[idxPercolate], self.arrPriority[parent]
            self.arrValue[parent], self.arrValue[idxPercolate] = self.arrValue[idxPercolate], self.arrValue[parent]
            self.percolateUp(parent)

    def dequeueWithPriority(self):
        #escape condition
        if self.size == 0:
            return ''

        retPriority = self.arrPriority[0]
        retValue = self.arrValue[0]
        #마지막 value와 root의 priority와 value를 교환, complete tree의 structure property 유지
        self.arrPriority[0] = self.arrPriority[self.size - 1]
        self.arrValue[0] = self.arrValue[self.size - 1]
        self.size = self.size - 1
        #PercolateDown을 통해 heap property 유지
        self.percolateDown(0)
        return retValue

    def percolateDown(self, idxPercolate):
        '''해당 node까지의 size는 해당 node의 idx보다 하나 더 크다.
        2*idxPercolate + 1 < self.size이면 leftchild는 보장되어있음
        <=> 2*idxPercolate + 1 >= self.size이면 leftchild는 없음'''
        if 2*idxPercolate + 1 >= self.size:
            return
        else: #적어도 leftchild는 있음, rightchild 보장 안됨
            leftChild = 2*idxPercolate + 1
            leftPriority = self.arrPriority[leftChild]

        if 2*idxPercolate + 2 >= self.size: #rightchild 없음
            rightPriority = -9999
        else: #rightchild 있음
            rightChild = 2*idxPercolate+2
            rightPriority = self.arrPriority[rightChild]

        if leftPriority > rightPriority:
            biggerChild = leftChild
        else:
            biggerChild = rightChild

        if self.arrPriority[idxPercolate] < self.arrPriority[biggerChild]:
            self.arrPriority[idxPercolate], self.arrPriority[biggerChild] = self.arrPriority[biggerChild], self.arrPriority[idxPercolate]
            self.arrValue[idxPercolate], self.arrValue[biggerChild] = self.arrValue[biggerChild], self.arrValue[idxPercolate]
            self.percolateDown(biggerChild)

    def build(self, arrInputPriority, arrInpurValue):
        for itr in range(len(arrInputPriority)):
            self.arrPriority[itr] = arrInputPriority[itr]
            self.arrValue[itr] = arrInpurValue[itr]
        self.size = len(arrInputPriority)
        for itr in range(self.size-1, -1, -1): #(시작점, 종착점 하나 전, 종착점을 향한 진행 간격)
            self.percolateDown(itr)


pq = BinaryHeap()
pq.enqueueWithPriority('pilwon woo', 1)
pq.enqueueWithPriority('hyungjin park', 2)
pq.enqueueWithPriority('minho ryu', 5)
pq.enqueueWithPriority('jaelim ahn', 7)

print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())

pq2 = BinaryHeap()
pq2.build({0:1, 1:2, 2:3, 3:99}, {0:'pilwon woo', 1:'hyungjin park', 2:'minho ryu', 3:'jaelim ahn'})
print(pq2.dequeueWithPriority())
print(pq2.dequeueWithPriority())
print(pq2.dequeueWithPriority())
print(pq2.dequeueWithPriority())

