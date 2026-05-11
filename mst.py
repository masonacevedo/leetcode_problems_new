from heapq import heappush, heappop

def minimumSpanningTree(adjList):

    firstVertex = list(adjList.keys())[0]
    unvisited = [(0, firstVertex)]

    totalCost = 0
    visited = set()
    while len(unvisited) > 0:
        costToAdd, currentNode = heappop(unvisited)
        if currentNode in visited:
            continue
        
        # adjList
        totalCost += costToAdd

        for pair in adjList[currentNode]:
            neighbor, edgeWeight = pair
            if neighbor not in visited:
                heappush(unvisited, (edgeWeight, neighbor))

        visited.add(currentNode)
    
    return totalCost


    
    pass


n = 4

edges = [
    [0,1,10],
    [0,3,5],
    [0,2,6],
    [1,3,15],
    [2,3,4],
]

adjList = {}

for i in range(0, n):
    adjList[i] = []


for triplet in edges:
    node1, node2, weight = triplet
    
    adjList[node1].append((node2, weight))

    adjList[node2].append((node1, weight))
    
ans = minimumSpanningTree(adjList)
print("ans:", ans)