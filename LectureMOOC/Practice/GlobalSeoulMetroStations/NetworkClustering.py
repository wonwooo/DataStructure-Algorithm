import sys
import Dijkstra
import Graph
import csv

class NewmanClustering:

    def __init__(self):
        pass

    def performNewmanClustering(self, graph, K):
        lstVertexes = graph.vertexes

        print("-------------------------------")
        print("Initial Dataset")
        graph.printComponent()

        cnt = 0
        while True:
			# Compute the edge-betweenness
            matBetweenness = self.????????????????????(?????????)
            maxBetweenness = 0.0
            idxSrcEdge = -1
            idxDstEdge = -1
			
            for itr1 in range(len(lstVertexes)):
                for itr2 in range(len(lstVertexes)):
					# Find the maximum value of the edge-betweenness, and store the index of the source and the destination stations
                    if ?????????????[lstVertexes[itr1]][lstVertexes[itr2]] > ????????????:
                        ????????????? = ?????????[lstVertexes[itr1]][lstVertexes[itr2]]
                        idxSrcEdge = itr1
                        idxDstEdge = itr2
						
			# Remove the edge with the maximum edge-betweenness
            graph.?????????(lstVertexes[idxSrcEdge],lstVertexes[idxDstEdge])
            graph.?????????(lstVertexes[idxDstEdge],lstVertexes[idxSrcEdge])
            components = graph.findComponent()
            print("-------------------------------")
            print("Iteration "+str(cnt))
            graph.printComponent()
            if len(components) == K:
                break
            cnt = cnt + 1

    def calculateEdgeBetweenness(self, graph):
        lstVertexes = graph.vertexes
        matBetweenness = {}
        for itr1 in range(len(lstVertexes)):
            matBetweenness[lstVertexes[itr1]] = {}
            for itr2 in range(len(lstVertexes)):
                matBetweenness[lstVertexes[itr1]][lstVertexes[itr2]] = 0.0

        print("Calculating Betweenness ")
        for itr1 in range(len(lstVertexes)):
            print(".",end="")
            sys.stdout.flush()
            dist, path, routes = Dijkstra.performAllDestinationDijkstra(graph, lstVertexes[itr1])
            for itr2 in range(len(lstVertexes)):
                if itr1 == itr2:
                    continue
				
				# Remember that "routes" is a dictionary with a string key as a station name
				# lstVertexes[itr1] is the source
				# lstVertexes[itr2] is the destination
				# routes[lstVertexes[itr2] is the list of the station in the path between the source and the destination
				# You need to increase the matrix of the edge-betweenness
                if routes[lstVertexes[itr2]] != None:
                    for itr3 in range(len(routes[lstVertexes[itr2]])-1):
                        srcIncludedEdge = routes[lstVertexes[itr2]][itr3]
                        dstIncludedEdge = routes[lstVertexes[itr2]][itr3+1]
                        ?????????[srcIncludedEdge][dstIncludedEdge] = ?????????[srcIncludedEdge][dstIncludedEdge] + 1
                        ?????????[dstIncludedEdge][srcIncludedEdge] = ?????????[dstIncludedEdge][srcIncludedEdge] + 1
        print()
        return matBetweenness

if __name__ == "__main__":
    #g = Graph.DenseGraph('Subway-Seoul-ver-2.csv')
    g = Graph.DenseGraph('Subway-Seoul.csv')
    clustering = NewmanClustering()
    clustering.performNewmanClustering(g,10)
