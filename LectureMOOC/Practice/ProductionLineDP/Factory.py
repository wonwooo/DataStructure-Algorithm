import numpy as np
from ProductionList import ProductionList
from ManufacturingProcess import ManufacturingProcess
import matplotlib.pyplot as plt


class Factory(ManufacturingProcess):
    row = 2
    col = 5
    numStartProduct = 2

    def __init__(self, strFilename, breakProb):
        self.breakProb = breakProb
        self.waitingProduct = ProductionList(strFilename)
        self.completedProduct = ProductionList('')

        self.processes = [[[] for j in range(self.col)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if i == 0:
                    self.processes[i][j] = ManufacturingProcess('queue')
                elif i == 1:
                    self.processes[i][j] = ManufacturingProcess('stack')

    def selectLine(self, matCost):
        # Problem 1.
        # Return line = 1 or 2 by selecting a line by dynamic
        # programming. matCost = (Line) X (Processor)
        # Line = this.row
        # Processor = this.col

        # Memoization table
        matShortestCost = np.zeros((self.row, self.col))

        # Retrace table
        matPrevLine = np.zeros((self.row, self.col))

        # initialization of memoization table (the first col)
        for i in range(self.row):
            matShortestCost[i][0] = matCost[i][0]

        # dynamic programming iteration
        for i in range(1,self.col):
            for j in range(self.row):
                if matShortestCost[0][i - 1] + matCost[j][i] < matShortestCost[1][i - 1] + matCost[j][i]:
                    matShortestCost[j][i] = matShortestCost[0][i - 1] + matCost[j][i]
                    matPrevLine[j][i] = int(0)
                else:
                    matShortestCost[j][i] = matShortestCost[1][i - 1] + matCost[j][i]
                    matPrevLine[j][i] = int(1)

        # choice of line by the dynamic programming
        if matShortestCost[0][self.col-1] < matShortestCost[1][self.col-1]:
            endLine = int(0)
        else:
            endLine = int(1)

        for i in range(self.col-1, 0, -1):
            endLine = int(matPrevLine[endLine][i])

        line = endLine

        print('======================')
        print('Cost Matrix : ')
        print(matShortestCost)
        print('Retrace Matrix : ')
        print(matPrevLine)
        return line

    def getCostMatrix(self):
        matCost = np.zeros((self.row, self.col))
        for i in range(self.row):
            for j in range(self.col):
                matCost[i][j] = self.processes[i][j].getSize()
        return matCost

    def run(self):
        cntProduct = self.waitingProduct.getSize()
        cntltr = 0
        while self.completedProduct.getSize() != cntProduct:
            fig = plt.figure()
            for j in range(self.numStartProduct):
                product = self.waitingProduct.removeFirst()
                if product != 'none':
                    line = self.selectLine(self.getCostMatrix())
                    print('Selected Line : ', line)
                    print('Product No. : ', product.numNo)
                    self.processes[line][0].arriveProduct(product)

            for jj in range(self.col):
                j = self.col - jj
                for i in range(self.row):
                    if j == self.col:

                        plt.text(100 + j * 50, 100, self.completedProduct.getListString(), style='italic')
                    else:
                        plt.text(100 + j * 50, 50 + i * 100, self.processes[i][j].getListString(), style='italic')

            for i in range(self.row):
                plt.text(100, 50 + i * 100, self.processes[i][0].getListString(), style='italic')

            plt.text(50, 100, self.waitingProduct.getListString(), style='italic')
            plt.axis([0, 450, 0, 200])
            plt.show()
            for jj in range(self.col):
                j = self.col - jj
                for i in range(self.row):
                    if self.breakProb < np.random.uniform(0, 1):
                        if j == self.col:
                            product = self.processes[i][j - 1].leaveProduct()
                            if product != 'none':
                                self.completedProduct.addLast(product)
                        else:
                            product = self.processes[i][j - 1].leaveProduct()
                            if product != 'none':
                                self.processes[i][j].arriveProduct(product)
            cntltr += 1

        fig = plt.figure()
        plt.text(100 + self.col * 50, 100, self.completedProduct.getListString(), style='italic')
        plt.axis([0, 450, 0, 200])
        plt.show()

        print('Count Iteration :', cntltr)
