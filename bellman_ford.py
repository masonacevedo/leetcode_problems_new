def bellmanFord(source, dest, adjList):
    bestSoFar = {}
    for edge in adjList:
        node1, node2, _ = edge
        bestSoFar[node1] = float('inf')
        bestSoFar[node2] = float('inf')
        
    bestSoFar[source] = 0
    
    for i in range(0, len(bestSoFar) - 1):
        madeOffer = makeOffers(adjList, bestSoFar)
        if not(madeOffer):
            print(f"breaking early at iteration {i}")
            break

    lastOffer = makeOffers(adjList, bestSoFar)
    if lastOffer:
        raise Exception("Negative cycle found in graph. No minimum path exists.")
    
    return bestSoFar

def makeOffers(adjList, bestSoFar):
    madeOffer = False
    for edge in adjList:
        source, dest, weight = edge
        if bestSoFar[source] + weight < bestSoFar[dest]:
            madeOffer = True
            bestSoFar[dest] = bestSoFar[source] + weight

    return madeOffer





ADJACENCY_LIST = [
    [0,1,10],
    [0,2,4],
    [1,0,10],
    [2,0,4],
    [1,2,3],
    [2,1,3],
    [1,4,0],
    [2,3,7],
    [3,2,7],
    [3,4,8],
    [4,3,8],
    [4,5,-6],
    [3,5,9],
    [5,3,9]
]

print("bellmanFord:", bellmanFord(0, 5, ADJACENCY_LIST))
