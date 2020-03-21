class AssemblyLines:
    timeStation = [[7,9,3,4,8,4], [8,5,6,4,5,7]]#Station에서 생산하는 데 걸리는 시간
    timeBelt = [[2,2,3,1,3,4,3],[4,2,1,2,2,1,2]]#Station간 이동에 걸리는 시간
    intCount = 0
    def Scheduling(self, idxLine, idxStation): #해당하는 idxLine, idxStation까지의 최소 생산 시간을 계산하는 함수
        print("Calculate scheduling : line, station : ", idxLine, idxStation, "(", self.intCount, "recursion calls )")
        self.intCount = self.intCount + 1
        #Escape condition
        if idxStation == 0:
            if idxLine == 1:
                return self.timeBelt[0][0] + self.timeStation[0][0]
            elif idxLine == 2:
                return self.timeBelt[1][0] + self.timeStation[1][0]
        if idxLine == 1:
            costLine1 = self.Scheduling(1, idxStation-1) + self.timeStation[0][idxStation]
            costLine2 = self.Scheduling(2, idxStation-1) + self.timeStation[0][idxStation] + self.timeBelt[1][idxStation]
        elif idxLine == 2:
            costLine1 = self.Scheduling(1, idxStation-1) + self.timeStation[1][idxStation] + self.timeBelt[0][idxStation]
            costLine2 = self.Scheduling(2, idxStation-1) + self.timeStation[1][idxStation]
        if costLine1 > costLine2:
            return costLine2
        else:
            return costLine1

    def startScheduling(self):
        numStation = len(self.timeStation[0])
        costLine1 = self.Scheduling(1, numStation - 1) + self.timeBelt[0][numStation]
        costLine2 = self.Scheduling(2, numStation - 1) + self.timeBelt[0][numStation]
        if costLine1 > costLine2:
            return costLine2
        else:
            return costLine1