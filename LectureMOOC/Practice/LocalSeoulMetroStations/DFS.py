class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.distance = 9999
        self.color = 'black'

    def addNeighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertexes = {}

    def __init__(self):
        self.vertexes = {} #name:vertex

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertexes:
            self.vertexes[vertex.name] = vertex
            return True
        else:
            return False


    def addEdge(self, src, dst, weight=None, directed=None):
        if src in self.vertexes and dst in self.vertexes:
            self.vertexes[src].addNeighbor(dst)
            self.vertexes[dst].addNeighbor(src)


    def dfsStack(self, vertex):
        vertex.color = 'red'
        stack = []
        stack.append(vertex)
        while len(stack)!=0:
            current = stack.pop()
            for nameNeighbor in current.neighbors:
                if self.vertexes[nameNeighbor].color == 'black':
                    self.vertexes[nameNeighbor].color = 'red'
                    stack.append(self.vertexes[nameNeighbor])
            print(current.name, end=' ')


    def dfsRecursion(self, vertex):
        vertex.color = 'red'
        print(vertex.name, end=' ')

        for nameNeighbor in vertex.neighbors:
            if self.vertexes[nameNeighbor].color == 'black':
                self.dfsRecursion(self.vertexes[nameNeighbor])

    def bfs(self, vertex):
        que = []
        vertex.color='red'
        que.append(vertex)
        while len(que) != 0:
            for nameNeighbor in que[0].neighbors:
                if self.vertexes[nameNeighbor].color == 'black':
                    que.append(self.vertexes[nameNeighbor])
                    self.vertexes[nameNeighbor].color = 'red'

            print(que.pop(0).name, end=' ')



if __name__ == '__main__':

    vertexNames = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    vertexList = [Vertex(name) for name in vertexNames]
    edgeList = [(1,3), (5,3), (3,2), (2,0), (0,1), (5,7), (5,4), (4,6), (7,6), (7,9), (9,8)]
    edgeList = [tuple(map(str, x)) for x in edgeList]

    graph = Graph()
    for v in vertexList:
        graph.addVertex(v)
    for edge in edgeList:
        src = edge[0]
        dst = edge[1]
        graph.addEdge(src, dst)

    graph.dfsRecursion(vertexList[5])
    #graph.bfs(vertexList[5])
    #graph.dfsStack(vertexList[5])



