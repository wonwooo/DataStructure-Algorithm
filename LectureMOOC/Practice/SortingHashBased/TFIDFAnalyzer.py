import time
import sys
import csv
import math
import SortingHashBased.SortingAlgorithm
import SortingHashBased.BagOfWordCreator

class TFIDFAnalyzer:

    def __init__(self,folder,maxFileNumber,hashSize):
        dataset = BagOfWordCreator.BagOfWord(folder,maxFileNumber,hashSize,hash=True)
        dataset.printBagOfWords()
        self.words = dataset.words
        self.bows = dataset.bows
        self.numDocuments = len(self.bows)

    def writeImportantTerms(self,strFilename,topK):
        #sorting = SortingAlgorithm.SelectionSort()
        sorting = SortingAlgorithm.QuickSort()
        print("Start Sorting........")
        startTime = time.time()
        lstTFKeys, lstTFValues = analyzer.calculateTermFrequency()
        lstTFKeys, lstTFValues = sorting.performSorting(lstTFValues, lstTFKeys)
        lstDFKeys, lstDFValues = analyzer.calculateDocumentFrequency()
        lstDFKeys, lstDFValues = sorting.performSorting(lstDFValues, lstDFKeys)
        lstTFIDFKeys, lstTFIDFValues = analyzer.calculateTFIDF()
        lstTFIDFKeys, lstTFIDFValues = sorting.performSorting(lstTFIDFValues, lstTFIDFKeys)
        endTime = time.time()
        print("Finished Sorting........")
        print("Time : "+str((endTime-startTime)))

        file = open(strFilename,'w')
        file.write("Num,TF_Words,TF_Values,DF_Words,DF_Values,TFIDF_Words,TFIDF_Values\n")
        for itr in range(topK):
            line = str(itr)+","
            line = line + lstTFKeys[itr] + "," + str(lstTFValues[itr]) + ","
            line = line + lstDFKeys[itr] + "," + str(lstDFValues[itr]) + ","
            line = line + lstTFIDFKeys[itr] + "," + str(lstTFIDFValues[itr]) + "\n"
            file.write(line)
        file.close()

    def calculateTermFrequency(self):
        termFrequencies = []
        retWords = []
        # We have stored a list of words in "self.words"
        # Iterate the words to calculate the term frequency for each word
        # term frequency is the number of appearances of a word in all of the documents
        # You can use self.bows which is a list of dictionaries
        # A dictionary in the self.bows has the key as the index of a word in self.words and
        # the value is the appearance of the word in the document
        for idxWord in range(len(self.words)):
            retWords.append(self.words[idxWord])
            cnt = 0
            for idxBoW in range(len(self.bows)):
                if idxWord in self.bows[idxBoW]:
                    cnt = cnt + self.bows[idxBoW][idxWord]
            termFrequencies.append(cnt)
        return retWords,termFrequencies

    def calculateDocumentFrequency(self):
        documentFrequencies = []
        retWords = []
        # We have stored a list of words in "self.words"
        # Iterate the words to calculate the document frequency for each word
        # document frequency is the count of documents that has a word
        # You can use self.bows which is a list of dictionaries
        # A dictionary in the self.bows has the key as the index of a word in self.words and
        # the value is the appearance of the word in the document
        for idxWord in range(len(self.words)):
            retWords.append(self.words[idxWord])
            cnt = 0
            for idxBoW in range(len(self.bows)):
                if idxWord in self.bows[idxBoW]:
                    cnt = cnt + 1
            documentFrequencies.append(cnt)
        return retWords,documentFrequencies

    def calculateTFIDF(self):
        TFIDF = []
        words, termFrequencies = self.calculateTermFrequency()
        words, documentFrequencies = self.calculateDocumentFrequency()
        # calculate TF-IDF with the term frequencies and the document frequencies
        # TF[i] * log ( N / DF[i] )   , i is the word index, N is the number of documents (self.numDocuments)
        retWords = []
        for itr in range(len(self.words)):
            retWords.append(self.words[itr])
            TFIDF.append( termFrequencies[itr] * math.log(self.numDocuments / documentFrequencies[itr]) )
        return retWords, TFIDF

if __name__ == "__main__":
    analyzer = TFIDFAnalyzer('./talk.politics.misc', 100,20)
    lstKeys,lstValues = analyzer.calculateTermFrequency()
    lstKeys,lstValues = analyzer.calculateDocumentFrequency()
    lstKeys,lstValues = analyzer.calculateTFIDF()
    print("Before Sorting Keys : "+str(lstKeys))
    print("Before Sorting Values : " + str(lstValues))
    analyzer.writeImportantTerms('ImportantTerms.csv',100)


