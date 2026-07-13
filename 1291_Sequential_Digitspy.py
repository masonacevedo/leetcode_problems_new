from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        minDigits = len(str(low))
        maxDigits = len(str(high))

        allDigits = []
        for length in range(minDigits, maxDigits+1):
            allDigits += sequentialDigits_N(length)
        
        allNums = [int(s) for s in allDigits]

        return list(filter(lambda n: low <= n and n <= high, allNums))




        


def sequentialDigits_N(n):
    # returns numbers with n digits that have sequential digits
    ans = []
    for i in range(1, 10-n+1):
        num = ""
        for digit in range(i, i+n):
            num += str(digit)
        ans.append(num)
    
    return ans


s = Solution()

ans = s.sequentialDigits(1000, 13000)

print("ans:", ans)