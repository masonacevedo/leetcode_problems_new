import math
from typing import List
from heapq import heappush, heappop, heapify

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = {}

        for i in range(0, n):
            adjList[i] = []

        for i in range(0, len(edges)):
            edge = edges[i]
            prob = succProb[i]
            
            edgeWeight = -math.log(prob) if prob != 0 else float('inf')

            node1, node2 = edge

            adjList[node1].append((node2, edgeWeight))
            adjList[node2].append((node1, edgeWeight))
        
        # print("adjList:", adjList)
        # for k,v in adjList.items():
        #     print(k,"|",v)

        bestSoFar = {i:float('inf') for i in adjList.keys()}
        bestSoFar[start_node] = 0

        # print("bestSoFar:", bestSoFar)

        unvisited = [(0, start_node)]
        visited = set()
        # print("before while loop")
        while len(visited) < n and len(unvisited) > 0:
            # print("unvisited:", unvisited)
            bestToCurrent, currentNode = heappop(unvisited)
            # print("bestToCurrent:", bestToCurrent)
            # print("currentNode:", currentNode)
            neighbors = adjList[currentNode]
            # print("neighbors:", neighbors)

            for pair in neighbors:
                neighbor, distance = pair
                # print("bestToCurrent:", bestToCurrent)
                # print("distance:", distance)
                # print("bestSoFar[neighbor]:", bestSoFar[neighbor])
                if distance + bestToCurrent < bestSoFar[neighbor]:
                    bestSoFar[neighbor] = distance + bestToCurrent
                    heappush(unvisited, (bestSoFar[neighbor], neighbor))

            visited.add(currentNode)
        
        # if we complete our traversal and we've emptied the visiting map without 
        # seeing all the nodes, this means that the start node is not connected
        # to the end node.
        if len(visited) == 0:
            return 0.0
        
        # print("bestSoFar:", bestSoFar)

        pathLength = bestSoFar[end_node]
        return 1/math.exp(pathLength)




s = Solution()
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
# edges = [[0,1]]
# succProb = [0.5]
start = 0
end = 2

ans = s.maxProbability(n, edges, succProb, start, end)
print("ans:", ans)