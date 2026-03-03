from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        bestPossible = max(max(citations), len(citations))
        worstPossible = 0

        # print("citations:", citations)
        # print("bestPossible:", bestPossible)
        # print("worstPossible:", worstPossible)

        guess = (bestPossible + worstPossible)//2

        hComputations = {}
        # print("0:", satisfiesHCriteria(citations, 0, hComputations))
        # print("1:", satisfiesHCriteria(citations, 1, hComputations))
        
        while satisfiesHCriteria(citations, guess, hComputations) == satisfiesHCriteria(citations, guess+1, hComputations):
            if bestPossible == (worstPossible+1):
                return guess+1
            # print("bestPossible:", bestPossible)
            # print("worstPossible:", worstPossible)
            # print("guess:", guess)
            # print("hComputations:", hComputations)
            # input()
            if satisfiesHCriteria(citations, guess, hComputations):
                worstPossible = guess
            else:
                bestPossible = guess
            guess = (bestPossible + worstPossible)//2
        
        return guess
    
def satisfiesHCriteria(nums, h, comps):
    if h in comps:
        return comps[h]
    count = sum(True if num >= h else 0 for num in nums)
    ans = (count >= h)
    comps[h] = ans
    return ans

mySol = Solution()
citations = [1,3,1]
ans = mySol.hIndex(citations)
assert(ans == 1)

citations = [0]
ans = mySol.hIndex(citations)
assert(ans == 0)

citations = [11, 15]
ans = mySol.hIndex(citations)
assert(ans == 2)

citations = [11]*11
ans = mySol.hIndex(citations)
print("ans:", ans)