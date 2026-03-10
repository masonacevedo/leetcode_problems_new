from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))

        events.sort()

        result = [[0, 0]]
        heap = [(0, float('inf'))]

        for x, neg_h, r in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_h:
                heapq.heappush(heap, (neg_h, r))

            max_h = -heap[0][0]
            if result[-1][1] != max_h:
                result.append([x, max_h])

        return result[1:]


mySol = Solution()

print(mySol.getSkyline(buildings=[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print(mySol.getSkyline(buildings=[[0,2,3],[2,5,3]]))
