from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rowSums = generateRowSums(grid)
        colSums = generateColSums(grid)

        numRows = len(grid)
        numCols = len(grid[0])

        topHalf = 0
        bottomHalf = sum(rowSums)
        for rowSum in rowSums:
            topHalf += rowSum
            bottomHalf -= rowSum
            if topHalf == bottomHalf:
                return True
        
        leftHalf = 0
        rightHalf = sum(colSums)
        for colSum in colSums:
            leftHalf += colSum
            rightHalf -= colSum
            if leftHalf == rightHalf:
                return True


        return False


def generateRowSums(grid):
    numRows = len(grid)
    numCols = len(grid[0])
    rowSums = []
    for row in range(0, numRows):
        currentRowTotal = 0
        for col in range(0, numCols):
            num = grid[row][col]
            currentRowTotal += num
        rowSums.append(currentRowTotal)
    return rowSums



def generateColSums(grid):
    numRows = len(grid)
    numCols = len(grid[0])
    colSums = []
    for col in range(0, numCols):
        currentColTotal = 0
        for row in range(0, numRows):
            num = grid[row][col]
            currentColTotal += num
        colSums.append(currentColTotal)
    return colSums

grid = [[1,4],
        [2,3],
        [2,3],
        [4,1]]

rowSums = generateRowSums(grid)
colSums = generateColSums(grid)

print("rowSums:", rowSums)
# print("colSums:", colSums)

s = Solution()
ans = s.canPartitionGrid(grid)
print("ans:", ans)