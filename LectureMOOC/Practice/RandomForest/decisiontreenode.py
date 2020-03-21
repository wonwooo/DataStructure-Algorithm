import csv
import math
from RandomForest.voterecord import Record

class Node:

    def __init__(self,depth,records):
        self.depth = depth
        self.blnSplit = False
        self.children = {}
        self.records = records
        self.decisionAttribute = -1
        self.stat = {}
        for type in Record.types:
            self.stat[type] = 0
            for record in records:
                if record.party == type:
                    self.stat[type] = self.stat[type] + 1

    def __str__(self):
        ret = ""
        if self.blnSplit == True:
            for itr in range(self.depth):
                ret = ret + "    "
            ret = ret + "+---"
            ret = 'Feature '+str(self.decisionAttribute)+ '('+str(self.stat)+')' + '\n'
            for key in self.children.keys():
                for itr in range(self.depth):
                    ret = ret + "    "
                ret = ret + "+---"
                ret = ret + "(" + key + ")" + str(self.children[key])
        else:
            ret = ret + "Closed Decision Leaf : " + str(self.stat) + "\n"
        return ret

    def splitNode(self):
        self.blnSplit = True
        gains = self.calculateInformationGainPerFeatures()
        idxMaxGainFeature = -1
        maxGain = -999999999999999999.0
        for itr in range(len(gains)):
            if maxGain < gains[itr]:
                maxGain = gains[itr]
                idxMaxGainFeature = itr

        for value in Record.values:
            childRecords = []
            for record in self.records:
                if record.feature[idxMaxGainFeature] == value:
                    childRecords.append(record)
            self.children[value] = Node(self.depth+1,childRecords)
        self.decisionAttribute = idxMaxGainFeature
        return self.children

    def calculateInformationGainPerFeatures(self):
        gains = []
        entropyClass = self.calculateClassEntropy()
        for itr in range(Record.numValues):
            entropyConditional = self.calculateConditionalEntropy(itr)
            gains.append( entropyClass - entropyConditional )
        return gains

    def calculateClassEntropy(self):
        entropy = 0.0
        for type in Record.types:
            cnt = 0.0
            for record in self.records:
                if record.party == type:
                    cnt = cnt + 1.0
            size = float(len(self.records))
            prob = cnt / size
            entropy = entropy - prob * math.log(prob,2)
        return entropy

    def calculateConditionalEntropy(self,idxFeature):
        entropy = 0.0
        for value in Record.values:
            for type in Record.types:
                cntFeature = 0.0
                cntFeatureAndClass = 0.0
                for record in self.records:
                    if record.feature[idxFeature] == value:
                        cntFeature = cntFeature + 1
                        if record.party == type:
                            cntFeatureAndClass = cntFeatureAndClass + 1.0
                size = float(len(self.records))
                probFeature = cntFeature / size + 0.0001
                probFeatureAndClass = cntFeatureAndClass / size + 0.0001
                entropy = entropy + probFeatureAndClass * math.log(probFeature/probFeatureAndClass,2)
        return entropy

if __name__ == "__main__":
    csvfile = open('house-votes-84.csv','rt')
    reader = csv.reader(csvfile,delimiter=',')
    records = []

    for row in reader:
        record = Record(row)
        print (record)
        records.append(record)

    node = Node(records)
    print(node)
    node.splitNode()
    print(node)