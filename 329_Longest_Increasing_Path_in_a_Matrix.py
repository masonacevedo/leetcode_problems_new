from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        bestSoFar = -1
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                longestPathFromHere = longestPathMemoized(matrix, row, col, memo)
                bestSoFar = max(bestSoFar, longestPathFromHere)

        return bestSoFar

def longestPathMemoized(matrix, row, col, memo):
    
    key = (row, col)
    if key in memo:
        return memo[key]
    
    # first, check for neighbors. 
    # if there are no neighbors, then the longest path from here is 0.
    # if there are neighbors, the longest path from here is 1 + the longest path from each neighbor.

    neighbors = calcNeighbors(matrix, row, col)
    
    if len(neighbors) == 0:
        memo[key] = 1
        return 1
    
    bestSoFar = 0
    for neighbor in neighbors:
        neighborRow, neighborCol = neighbor
        longestPath = longestPathMemoized(matrix, neighborRow, neighborCol, memo)
        bestSoFar = max(longestPath, bestSoFar)
    
    memo[key] = 1 + bestSoFar
    return 1 + bestSoFar



def calcNeighbors(matrix, row, col):
    
    currentEntry = matrix[row][col]
    potentialNeighbors = []

    leftNeighbor =   (row, col-1)
    rightNeighbor =  (row, col+1)

    topNeighbor =    (row-1, col)
    bottomNeighbor = (row+1, col)

    if row != 0:
        neighborRow, neighborCol = topNeighbor
        neighborEntry = matrix[neighborRow][neighborCol]
        if neighborEntry > currentEntry:
            potentialNeighbors.append(topNeighbor)
    
    if col != 0:
        neighborRow, neighborCol = leftNeighbor
        neighborEntry = matrix[neighborRow][neighborCol]
        if neighborEntry > currentEntry:
            potentialNeighbors.append(leftNeighbor)
    
    
    if row != len(matrix) - 1:
        neighborRow, neighborCol = bottomNeighbor
        neighborEntry = matrix[neighborRow][neighborCol]
        if neighborEntry > currentEntry:
            potentialNeighbors.append(bottomNeighbor)
    
    
    if col != len(matrix[0]) - 1:
        neighborRow, neighborCol = rightNeighbor
        neighborEntry = matrix[neighborRow][neighborCol]
        if neighborEntry > currentEntry:
            potentialNeighbors.append(rightNeighbor)
    
    
    return potentialNeighbors


    # if row == 0:
        



s = Solution()

matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]

ans = s.longestIncreasingPath(matrix)
print("ans:", ans)