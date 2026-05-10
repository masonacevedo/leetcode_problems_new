from heapq import heapify, heappush, heappop

class Node:
    def __init__(self, value, neighbors=None, bestKnownValue=float('inf')):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []
        self.bestKnownValue = bestKnownValue

    def __repr__(self):
        ans = ""
        ans += str(self.value)
        ans += "|"
        ans += str(self.bestKnownValue)
        # ans += "->"
        # for pair in self.neighbors:
        #     node, distance = pair
        #     ans += "(" + str(node.value) + "," + str(distance) + ");"
        
        return ans
    
    def __lt__(self, other):
        return self.bestKnownValue < other.bestKnownValue

def shortestPath(startNode, endNode, nodeMap):
    # idea: first, maintain a dictionary of all the nodes we haven't visited yet.
    # node 1 starts at a distance away of 0, and all else is infinitely far away. 
    # Then, iterate through the neighbors: make a relaxation offer to each neighbor.
    # then, find the unvisited node with the lowest known distance. hop there,
    # then make relaxation offers from there. 


    unvisited = []
    startNode.bestKnownValue = 0
    for node in nodeMap.values():
        unvisited.append(node)
    heapify(unvisited)
    print("unvisited heap:", unvisited)
    print()
    visited = set()

    # # while there remain unvisited nodes...
    while len(visited) < len(nodeMap):
        print("about to pop off heap!")
        # input("")
        currentNode = heappop(unvisited)
        print("popped off heap! result:")
        print("currentNode:", currentNode)
        # input("")
        
        for pair in currentNode.neighbors:
            neighbor, distance = pair
            distanceThroughCurrentNode = currentNode.bestKnownValue + distance
            print("making relaxation offer")
            print("distanceThroughCurrentNode:", distanceThroughCurrentNode)
            if distanceThroughCurrentNode < neighbor.bestKnownValue:
                print("offer accepted")
                neighbor.bestKnownValue = distanceThroughCurrentNode
                heappush(unvisited, neighbor)
                print("unvisited:", unvisited)
            else:
                print("offer rejected")

            # input("")
            print("\n")
        
        visited.add(currentNode)


    for node in nodeMap.values():
        print("node:", node)



nodes = [i for i in range(0, 5)]
edges = [
    [0, 1, 4],
    [0, 2, 8],
    [1, 2, 3],
    [1, 4, 6],
    [2, 3, 2],
    [4, 3, 10]
]

nodeMap = {k : Node(k) for k in nodes}

for edge in edges:
    label1, label2, edgeWeight = edge
    node1, node2 = nodeMap[label1], nodeMap[label2]

    node1.neighbors.append((node2, edgeWeight))
    node2.neighbors.append((node1, edgeWeight))
    

for k,v in nodeMap.items():
    print(k,"|",v)



ans = shortestPath(nodeMap[0], nodeMap[3], nodeMap)
print('ans:', ans)