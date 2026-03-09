from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeHelper(coins, amount, {})

    def coinChangeHelper(self, coins: List[int], amount: int, memo) -> int:
        if amount in memo:
            return memo[amount]

        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        
        
        # candidates = []
        bestSoFar = float('inf')
        for coin in coins:
            amountToMake = amount - coin
            recursiveCall = self.coinChangeHelper(coins, amountToMake, memo)
            if recursiveCall == -1:
                pass
            else:
                bestSoFar = min(bestSoFar, 1 + recursiveCall)
        
        # print("amount:", amount)
        # print("candidates:", candidates)
        # input()
        if bestSoFar == float('inf'):
            memo[amount] = -1
            return -1
        memo[amount] = bestSoFar
        return bestSoFar

coins = [1,2, 5]
amount = 100

s = Solution()
ans = s.coinChange(coins, amount)
print("ans:", ans)