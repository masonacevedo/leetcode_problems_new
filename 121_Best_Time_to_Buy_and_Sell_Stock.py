from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        bestSoFar = 0
        buyPrice = prices[0]
        while i < len(prices):
            currentPrice = prices[i]
            # print("i:", i)
            # print("currentPrice:", currentPrice)
            # print("buyPrice:", buyPrice)
            # print()
            if currentPrice < buyPrice:
                buyPrice = currentPrice
            else:
                bestSoFar = max(bestSoFar, currentPrice - buyPrice)
            i += 1
        
        return bestSoFar

mySol = Solution()
prices = [7,6,4,3,1]
ans = mySol.maxProfit(prices)
# print("ans:", ans)