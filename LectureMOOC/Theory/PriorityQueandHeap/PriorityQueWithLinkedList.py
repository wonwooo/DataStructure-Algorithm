class Node:
    value = None
    nodeNext = None
    blnHead = ''
    blnTail = ''

    def __init__(self, value = '', nodeNext = '', blnHead=False, blnTail=False):
        self.value = value
        self.nodeNext = nodeNext
        self.blnHead = blnHead
        self.blnTail = blnTail

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setNext(self, nodeNext):
        self.nodeNext = nodeNext

    def getNext(self):
        return self.nodeNext

    def isTail(self):
        return self.blnTail

    def isHead(self):
        return self.blnHead



class SingleLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0
    def __init__(self):
        self.nodeTail = Node(blnTail=True)
        self.nodeHead = Node(blnHead=True, nodeNext=self.nodeTail)

    def insertAt(self, value, idx):
        nodePrev = self.get(idx - 1)
        nodeNext = nodePrev.getNext()
        nodeNew = Node(value=value)
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size += 1

    def removeAt(self, idx):
        nodePrev = self.get(idx-1)
        nodeRemove = nodePrev.getNext()
        nodePrev.setNext(nodeRemove.getNext())
        self.size -= 1
        return nodeRemove

    def get(self, idx):
        node = self.nodeHead
        for i in range(idx + 1): #nodeHead 다음의 node의 idx를 0으로 간주할때
            node = node.getNext()
        return node

    def getsize(self):
        return self.size

    def printStatus(self):
        node = self.nodeHead
        while node.getNext().isTail() == False:
            node = node.getNext()
            value = node.getValue()
            print(value , end = " ")




class PriorityNode:
    priority = -1
    value = ''
    def __init__(self, value, priority):
        self.priority = priority
        self.value = value

    def getValue(self):
        return self.value

    def getPriority(self):
        return self.priority


class PriorityQueue:#Earlybird approach; priority에 따라 정렬하면서 enqueue

    list = ''

    def __init__(self):
        self.list = SingleLinkedList()

    def enqueueWithPriority(self, value, priority):
        idxInsert = 0
        for itr in range(self.list.getsize()):
            node = self.list.get(itr)
            if node.getValue() == '':
                idxInsert = itr
                break
            if node.getValue().getPriority() < priority:
                idxInsert = itr
                break
            else:
                idxInsert = itr + 1

        self.list.insertAt(PriorityNode(value, priority), idxInsert)

    def dequeueWithPriority(self):
        return self.list.removeAt(0).getValue().getValue()


pq = PriorityQueue()
pq.enqueueWithPriority('pilwon woo', 1)
pq.enqueueWithPriority('hyungjin park', 2)
pq.enqueueWithPriority('minho ryu', 5)
pq.enqueueWithPriority('jaelim ahn', 7)

print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())
print(pq.list.printStatus())
print(pq.dequeueWithPriority())
print(pq.list.printStatus())