from enum import Enum

from typing import List

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        seenBefore = set()
        row = 0
        col = 0
        direction = Direction.RIGHT
        ans = []
        while len(seenBefore) < len(matrix) * len(matrix[0]):
            # print("ans:", ans)
            # print("row:", row)
            # print("col:", col)
            # print("direction:", direction)
            # print()
            entry = matrix[row][col]
            ans.append(entry)
            seenBefore.add((row, col))
            row, col, direction = nextCoords(row, col, direction, seenBefore, len(matrix), len(matrix[0]))
            # print("row:", row)
            # print("col:", col)
            # print("direction:", direction)
            # input()

        return ans

def nextCoords(row, col, direction, seenBefore, numRows, numCols):
    if direction == Direction.UP:
        if row == 0 or (row-1, col) in seenBefore:
            return (row, col+1, Direction.RIGHT)
        else:
            return (row-1, col, Direction.UP)
    elif direction == Direction.RIGHT:
        if col == (numCols-1) or (row, col+1) in seenBefore:
            return (row+1, col, Direction.DOWN)
        else:
            return (row, col+1, Direction.RIGHT)
    elif direction == Direction.DOWN:
        if row == (numRows-1) or (row+1, col) in seenBefore:
            return (row, col-1, Direction.LEFT)
        else:
            return (row+1, col, Direction.DOWN)
    elif direction == Direction.LEFT:
        if col == 0 or (row, col-1) in seenBefore:
            return (row-1, col, Direction.UP)
        else:
            return (row, col-1, Direction.LEFT)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
    ]

s = Solution()
ans = s.spiralOrder(matrix)
# print("ans:", ans)