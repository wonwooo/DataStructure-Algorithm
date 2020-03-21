import random
import csv

class DenseGraph:
    vertexes = []
    edges = {}
    
    def __init__(self,strFilename):
        self.vertexes = []
        self.edges = {}

        csvfile = open(strFilename, 'r')
        reader = csv.reader(csvfile)

        for row in reader:
            if row[0] not in self.vertexes:
                self.addVertex(row[0])
            self.addEdge(row[0], row[1], int(row[2]))

        csvfile.close()

    def addVertex(self, vertex):
        self.vertexes.append(vertex)
        self.edges[vertex] = {}
    
    def addEdge(self, src, dst, weight, directed=True):
        if directed == True:
            self.edges[src][dst] = weight
        else:
            self.edges[src][dst] = weight
            self.edges[dst][src] = weight

    def removeEdge(self,src,dst,directed=True):
        if directed == True:
            if dst in self.edges[src]:
                self.edges[src].pop(dst)
        else:
            if dst in self.edges[src]:
                self.edges[src].pop(dst)
            if src in self.edges[dst]:
                self.edges[dst].pop(src)

    def getNeighbors(self, vertex):
        retNeighbor = []
        retWeight = []
        for key in self.edges[vertex].keys():
            retNeighbor.append(key)
            retWeight.append(self.edges[vertex][key])
        return retNeighbor, retWeight

    def findComponent(self):
        checkVertex = {}
        for itr in range(len(self.vertexes)):
            checkVertex[self.vertexes[itr]] = False

        components = []
        for itr in range(len(self.vertexes)):
            vertex = self.vertexes[itr]
            if checkVertex[vertex] == False:
                component = []
                components.append(component)
                self.iterateNeighbors(vertex,checkVertex,component)
        return components

    def iterateNeighbors(self,vertex,checkVertex,component):
        checkVertex[vertex] = True
        component.append(vertex)
        for key in self.edges[vertex]:
            if checkVertex[key] == False:
                self.iterateNeighbors(key,checkVertex,component)

    def printComponent(self):
        components = self.findComponent()
        for itr in range(len(components)):
            print("Component "+str(itr)+" : "+str(len(components[itr])))
            for vertex in components[itr]:
                print(vertex+",",end="")
            print()

    def getWeight(self, src, dst):
        return self.edges[src][dst]

if __name__ == "__main__":
    g = DenseGraph('Subway-Seoul.csv')
    g.printComponent()
    for itr in range(30):
        pick1 = random.randint(0,len(g.vertexes))
        dsts = []
        for dst in g.edges[g.vertexes[pick1]].keys():
            dsts.append(dst)
        pick2 = random.randint(0,len(dsts)-1)
        g.removeEdge(g.vertexes[pick1],dsts[pick2])
        g.removeEdge(dsts[pick2], g.vertexes[pick1])
    g.printComponent()
