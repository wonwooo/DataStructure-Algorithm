from LocalSeoulMetroStations.Graph import DenseGraph
import csv

def performDijkstra(graph, src, dst):
    dist = {}
    path = {}
    Vertexes = []
    for vertex in graph.vertexes:
        dist[vertex] = 99999999
        Vertexes.append(vertex)
    dist[src] = 0

    while len(Vertexes) != 0:
        #mindist, minvertex 찾는 부분 PriorityQueue로 구현가능
        minDist = 9999999
        min_vertex = None
        for vertex in Vertexes:
            if dist[vertex] < minDist:
                min_vertex = vertex
                minDist = dist[vertex]
        if minDist == 9999999:
            break
        Vertexes.remove(min_vertex)

        neighbors, weights = graph.getNeighbors(min_vertex)
        for itr in range(len(neighbors)):
            if dist[neighbors[itr]] > dist[min_vertex] + weights[itr]:
                dist[neighbors[itr]] = dist[min_vertex] + weights[itr]
                path[neighbors[itr]] = min_vertex

    course = dst
    next = dst
    while next != src:
        next = path[next]
        course = next + '->' + course

    return dist, path, course


if __name__ == "__main__":
    csvfile = open('Subway-Seoul.csv', 'r')
    reader = csv.reader(csvfile)
    g = DenseGraph()

    for row in reader:
        if row[0] not in g.vertexes:
            g.addVertex(row[0])
        g.addEdge(row[0], row[1], int(row[2]), True)

    while True:
        src = input('Source Station (예,''동두천'', type ''quit'' to quit): ')
        if src == 'quit':
            break
        elif src not in g.vertexes:
            print(src +  " is not subway station, please try again")
            continue
        dst = input('Destination Station (예,''서울대입구''): ')
        if dst not in g.vertexes:
            print(dst + " is not subway station, please try again")
            continue

        dist, path, course = performDijkstra(g, src, dst)
        print("Path")
        print(course)
        print("Distance:")
        print(dist[dst])
