from ProductionList import ProductionList

class Queue(ProductionList):
    def __init__(self):
        self.List = ProductionList('')

    def add(self, Object):
        # Problem 3. complete the add function of Queue
        # remember Queue has FIFO characteristics
        self.List.addFirst(Object)

    def get(self):
        # Problem 3. complete the remove function of Queue
        # remember Queue has FIFO characteristics
        nodeRemoved = self.List.removeLast()
        return nodeRemoved

    def getSize(self):
        size = self.List.getSize()
        return size

    def getListString(self):
        string = self.List.getListString()
        return string