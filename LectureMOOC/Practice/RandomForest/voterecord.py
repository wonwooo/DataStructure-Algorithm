class Record:

    types = ['republican','democrat']
    values = ['y','n','?']
    numValues = 16

    def __init__(self,csvline):
        self.party = csvline[0]
        self.feature = []
        for itr in range(1,len(csvline)):
            self.feature.append(csvline[itr])

    def __str__(self):
        ret = 'Classficiation : '+self.party+', Features : '+str(self.feature)
        return ret
