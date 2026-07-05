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
        
        
        bestKnown = {node: float('inf') for node in adjList.keys()}
        bestKnown[source] = 0

        seenBefore = set()

        queue = deque([])

        while len(seenBefore) < n:
            curent = queue.popleft()
            breakpoint()
            seenBefore.add(current)

        # breakpoint()


s = Solution()

n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]

s.minScore(n, roads)