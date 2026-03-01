from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        increasing = prices[1] >= prices[0]
        if increasing:
            profit -= prices[0]
        
        for i, currentPrice in enumerate(prices[0:-1]):
            nextPrice = prices[i+1]
            if increasing and nextPrice > currentPrice:
                pass
            elif increasing and currentPrice > nextPrice:
                # print("selling at:", currentPrice)
                # sell stock! 
                profit += currentPrice
                increasing = False
            elif increasing and currentPrice == nextPrice:
                pass
            elif not(increasing) and nextPrice > currentPrice:
                # print("buying at:", currentPrice)
                # buy stock! 
                profit -= currentPrice
                increasing = True
            elif not(increasing) and currentPrice > nextPrice:
                pass
            elif not(increasing) and currentPrice == nextPrice:
                pass
        
        if increasing:
            profit += prices[-1]

        return profit

mySol = Solution()
prices = [1,2,3,4,5]
ans = mySol.maxProfit(prices)
print("ans:", ans)