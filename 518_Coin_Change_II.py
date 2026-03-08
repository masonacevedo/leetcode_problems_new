from typing import List
import copy

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        return self.changeHelper(amount, sorted(coins))
    
    def changeHelper(self, amount: int, coins: List[int]) -> int:
        # print("amount:", amount)
        # print("coins:", coins)
        # print()

        if len(coins) == 0:
            return -1
        
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
                recursiveCall = self.changeHelper(remainingAmount, coins[1:])
                # print("amount:", amount)
                # print("minCoin:", minCoin)
                # print("remainingAmount:", remainingAmount)
                # print("coins:", coins)
                # print("i:", i)
                # print("recursiveCall:", recursiveCall)
                # print()
                if recursiveCall != -1:
                    ans += recursiveCall
            

        return ans



s = Solution()

amount = 10
coins = [10]

ans = s.change(amount, coins)
print("ans:", ans)