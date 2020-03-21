class PlanNode:
    def __init__(self, numNo, strSerialNumber, strModel):
        self.numNo = numNo
        self.strSerialNumber = strSerialNumber
        self.strModel = strModel


    def printOut(self):
        print('No :', self.numNo, ', SerialNum : ', self.strSerialNumber, ', Model : ', self.strModel)


    def getNextNode(self):
        return self.nextNode


    def getPrevNode(self):
        return self.prevNode


    def setNextNode(self, node):
        self.nextNode = node


    def setPrevNode(self, node):
        self.prevNode = node
