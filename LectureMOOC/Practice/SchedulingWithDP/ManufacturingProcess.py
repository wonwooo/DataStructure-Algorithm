from Stack import Stack
from Queue import Queue

class ManufacturingProcess(Queue, Stack):
    def __init__(self, typ):
        if typ == 'queue':
            self.waitingLine = Queue()
        if typ == 'stack':
            self.waitingLine = Stack()

    def arriveProduct(self, plan):
        # Problem 4. complete the method call to add a product to the waiting line
        self.waitingLine.add(plan)

    def leaveProduct(self):
        if self.getSize() > 0:
            plan = self.waitingLine.get()
        else:
            plan = 'none'
        return plan

    def getSize(self):
        size = self.waitingLine.getSize()
        return size

    def getListString(self):
        String = self.waitingLine.getListString()
        return String
