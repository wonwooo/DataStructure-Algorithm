class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

    def addNeighbor(self, valueNeighbor):
        if valueNeighbor not in self.neighbors:
            self.neighbors.append(valueNeighbor)


class Graph:
    vertexes = {}

    def __init__(self):
        self.vertexes = {}

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.value not in self.vertexes.keys():
            self.vertexes[vertex.value] = vertex

    def addEdge(self, src, dst):
        if src in self.vertexes.keys() and dst in self.vertexes.keys():
            self.vertexes[src].addNeighbor(dst)

    def reset(self):
        for value, vertex in self.vertexes.items():
            vertex.visited = None

    def dfsCycle(self, vertexValue, checkValue):
        global cycleMembers
        self.vertexes[vertexValue].visited = True
        for neighborValue in self.vertexes[vertexValue].neighbors:
            if not self.vertexes[neighborValue].visited:
                self.dfsCycle(neighborValue, checkValue)
            elif self.vertexes[neighborValue].visited and neighborValue == checkValue:
                cycleMembers.append(neighborValue)
                return

#Make Vertexes
N = int(input())
vertexList = [Vertex(i) for i in range(1, N+1)]
graph = Graph()
for v in vertexList:
    graph.addVertex(v)

#Add edge following inputs
for i in range(1, N+1):
    graph.addEdge(i, int(input()))

cycleMembers = []
for value, vertex in graph.vertexes.items():
    graph.dfsCycle(value, value)
    graph.reset()
print(len(cycleMembers))
for v in sorted(cycleMembers):
    print(v)




