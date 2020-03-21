from os import listdir
from os.path import isfile, join
from HashTable import HashTable
import matplotlib.pyplot as plt
import time

class BagOfWord:

    def __init__(self,folder,maxFileNumber,hashSize,hash=True):
        files = [f for f in listdir(folder) if isfile(join(folder,f))]
        self.hash = hash
        self.words = []
        self.bows = []
        cnt = 0
        self.hashTable = HashTable(hashSize)
        for file in files:
            cnt = cnt + 1
            print("File Num : "+str(cnt)+" Loading : "+folder+"/"+str(file))
            if hash == True:
                tempBoW = self.createBowWithHash(folder,file)
            else:
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
        file.close()
        return tempBoW

    def createBowWithHash(self,folder,file):
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
                ###############################################
                # Need to change the code to use Hash Structure
                # token in self.words --> hash.get(token) != None
                idxWord = self.hashTable.get(token) #HashTable에 없는 단어를 추가해야할때
                if idxWord == None:
                    # key : strWord(token)
                    # value : 0,1,2,3,....
                    idxWord = len(token)
                    self.words.append(token)
                    self.hashTable.put(token,idxWord)
                ###############################################
                if idxWord in tempBoW.keys():
                    tempBoW[idxWord] = tempBoW[idxWord] + 1
                else:
                    tempBoW[idxWord] = 1
        file.close()
        return tempBoW

    def printBagOfWords(self):
        print ("Words : "+str(self.words))
        cnt = 0
        for bow in self.bows:
            cnt = cnt + 1
            print ("Num : "+str(cnt)+" Document BoW : "+str(bow))
        if self.hash == True:
            fig, ax1 = plt.subplots()
            ax1.plot(self.hashTable.recordLoadFactor, 'b-')
            ax1.set_xlabel('Num. of Key-Value Pairs')
            ax1.set_ylabel('Load Factor', color='b')
            ax1.tick_params('y', colors='b')

            ax2 = ax1.twinx()
            ax2.plot(self.hashTable.recordHashSize, 'r-')
            ax2.set_ylabel('Hash Size', color='r')
            ax2.tick_params('y', colors='r')

            fig.tight_layout()
            plt.show()

if __name__ == "__main__":
    tic = time.time()
    creator = BagOfWord('./talk.politics.misc',100,50,hash=True)
    elapsedTime = time.time() - tic
    creator.printBagOfWords()
    print("Elapsed Time for BOW : " + str(elapsedTime))


