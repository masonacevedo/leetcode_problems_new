from heapq import heapify, heappush, heappop
def shortestPath(source, dest, adjList):
    
    bestSoFar = {node: float('inf') for node in adjList.keys()}

    bestSoFar[source] = 0
    
    heap = [(0, source)]
    visited = set()

    while len(heap) > 0:
        _, currentNode = heappop(heap)
        if currentNode in visited:
            continue

        for neighbor, distance in adjList[currentNode]:
            if bestSoFar[currentNode] + distance < bestSoFar[neighbor]:
                bestSoFar[neighbor] = bestSoFar[currentNode] + distance
                heappush(heap, (bestSoFar[neighbor], neighbor))
        
        visited.add(currentNode)

    return bestSoFar[dest]
                



nodes = [i for i in range(0, 5)]
edges = [
    [0, 4, 8],
    [0, 1, 3],
    [0, 3, 7],
    [4,3,7],
    [1,3,4],
    [1,2,1],
    [3,2,2]
]

ADJACENCY_LIST = {n : [] for n in nodes}

for edge in edges:
    node1, node2, edgeWeight = edge

    ADJACENCY_LIST[node1].append((node2, edgeWeight))
    ADJACENCY_LIST[node2].append((node1, edgeWeight))
    

ans = shortestPath(0, 2, ADJACENCY_LIST)

print("ans:", ans)