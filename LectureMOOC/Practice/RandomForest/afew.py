import csv
import math
from RandomForest.decisiontreenode import Node
from RandomForest.voterecord import Record

class DecisionTree:
    def __init__(self, records):
        self.root = Node(0, records)
        self.performID3()

    def performID3(self, node = None):
        if node == None:
            node = self.root
        node.splitNode()
        for key in node.children.keys():
            if 0 in node.children[key].stat.values():
                '''stat은 해당 node가 가진 records의 type('repub' or 'democ')의 갯수
                0이라는 것은 더이상 node를 쪼갤 필요가 없다는뜻'''
                pass
            else:
                self.performID3(node.children[key])
        return node

    def performID3withMaxDepth(self, maxDepth, currentDepth = 0, node = None):
        if node == None:
            node = self.root
            currentDepth = 0
        if currentDepth == maxDepth:
            return node
        node.splitNode()
        for key in node.children.keys():
            if 0 in node.children[key].stat.values():
                pass
            else:
                self.performID3withMaxDepth(maxDepth, currentDepth+1, node.children[key])
        return node

    def classify(self, test):
        types = Record.types #['republican', 'democrat']
        currentNode = self.root
        while True:
            if currentNode.blnSplit == False: #더이상 쪼개지지 않는 node에 도착하면 학습 데이터 중 가장 많았던 type으로 분류
                result = None
                if currentNode.stat[types[0]] > currentNode.stat[types[1]]:
                    result = types[0]
                elif currentNode.stat[types[0]] < currentNode.stat[types[1]]:
                    result = types[1]
                else:
                    result = None
                break
            else:
                currentNode = currentNode.children[test[currentNode.decisionAttribute]]

        return result #for random forest

    def __str__(self):
        ret = str(self.root)
        return ret
if __name__ == "__main__":
    csvfile = open('house-votes-84.csv', 'rt')
    reader = csv.reader(csvfile, delimiter=',')
    records = []

    for row in reader:
        record = Record(row)
        records.append(record)

    tree = DecisionTree(records)
    tree.performID3withMaxDepth(maxDepth = 3)

    test = ['y', 'y', '?', 'y', 'n', '?', '?', '?', 'n', 'n', 'n', 'y', 'n', '?', 'y', 'n']

    result = tree.classify(test)
    print("Classification Result :",result)

    print(tree)




