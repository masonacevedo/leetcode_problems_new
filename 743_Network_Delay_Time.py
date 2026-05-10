from typing import List
from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = {}

        for i in range(1, n+1):
            adjList[i] = []
        
        for triplet in times:
            source, dest, weight = triplet
            adjList[source].append((dest, weight))


        bestSoFar = {node: float('inf') for node in adjList.keys()}
        bestSoFar[k] = 0

        unvisited = [(0, k)]
        visited = set()
        
        while len(unvisited) > 0 and len(visited) < n:
            distanceToCurrentNode, currentNode = heappop(unvisited)

            neighbors = adjList[currentNode]

            for pair in neighbors:
                neighbor, edgeLength = pair
                if (distanceToCurrentNode + edgeLength) < bestSoFar[neighbor]:
                    bestSoFar[neighbor] = distanceToCurrentNode + edgeLength
                    heappush(unvisited, (bestSoFar[neighbor], neighbor))
            
            visited.add(currentNode)
        
        if max(bestSoFar.values()) == float('inf'):
            return -1
        else:
            return max(bestSoFar.values())
        
        
        


s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
ans = s.networkDelayTime(times, n, k)