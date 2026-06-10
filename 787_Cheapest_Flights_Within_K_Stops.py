from typing import List
import copy

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        bestSoFar = {i: float('inf') for i in range(0, n)}
        bestSoFar[src] = 0
        for i in range(0, k+1):
            snapshot = copy.copy(bestSoFar)
            
            for edge in flights:
                source, dest, price = edge
                if snapshot[source] + price < bestSoFar[dest]:
                    bestSoFar[dest] = snapshot[source] + price
        
        if bestSoFar[dst] == float('inf'):
            return -1
        return bestSoFar[dst]

s = Solution()

# n = 4
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# src = 0
# dst = 3
# k = 2

# n = 5
# flights = [
#     [0, 1, 999],
#     [0, 1, 10],
#     [1, 2, 10],
#     [0, 3, 1],
#     [0, 4, 5],
#     [3, 4, 1],
#     [4, 2, 1],
# ]
# src = 0
# dst = 2
# k = 1

# n=3
# flights = [
#     [0,1,100],
#     [1,2,100],
#     [0,2,500]
# ]
# src=0
# dst=2
# k=0

n = 5
src = 2
dst = 0
k = 2
flights = [
    [1,0,5],
    [2,1,5],
    [3,0,2],
    [1,3,2],
    [4,1,1],
    [2,4,1]
]

ans = s.findCheapestPrice(n, flights, src, dst, k)
print("ans:", ans)