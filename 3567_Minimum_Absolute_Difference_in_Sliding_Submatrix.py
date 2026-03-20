from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        answers = [[] for _ in range(0, m-k+1)]
        for i in range(0, m - k+1):
            for j in range(0, n - k+1):
                subMatrixVals = getSubMatrixVals(grid, i, j, k)
                minDifference = calculateMinimumDifference(subMatrixVals)
                answers[i].append(minDifference)
        
        return answers

def getSubMatrixVals(grid, i, j, k):
    vals = []
    for row in range(i, i+k):
        for col in range(j, j+k):
            vals.append(grid[row][col])
    return vals

def calculateMinimumDifference(vals):
    
    sortedVals = sorted(vals)
    if max(sortedVals) == min(sortedVals):
        return 0
    bestSoFar = float('inf')
    for val1, val2 in zip(sortedVals[0:-1], sortedVals[1:]):
        if val1 != val2:
            bestSoFar = min(bestSoFar, abs(val2-val1))
    return bestSoFar

s = Solution()
grid = [[3,5,1,2,3],
        [1,5,2,3,3],
        [2,5,5,1,3],
        [1,5,1,5,4],
        [1,2,3,4,1]]
k = 3
ans = s.minAbsDiff(grid, k)
print("ans:", ans)