from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if not(uniqueEntries(row)):
                return False
        
        for row in range(0, len(board)):
            col = [board[i][row] for i in range(0, 9)]
            # print("col:", col)
            # input()
            if not(uniqueEntries(col)):
                return False
        
        if not(uniqueSquare(0,0,board)):
            return False
        
        if not(uniqueSquare(3,0,board)):
            return False

        if not(uniqueSquare(6,0,board)):
            return False

        if not(uniqueSquare(0,3,board)):
            return False
        
        if not(uniqueSquare(3,3,board)):
            return False

        if not(uniqueSquare(6,3,board)):
            return False

        
        if not(uniqueSquare(0,6,board)):
            return False
        
        if not(uniqueSquare(3,6,board)):
            return False

        if not(uniqueSquare(6,6,board)):
            return False

        
        return True
    
def uniqueSquare(row, col, board):
    # print("unique square")
    # print("row:", row)
    # print("col:", col)
    seen = set()
    for rowIndex in range(row, row+3):
        for colIndex in range(col, col+3):
            entry = board[rowIndex][colIndex]
            # print("entry:", entry)
            # print("seen:", seen)
            # input()
            if entry in seen and entry != ".":
                return False
            seen.add(entry)
    
    return True

def uniqueEntries(nums):
    seen = set()
    for num in nums:
        if num in seen and num != ".":
            return False
        seen.add(num)
    return True

board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
for row in board:
    print(row)

mySol = Solution()
mySol.isValidSudoku(board)
