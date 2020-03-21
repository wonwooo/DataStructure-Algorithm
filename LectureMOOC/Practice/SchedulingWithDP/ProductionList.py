import matplotlib.pyplot as plt
import numpy as np
from PlanNode import PlanNode

class ProductionList(PlanNode):
    def __init__(self, Filename):

        self.nodeHead = PlanNode(-1, 'head', '')
        self.nodeTail = PlanNode(-1, 'tail', '')

        self.nodeHead.setNextNode(self.nodeTail)
        self.nodeTail.setPrevNode(self.nodeHead)

        if Filename != '':

            f = open(Filename)
            temp = f.readlines()
            f.close()

            dataset = []
            for row in temp:
                dataset.append(row[:-1].split(','))
            Dataset = np.asarray(dataset[1:]).T

            numNos = Dataset[0].astype('int')
            strSerialNumbers = Dataset[1].astype('str')
            strModels = Dataset[2].astype('str')
            for i in range(len(numNos)):
                node = PlanNode(numNos[i], strSerialNumbers[i], strModels[i])
                node.printOut()
                self.addLast(node)

    def addLast(self, node):
        nodeLast = self.nodeTail.getPrevNode()
        nodeLast.setNextNode(node)
        node.setPrevNode(nodeLast)
        node.setNextNode(self.nodeTail)
        self.nodeTail.setPrevNode(node)

    def addFirst(self, node):
        # Problem 1. complete the add first function of a doubly linked list
        # 'node' at the first of the linked list
        nodeFirst = self.nodeHead.getNextNode()
        nodeFirst.setPrevNode(node)
        node.setPrevNode(self.nodeHead)
        node.setNextNode(nodeFirst)
        self.nodeHead.setNextNode(node)

    def removeLast(self):
        # Problem 1. complete the remove last function of a doubly linked list
        # remove the node at the last of the linked list
        node = self.nodeTail.getPrevNode()
        if node.numNo != -1:
            nodePrev = node.getPrevNode()
            nodePrev.setNextNode(self.nodeTail)
            self.nodeTail.setPrevNode(nodePrev)
        return node

    def removeFirst(self):
        #  Problem 1. complete the remove first function of a doubly linked list
        # remove the node at the first of the linked list
        node = self.nodeHead.getNextNode()
        if node.numNo != -1:
            nodeNext = node.getNextNode()
            nodeNext.setPrevNode(self.nodeHead)
            self.nodeHead.setNextNode(nodeNext)
        return node

    def getSize(self):
        # Problem 1. complete the code of a doubly linked list to
        # return the size of the linked list excluding head and tail nodes
        node = self.nodeHead
        cnt = 0
        while node.getNextNode().numNo != -1:
            node = node.getNextNode()
            cnt += 1
        return cnt

    def getListString(self):
        node = self.nodeHead
        ListString = ''
        while node.getNextNode().strSerialNumber != 'tail':
            node = node.getNextNode()
            ListString = ListString + ','
            ListString = ListString + str(node.numNo)
        return ListString

    def showPlanChart(self):

        allStartDate = []
        allModel = []
        node = self.nodeHead

        while node.getNextNode() != self.nodeTail:
            node = node.getNextNode()
            allStartDate.append(node.dateStart)
            allModel.append(node.strModel)

        Uniq_allModel = list(set(allModel))
        Counting_allModel = [allModel.count(a) for a in Uniq_allModel]
        xlabel = [i for i in range(len(Uniq_allModel))]
        plt.bar(xlabel[0:10], Counting_allModel[0:10], align='center')
        plt.xticks(xlabel[0:10], Uniq_allModel[0:10])
        plt.xlabel('Model')
        plt.ylabel('Number of Orders')
        plt.show()

        Uniq_allStartDate = list(set(allStartDate))
        Counting_dateStart = [allStartDate.count(a) for a in Uniq_allStartDate]
        xlabel = [i for i in range(len(Uniq_allStartDate))]
        plt.bar(xlabel[0:10], Counting_dateStart[0:10], align='center')
        plt.xticks(xlabel[0:10], Uniq_allStartDate[0:10])
        plt.xlabel('Date')
        plt.ylabel('Number of Orders')
        plt.show()