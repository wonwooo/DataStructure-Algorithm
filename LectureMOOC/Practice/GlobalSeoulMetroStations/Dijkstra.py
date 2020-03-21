from Graph import DenseGraph
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
        minDist = 99999999
        min_vertex = None
        for vertex in Vertexes:
            if dist[vertex] < minDist:
                min_vertex = vertex
                minDist = dist[vertex]
        if minDist == 99999999:
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

def performAllDestinationDijkstra(graph, src):
    dist = {}
    path = {}
    routes = {}
    Vertexes = []
    for vertex in graph.vertexes:
        dist[vertex] = 99999999
        path[vertex] = None
        Vertexes.append(vertex)
    dist[src] = 0

    while len(Vertexes) != 0:
        minDist = 99999999
        min_vertex = None
        for vertex in Vertexes:
            if dist[vertex] < minDist:
                min_vertex = vertex
                minDist = dist[vertex]
        if minDist == 99999999:
            break
        Vertexes.remove(min_vertex)

        neighbors, weights = graph.getNeighbors(min_vertex)
        for itr in range(len(neighbors)):
            if dist[neighbors[itr]] > dist[min_vertex] + weights[itr]:
                dist[neighbors[itr]] = dist[min_vertex] + weights[itr]
                path[neighbors[itr]] = min_vertex

				
	# Return "routes" as a dictionary with a key of string vertex
	# Each value of the key should be a list of the route from the source as the input to the destination of the key which is a station
    for vertex in graph.vertexes:
        next = vertex
        temp = [next]
        while next != src:
            ????????? = ?????????[?????????]
            if next == None:
                temp = None
                break
            temp = [?????????] + temp
        routes[?????????] = temp

    return dist, path, routes

if __name__ == "__main__":
    g = DenseGraph('Subway-Seoul.csv')

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
