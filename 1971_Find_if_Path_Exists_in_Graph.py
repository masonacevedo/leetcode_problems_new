from collections import deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = {}

        for e in edges:
            u,v = e
            if u in adjList:
                adjList[u].append(v)
            else:
                adjList[u] = [v]
            
            if v in adjList:
                adjList[v].append(u)
            else:
                adjList[v] = [u]
            
        queue = deque([source])
        seenBefore = set()
        while len(queue) > 0:
            currentVertex = queue.popleft()
            if currentVertex == destination:
                return True
            neighbors = adjList[currentVertex]

            for neighbor in neighbors:
                if not(neighbor in seenBefore):
                    queue.append(neighbor)

            seenBefore.add(currentVertex)



            pass
        return False

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

s = Solution()
ans = s.validPath(n, edges, source, destination)
print("ans:", ans)