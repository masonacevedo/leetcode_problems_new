
import random
class Solution:
    def getSum(a,b):
        if a == 0:
            return b
        elif b == 0:
            return a
        elif a == -1*b:
            return 0
        elif a > 0 and b > 0:
            return self.add(a,b)
        
        elif a < 0 and b < 0:
            return -1*self.add(-1*a, -1*b)
        
        else:
            if abs(a) > abs(b):
                bigger, smaller = a, b
            else:
                bigger, smaller = b, a
            
            res = self.subtract(bigger,smaller)

            if a > 0:
                pos, neg = a, b
            else:
                pos, neg - b, a

            if bigger == pos:
                return res
            else:
                return -1*res
    



        
        

        
        

    def add(self, a: int, b: int) -> int:

        if a > b:
            bigger, smaller = a, b
        else:
            bigger, smaller = b, a
        
        bigString = bin(bigger)[2:]
        smallString = bin(smaller)[2:]

        leadingZeros = "0" * (len(bigString) - len(smallString))
        smallString = leadingZeros + smallString
        

        carryOne = False
        i = len(bigString) - 1
        # print("bigString:  ", bigString)
        # print("smallString:", smallString)
        ans = ""
        while i >= 0:
            # print("i:", i)

            d1 = bigString[i]
            d2 = smallString[i]
            # print("d1:", d1)
            # print("d2:", d2)
            # print('carryOne:', carryOne)
            # print()
            
            digits = [d1, d2]
            numOnes = digits.count("1")

            if carryOne:
                numOnes += 1

            if numOnes == 0:
                ans += "0"
                carryOne = False
            elif numOnes == 1:
                ans += "1"
                carryOne = False
            elif numOnes == 2:
                ans += "0"
                carryOne = True
            elif numOnes == 3:
                ans += "1"
                carryOne = True
            
            i -= 1

        if carryOne:
            ans += "1"
        
        finalBinString = "".join(list(reversed(ans)))
        return int(finalBinString, 2)

s = Solution()
ans = s.getSum(17, 38)

for _ in range(0, 1000):
    a = random.randint(1, 99999)
    b = random.randint(1, 99999)
    assert(a + b == s.getSum(a,b))

# print("ans:", ans)
        