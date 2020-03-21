import matplotlib.pyplot as plt
import numpy as np


from PlanNode import PlanNode

class ProductionList(PlanNode):
    def __init__(self, Filename):

        self.nodeHead = PlanNode(-1, 'head', '', '', '', '', '', '')
        self.nodeTail = PlanNode(-1, 'tail', '', '', '', '', '', '')

        self.nodeHead.setNextNode(self.nodeTail)
        self.nodeTail.setPrevNode(self.nodeHead)

        if Filename != '':

            f = open(Filename)
            temp = f.readlines()
            f.close()

            dataset = []
            for row in temp[0:11]:
                dataset.append(row[:-1].split(','))
            Dataset = np.asarray(dataset[1:]).T

            numNos = Dataset[0].astype('int')
            strSerialNumbers = Dataset[1].astype('str')
            strModels = Dataset[2].astype('str')
            numModelNumbers = Dataset[3].astype('str')
            dateStart = Dataset[4].astype('str')
            numAssemblyOrders = Dataset[5].astype('str')
            dateEnd = Dataset[6].astype('str')
            strOrderOrigins = Dataset[7].astype('str')

            for i in range(len(numNos)):
                node = PlanNode(numNos[i], strSerialNumbers[i], strModels[i], numModelNumbers[i], dateStart[i],
                                numAssemblyOrders[i], dateEnd[i], strOrderOrigins[i])
                self.addLast(node)

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

    def addLast(self, node):
        nodeLast = self.nodeTail.getPrevNode()
        nodeLast.setNextNode(node)
        node.setPrevNode(nodeLast)
        node.setNextNode(self.nodeTail)
        self.nodeTail.setPrevNode(node)

    def addFirst(self, node):
        # Problem 1. complete the add first function of a doubly linked list
        nodeFirst = self.nodeHead.getNextNode()
        nodeFirst.setPrevNode(node)
        node.setNextNode(nodeFirst)
        node.setPrevNode(self.nodeHead)
        self.nodeHead.setNextNode(node)

    def removeLast(self):
        # Problem 1. complete the remove last function of a doubly linked list
        node = self.nodeTail.getPrevNode()
        if node.strSerialNumber != 'head':
            nodeNewLast = node.getPrevNode()
            nodeNewLast.segNextNode(self.nodeTail)
            self.nodeTail.setPrevNode(nodeNewLast)
        else:
            node = 'none'
        return node

    def removeFirst(self):
        node = self.nodeHead.getNextNode()
        if node.strSerialNumber != 'tail':
            nodeNewFirst = node.getNextNode()
            nodeNewFirst.setPrevNode(self.nodeHead)
            self.nodeHead.setNextNode(nodeNewFirst)
        else:
            node = 'none'
        return node

    def getSize(self):
        node = self.nodeHead
        cnt = 0
        while node.getNextNode().strSerialNumber != 'tail':
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