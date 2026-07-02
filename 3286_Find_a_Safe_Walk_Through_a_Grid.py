from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        if grid[0][0] == 0:
            start = ([0,0], health)
        else:
            start = ([0,0], health-1)

        queue = deque([start])
        seenBefore = set()
        while len(queue) > 0:
            coords, h = queue.popleft()

            if tuple(coords + [h]) in seenBefore:
                continue

            if coords == [len(grid)-1, len(grid[0])-1] and h >= 1:
                return True

            if h >= 0:
                for neighbor in getNeighbors(coords, grid):

                    nRow, nCol = neighbor
                    if grid[nRow][nCol] == 1:
                        queue.append((neighbor, h-1))
                    else:
                        queue.append((neighbor, h))

            seenBefore.add(tuple(coords + [h]))
        
        return False

def getNeighbors(coords, grid):
    row, col = coords
    topNeighbor = [row-1, col]
    botNeighbor = [row+1, col]
    leftNeighbor = [row, col-1]
    rightNeighbor = [row, col+1]

    neighbors = []
    if row > 0:
        neighbors.append(topNeighbor)

    if col > 0:
        neighbors.append(leftNeighbor)

    if row < len(grid)-1:
        neighbors.append(botNeighbor)

    if col < len(grid[0]) - 1:
        neighbors.append(rightNeighbor)

    return neighbors



        
        


s = Solution()

grid = [[1,1,1,1]]

health = 4

ans = s.findSafeWalk(grid, health)
print("ans:", ans)