# idea: Implemenet djikstra's algorithm, then look at the node 
#       with the highest distance.
from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {node: [] for node in range(1,n+1)}

        for triplet in times:
            source, dest, weight = triplet
            adjList[source].append((dest, weight))
        
        bestSoFar = {node: float('inf') for node in adjList.keys()}
        bestSoFar[k] = 0

        heap = [(0, k)]
        visited = set()
        while len(heap) > 0:
            _, currentNode = heappop(heap)
            
            if currentNode in visited:
                continue
            
            for neighbor, distance in adjList[currentNode]:
                if bestSoFar[currentNode] + distance < bestSoFar[neighbor]:
                    bestSoFar[neighbor] = bestSoFar[currentNode] + distance
                    heapPair = (bestSoFar[neighbor], neighbor)
                    heappush(heap, heapPair)


            visited.add(currentNode)

        furthestDistance = max(bestSoFar.values())
        if furthestDistance == float('inf'):
            return -1
        
        return furthestDistance



s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
ans = s.networkDelayTime(times, n, k)
print("ans:", ans)