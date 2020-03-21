import csv
import math
from RandomForest.decisiontreenode import Node
from RandomForest.voterecord import Record

class DecisionTree:
    def __init__(self, records):
        self.root = Node(0,records)
        self.performID3()

    def performID3(self, node = None):
        if node == None:
            node = self.root
        node.splitNode()
        for key in node.children.keys():
            if 0 in node.children[key].stat.values():
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
                self.performID3withMaxDepth(maxDepth,currentDepth+1,node.children[key])
        return node

    def classify(self, test):
        types = Record.types
        currentNode = self.root
        while True:
            if currentNode.blnSplit == False:
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

        return result # for random forest

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
    tree.performID3()
    print(tree)
    
    test = ['y', 'y', '?', 'y', 'n', '?', '?', '?', 'n', 'n', 'n', 'y', 'n', '?', 'y', 'n']
    
    # classify
    tree.classify(test)
