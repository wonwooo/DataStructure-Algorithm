from RandomForest.decisiontree import DecisionTree
from RandomForest.voterecord import Record
import csv, random
import sys
sys.path.append("C:/Users/a2678/Desktop/DataStructure.RandomForest")

class RandomForest:
    def __init__(self, records, numSubSample, numTrees, maxDepth):
        self.trees = []
        # create |numTrees| decision trees with random sub-samples of |numSubSample|

        self.records = records
        for _ in range(numTrees):
            # make tree by sampled records
            tree_record = random.sample(records, numSubSample)
            tree = DecisionTree(tree_record)
            tree.performID3withMaxDepth(maxDepth)
            self.trees.append(tree)


    def classify(self, test):
        results = {key : 0 for key in Record.types}
        for tree in self.trees:
            # count results of trees
            types = Record.types
            result = tree.classify(test)
            if result == types[0]:
                results[types[1]] += 1

                maxVote = 0
                maxType = None
                results[types[0]] += 1
            else:
        for type in results.keys():
            # return max vote
            if results[type] > maxVote:
                maxType = type
                maxVote = results[type]
        return maxType

    def __str__(self):
        # create this method to visualize the multiple trees
        ret = ""
        for i, tree in enumerate(self.trees):
            ret += "\n*************** Tree %s ***************\n" %(i)
            ret += str(tree)
        return ret

class Evaluator:
    def evaluation(self,classifier,records):
        ret = 0.0
        for record in records:
            if classifier.classify(record.feature) == record.party:
                ret = ret + 1.0
        ret = ret / float(len(records))
        return ret

if __name__ == "__main__":
    csvfile = open('house-votes-84.csv', 'rt')
    reader = csv.reader(csvfile, delimiter=',')

    trainingRecords = []
    testingRecords = []
    cnt = 0
    for row in reader:
        record = Record(row)
        cnt = cnt + 1
        if cnt < 300:
            trainingRecords.append(record)
        else:
            testingRecords.append(record)

    forest = RandomForest(trainingRecords, 200, 3, 3)
    tree = DecisionTree(trainingRecords)

    print("Printing Random Forest")
    print(str(forest))
    print("--------------------------------------------")
    print("Feature for a single classification : "+str(trainingRecords[0].feature))
    print("True result for a single classification : " + str(trainingRecords[0].party))
    print("Est. result from random forest : " + str(forest.classify(trainingRecords[0].feature)))
    print("Est. result from decision tree : " + str(tree.classify(trainingRecords[0].feature)))
    print("--------------------------------------------")
    eval = Evaluator()
    print("Est. average accuracy from random forest : " + str(eval.evaluation(forest,testingRecords)))
    print("Est. average accuracy from decision tree : " + str(eval.evaluation(tree,testingRecords)))



