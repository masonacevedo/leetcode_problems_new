from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        memo = {}

        return maxPathHelper(grid, k, 0, 0, 0, 0, memo)



def maxPathHelper(grid, k, row, col, currentScore, currentCost, memo):
    # print("row:", row)
    # print("col:", col)
    # print()

    
    currentTile = grid[row][col]
    if currentTile == 0:
        newScore = currentScore
        newCost = currentCost
    elif currentTile == 1:
        newScore = currentScore + 1
        newCost = currentCost + 1
    elif currentTile == 2:
        newScore = currentScore + 2
        newCost = currentCost + 1
    
    if (row == len(grid)-1) and (col == len(grid[0])-1):
        if newCost > k:
            return -1
        return newScore

    if newCost > k:
        return -1

    if col < len(grid[0])-1:
        moveRight = maxPathHelper(grid, k, row, col+1, newScore, newCost, memo)
    else:
        moveRight = -1
    
    if row < len(grid)-1:
        moveDown = maxPathHelper(grid, k, row+1, col, newScore, newCost, memo)
    else:
        moveDown = -1
    
    # print('moveDown:', moveDown)
    # print('moveRight:', moveRight)
    # input("enter to con")
    return max(moveDown, moveRight)

grid = [
    [0, 1],
    [1, 2]
]
k = 1
s = Solution()

ans = s.maxPathScore(grid, k)
print("ans:", ans)