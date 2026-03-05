import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        s = sum(self.w)
        wAdjusted = [e/s for e in self.w]
        self.cumProbs = []
        total = 0
        for num in wAdjusted:
            total += num
            self.cumProbs.append(total)




    def pickIndex(self) -> int:
        res = random.random()
        for i, cumProb in enumerate(self.cumProbs):
            if res < cumProb:
                return i

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

s = Solution([1,10])
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
