class PlanNode:
    def __init__(self, numNo, strSerialNumber, strModel, numModelNumber, dateStart, numAssemblyOrder, dateEnd,
                 strOrderOrigin):
        self.numNo = numNo
        self.strSerialNumber = strSerialNumber
        self.strModel = strModel
        self.numModelNumber = numModelNumber
        self.dateStart = dateStart
        self.numAssemblyOrder = numAssemblyOrder
        self.dateEnd = dateEnd
        self.strOrderOrigin = strOrderOrigin

    def printOut(self):
        print('No :', self.numNo, ', SerialNum : ', self.strSerialNumber, ',Model:', self.strModel, 'start date :',
              self.dateStart)

    def getNextNode(self):
        node = self.nextNode
        return node

    def getPrevNode(self):
        node = self.prevNode
        return node

    def setNextNode(self, node):
        # Problem 1. complete this method
        self.nextNode = node

    def setPrevNode(self, node):
        # Problem 1. complete this method
        self.prevNode = node