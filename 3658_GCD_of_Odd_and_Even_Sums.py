class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        N = 2*n
        total = (N*(N+1))//2

        sumOfOdds = int((total/2) - (n/2))
        sumOfEvens = int((total/2) + (n/2))
        
        return gcd(sumOfEvens, sumOfOdds)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

s = Solution()

ans = s.gcdOfOddEvenSums(5)
print("ans:", ans)