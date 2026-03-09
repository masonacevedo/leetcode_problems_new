from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeHelper(coins, amount)

    def coinChangeHelper(self, coins: List[int], amount) -> int:
        DP = [0]

        # In this DP table, we'll want entry i to be the amount of coins
        # needed to make i amount of money! 

        for i in range(1, amount+1):
            ans = minCoinsNeeded(coins, i, DP)
            DP.append(ans)
            

        return DP[-1]

def minCoinsNeeded(coins, amount, DP):
    if amount == 0:
        return 0
    bestSoFar = float('inf')
    for coin in coins:
        amountToMake = amount - coin
        if amountToMake >= 0:
            DPValue = DP[amountToMake]
            if DPValue != -1:
                bestSoFar = min(bestSoFar, 1 + DPValue)

    if bestSoFar == float('inf'):
        return -1
    
    return bestSoFar

coins = [1, 2, 5, 99]
amount = 100

s = Solution()
ans = s.coinChange(coins, amount)
print("ans:", ans)