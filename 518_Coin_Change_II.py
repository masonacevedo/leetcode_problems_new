from typing import List
import copy

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        return self.changeHelper(amount, sorted(coins))
    
    # DP SOLUTION:
    # columns indexed by what coins are used,
    # rows indexed by amount.
    # i.e.
    # [waysToMake 37 with 1st coin, waysToMake 37 with 2nd coin, waysToMake 37 with 3rd coin... waysToMake 37 with all coins, ]
    # [waysToMake 38 with 1st coin, waysToMake 38 with 2nd coin, waysToMake 38 with 3rd coin... waysToMake 38 with all coins, ]
    # we build this solution by going down through an entire column first (the 1st column, with only one coin)
    # then go from there. 
    def changeHelper(self, amount: int, coins: List[int]) -> int:
        DP = [[None for _ in range(0, len(coins))] for _ in range(0, amount+1)]
        for col in range(0, len(coins)):
            for row in range(0, amount+1):
                ans = calculateNumWays(row, col, row, coins, DP)
                DP[row][col] = ans
            # prettyPrint(DP)
            # print()
            # input()

        
        return DP[amount][-1]


def calculateNumWays(amount, col, row, coins, DP):
    if row == 0:
        return 1
    elif col == 0:
        coinToUse = coins[0]
        if (amount % coinToUse) == 0:
            return 1
        else:
            return 0
    
    ans = 0
    coinToUse = coins[col]

    maxTimesTouse = amount//coinToUse

    for i in range(0, maxTimesTouse+1):
        amountToMake = amount - (coinToUse * i)
        if amountToMake < 0:
            pass
        else:
            # print("amountToMake:", amountToMake)
            # print("col-1:", col-1)
            # prettyPrint(DP)
            # input()

            ans += DP[amountToMake][col-1]

    return ans



def prettyPrint(rows):
    for row in rows:
        ans = "["
        for entry in row:
            ans += str(entry) + ", "
        ans += "]"
        print(ans)

s = Solution()

amount = 500
coins = [3,5,7,8,9,10,11]
# amount = 4
# coins = [1, 2, 3]
# 10, [1,2] -> answer should be 6
# 12 [1,2] -> answer should be 7
# 4, 1, 2, 3 => answer should be: 1 + 1 + 1 + 1 = 4

ans = s.change(amount, coins)
print("ans:", ans)