import sys
from os import listdir
from os.path import isfile, join

class BagOfWord:

    def __init__(self,folder,maxFileNumber):
        files = [f for f in listdir(folder) if isfile(join(folder,f))]
        self.words = []
        self.bows = []
        cnt = 0
        for file in files:
            cnt = cnt + 1
            print("File Num : "+str(cnt)+" Loading : "+folder+"/"+str(file))
            tempBoW = self.createBow(folder,file)
            self.bows.append(tempBoW)
            if cnt == maxFileNumber:
                break

    def createBow(self,folder,file):
        tempBoW = {}
        file = open(folder+"/"+str(file),"r")
        while True:
            line = file.readline()
            if not line:
                break
            for token in line.split(" "):
                token = token.replace(',','')
                token = token.rstrip()
                token = token.strip()
                if token.strip() == '':
                    continue
                if token in self.words:
                    for itr in range(len(self.words)):
                        if self.words[itr] == token:
                            idxWord = itr
                            break
                else:
                    self.words.append(token)
                    idxWord = len(self.words)
                if idxWord in tempBoW.keys():
                    tempBoW[idxWord] = tempBoW[idxWord] + 1
                else:
                    tempBoW[idxWord] = 1
                #print(token+","+str(idxWord))
        file.close()
        return tempBoW

    def printBagOfWords(self):
        print ("Words : "+str(self.words))
        cnt = 0
        for bow in self.bows:
            cnt = cnt + 1
            print ("Num : "+str(cnt)+" Document BoW : "+str(bow))

if __name__ == "__main__":
    creator = BagOfWord('./talk.politics.misc',100)
    creator.printBagOfWords()
