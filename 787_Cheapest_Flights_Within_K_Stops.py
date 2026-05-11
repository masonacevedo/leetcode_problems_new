from typing import List
from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adjList = {}

        for i in range(0, n):
            adjList[i] = []
        
        for triplet in flights:
            source, destination, weight = triplet

            adjList[source].append((destination, weight))
        
        # for key,value in adjList.items():
        #     print(key,"|",value)
        
        hopsSoFar = {node: float('inf') for node in adjList.keys()}
        hopsSoFar[src] = -1
        bestSoFar = {node: float('inf') for node in adjList.keys()}
        bestSoFar[src] = 0

        # print()
        # for key,value in bestSoFar.items():
        #     print(key,"|",value)

        
        unvisited = [(0, src, -1)]
        visited = set()

        while len(visited) < n and len(unvisited) > 0:
            priceToCurrent, currentNode, numStopsToCurrent = heappop(unvisited)
            # print("currentNode:", currentNode)
            # print("numStopsToCurrent:", numStopsToCurrent)
            # print("priceToCurrent:", priceToCurrent)
            # input()
            if numStopsToCurrent > k:
                continue

            neighbors = adjList[currentNode]

            for pair in neighbors:
                neighbor, edgeWeight = pair
                
                if (priceToCurrent + edgeWeight) < bestSoFar[neighbor] and (numStopsToCurrent+1 <= hopsSoFar[neighbor]):
                    # make relaxation offer!!
                    bestSoFar[neighbor] = priceToCurrent + edgeWeight
                    hopsSoFar[neighbor] = numStopsToCurrent+1
                    heappush(unvisited, (bestSoFar[neighbor], neighbor, hopsSoFar[neighbor]))
                    pass

        # for key, val in bestSoFar.items():
        #     print(key,"|",val)
        
        return bestSoFar[dst]

s = Solution()

# n = 4
# flights = [
#     [0,1,100],
#     [1,2,100],
#     [2,0,100],
#     [1,3,600],
#     [2,3,200]
# ]
# src = 0
# dst = 3
# k = 1


n = 5
flights = [
    [0, 1, 999],
    [0, 1, 10],
    [1, 2, 10],
    [0, 3, 1],
    [0, 4, 5],
    [3, 4, 1],
    [4, 2, 1],
]

src = 0
dst = 2
k = 1

s.findCheapestPrice(n, flights, src, dst, k)