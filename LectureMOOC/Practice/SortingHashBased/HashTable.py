import numpy as np

class HashTable:

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0 # number of key in self.keys
        self.keys = [] # unique strWord list
        self.data = np.asarray([[None,None]] * capacity)
        self.recordLoadFactor = []
        self.recordHashSize = []

    def calculateHashFunction(self,strWord):
        # f(key) function
        # Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
        # For example, ord('a') returns the integer 97
        # ord('€') (Euro sign) returns 8364
        hashValue = 0
        for i in range(len(strWord)):
            hashValue = hashValue + ord(strWord[i]) * ord(strWord[i])
        return hashValue % self.capacity

    def put(self, strWord, idxWord):
        # key is the strWord
        # value is the idxWord
        # get the key-value pair in the hash table
        trial = 0
        if self.size >= self.capacity / 2:
            self.doubleSize()
        hashValue = self.calculateHashFunction(strWord)
        while True:
            idx = (hashValue + trial + trial*trial ) % self.capacity
            if self.data[idx][1] == None:
                self.data[idx][0] = strWord
                self.data[idx][1] = idxWord
                self.size += 1
                self.keys.append(strWord)
                break
            if self.data[idx][0] == strWord:
                break
            trial += 1
        self.recordLoadFactor.append(self.getLoadFactor())
        self.recordHashSize.append(self.capacity)

    def doubleSize(self): #capacity만 2배로 만드는 함수
        tempHash = HashTable(self.capacity * 2 )
        print("!!!!! Doubling Hash !!!!!")
        # You need to know all existing keys in the current hash table
        # to reinsert the values to the temp hash table
        # Reinsert the values
        for key in self.keys:
            tempHash.put(key, self.get(key))

        # Substitute the properties of the temp hash table with those of the
        # current hash table
        self.keys = tempHash.keys
        self.capacity = tempHash.capacity
        self.size = tempHash.size
        self.data = tempHash.data

    def get(self, strWord):
        # find the corresponding idxWord of the strWord
        # return the value from the key-value pair
        # return None if the no key is found
        idxWord = None
        trial = 0
        hashValue = self.calculateHashFunction(strWord)
        while True:
            idx = ( hashValue + trial + trial*trial ) % self.capacity
            if self.data[idx][0] == strWord:
                idxWord = self.data[idx][1]
                break
            else:
                if self.data[idx][1] == None:
                    break
            trial += 1

        return idxWord

    def getLoadFactor(self):
        LoadFactor = self.size / self.capacity
        return LoadFactor

    def __repr__(self):
        return '{ ' + ', '.join([key + ':' + str(self.get(key)) for key in self.keys]) + ' }'
