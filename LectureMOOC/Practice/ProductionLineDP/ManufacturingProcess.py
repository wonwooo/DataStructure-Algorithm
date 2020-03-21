from Queue import Queue
from Stack import Stack

class ManufacturingProcess(Queue, Stack):
    def __init__(self, typ):
        if typ == 'queue':
            self.waitingLine = Queue()
        if typ == 'stack':
            self.waitingLine = Stack()

    def arriveProduct(self, plan):
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