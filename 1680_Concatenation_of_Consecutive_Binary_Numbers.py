class Solution:
    def concatenatedBinary(self, n: int) -> int:
        concatString = "".join([bin(i)[2:] for i in range(1, n+1)])
        num = int(concatString, 2)
        return num % ((10**9)+7)

mySol = Solution()
ans = mySol.concatenatedBinary(99999)
print("ans:", ans)