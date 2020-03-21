class DenseGraph:
    vertexes = []
    edges = {}

    def __init__(self):
        self.vertexes = []
        self.edges = {}

    def addVertex(self, vertex):
        self.vertexes.append(vertex)
        self.edges[vertex] = {}

    def addEdge(self, src, dst, weight, directed):
        if directed == True:
            self.edges[src][dst] = weight
        else:
            self.edges[src][dst] = weight
            self.edges[dst][src] = weight


   def getNeighbors(self, vertex):
        retNeighbor = []
        retWeight = []
        for dst in self.edges[vertex].keys():
            retNeighbor.append(dst)
            retWeight.append(self.edges[vertex][dst])
        return retNeighbor, retWeight

    def getWeight(self, src, dst):
        return self.edges[src][dst]