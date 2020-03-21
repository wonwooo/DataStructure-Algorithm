

class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = set() #Weight있는 경우 dict로
        self.visited = False

    def addNeighbor(self, neighborValue):
        self.neighbors.add(neighborValue)

class Graph:
    vertexes = {}

    def __init__(self):
        self.vertexes = {}

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertexes.values():
            self.vertexes[vertex.value] = vertex

    def addEdge(self, src, dst):
        if src not in self.vertexes.keys():
            self.addVertex(Vertex(src))
        if dst not in self.vertexes.keys():
            self.addVertex(Vertex(dst))
        if src in self.vertexes.keys() and dst in self.vertexes.keys():
            self.vertexes[src].addNeighbor(dst)
            self.vertexes[dst].addNeighbor(src)

    def dfs(self, vertexValue):
        if self.vertexes[vertexValue].visited == False:
            self.vertexes[vertexValue].visited = True
        else:
            return
        print(vertexValue, end = ' ')
        for neighborValue in self.vertexes[vertexValue].neighbors:
            if not self.vertexes[neighborValue].visited:
                self.dfs(neighborValue)

    def bfs(self, vertexValue):
        if self.vertexes[vertexValue].visited == False:
            self.vertexes[vertexValue].visited = True
        else:
            return
        queue = [vertexValue]
        while len(queue) != 0:
            current = queue.pop(0)
            print(current, end = ' ')
            for neighborValue in self.vertexes[current].neighbors:
                if not self.vertexes[neighborValue].visited:
                    self.vertexes[neighborValue].visited = True
                    queue.append(neighborValue)

    def reset(self):
        for value, vertex in self.vertexes.items():
            vertex.visited = False



graphdfs = Graph()
graphbfs = Graph()
V, E, vertexValue = map(int, input().split())

for i in range(E):
    src, dst = map(int, input().split())
    graphdfs.addEdge(src, dst)
    graphbfs.addEdge(src, dst)
graphdfs.dfs(vertexValue)
print()
graphbfs.bfs(vertexValue)





