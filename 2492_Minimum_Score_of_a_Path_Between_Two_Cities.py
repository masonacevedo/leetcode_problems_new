from collections import deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adjList = {}

        for i in range(1, n+1):
            adjList[i] = []


        for road in roads:
            source, dest, distance = road
            adjList[source].append((dest, distance))
            adjList[dest].append((source, distance))

        queue = deque([1])
        seenBefore = set()

        allDistances = []
        while len(queue) > 0:
            current = queue.popleft()

            for neighbor, d in adjList[current]:
                allDistances.append(d)
                if neighbor not in seenBefore:
                    queue.append(neighbor)

            seenBefore.add(current)

        return min(allDistances)


s = Solution()

n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]

s.minScore(n, roads)