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
        
        # for key,v in adjList.items():
        #     print(key,"|",v)


        bestSoFar = {node: float('inf') for node in adjList.keys()}

        bestSoFar[k] = 0

        # for key,v in bestSoFar.items():
        #     print(key,"|",v)

        unvisited = [(0, k)]
        visited = set()

        
        while len(unvisited) > 0 and len(visited) < n:
            # print("len(unvisited):", len(unvisited))
            # print("len(visited):", len(visited))
            distanceToCurrentNode, currentNode = heappop(unvisited)
            # print("currentNode:", currentNode)
            # print('distanceToCurrentNode:', distanceToCurrentNode)
            # input()

            neighbors = adjList[currentNode]

            for pair in neighbors:
                neighbor, edgeLength = pair

                if (distanceToCurrentNode + edgeLength) < bestSoFar[neighbor]:
                    # print("making relaxation offer from", currentNode, "to" ,neighbor)
                    # input()
                    bestSoFar[neighbor] = distanceToCurrentNode + edgeLength
                    heappush(unvisited, (bestSoFar[neighbor], neighbor))
            
            visited.add(currentNode)
        
        # print("unvisited:", unvisited)
        # print("visited:", visited)
        # for key,v in bestSoFar.items():
        #     print(key,"|",v)
        
        if max(bestSoFar.values()) == float('inf'):
            return -1
        else:
            return max(bestSoFar.values())
        
        
        


s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
ans = s.networkDelayTime(times, n, k)