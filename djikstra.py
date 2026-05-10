from heapq import heapify, heappush, heappop

class Node:
    def __init__(self, value, neighbors=None, bestKnownValue=float('inf'), backPointer=None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []
        self.bestKnownValue = bestKnownValue
        self.backPointer = backPointer

    def __repr__(self):
        ans = ""
        ans += str(self.value)
        # ans += "|"
        # ans += str(self.bestKnownValue)
        # ans += "|"
        # if self.backPointer:
        #     ans += str(self.backPointer.value)
        
        return ans
    
    def __lt__(self, other):
        return self.bestKnownValue < other.bestKnownValue

def shortestPath(startNode, endNode, nodeMap):

    unvisited = []
    startNode.bestKnownValue = 0
    for node in nodeMap.values():
        unvisited.append(node)
    heapify(unvisited)

    visitCount = 0
    n = len(nodeMap)
    while visitCount < n:
        currentNode = heappop(unvisited)
        
        for pair in currentNode.neighbors:
            neighbor, distance = pair
            distanceThroughCurrentNode = currentNode.bestKnownValue + distance
            if distanceThroughCurrentNode < neighbor.bestKnownValue:
                neighbor.bestKnownValue = distanceThroughCurrentNode
                heappush(unvisited, neighbor)
                neighbor.backPointer = currentNode

        visitCount += 1

    path = []
    currentNode = endNode
    while currentNode.backPointer:
        path.append(currentNode)
        currentNode = currentNode.backPointer
    path.append(startNode)

    return list(reversed(path))



nodes = [i for i in range(0, 9)]
edges = [
    [0, 1, 4],
    [0, 7, 8],
    [1, 7, 11],
    [1, 2, 8],
    [7, 8, 7],
    [7, 6, 1],
    [2, 3, 7],
    [8, 2, 2],
    [2, 5, 4],
    [6, 8, 6],
    [6, 5, 2],
    [3, 5, 14],
    [3, 4, 9],
    [4, 5, 10],
]

nodeMap = {k : Node(k) for k in nodes}

for edge in edges:
    label1, label2, edgeWeight = edge
    node1, node2 = nodeMap[label1], nodeMap[label2]

    node1.neighbors.append((node2, edgeWeight))
    node2.neighbors.append((node1, edgeWeight))
    

ans = shortestPath(nodeMap[0], nodeMap[6], nodeMap)

print("ans:", ans)