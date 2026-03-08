from typing import List
import copy

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        return self.changeHelper(amount, sorted(coins), {})
    
    def changeHelper(self, amount: int, coins: List[int], memo) -> int:

        if len(coins) == 0:
            return -1
        
        k = (amount, tuple(coins))
        if k in memo:
            return memo[k]

        minCoin = coins[0]
        if amount < minCoin:
            return -1
        elif amount == minCoin:
            return 1
        
        maxTimesUsed = amount//minCoin

        ans = 0
        for i in range(0, maxTimesUsed+1):
            remainingAmount = amount - (minCoin*i)
            
            if remainingAmount == 0:
                ans += 1
            else:
                recursiveCall = self.changeHelper(remainingAmount, coins[1:], memo)
                if recursiveCall != -1:
                    ans += recursiveCall
            
        memo[k] = ans
        return ans



s = Solution()

amount = 500
coins = [3,5,7,8,9,10,11]

ans = s.change(amount, coins)
print("ans:", ans)