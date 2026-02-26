class Solution:
    def reverseBits(self, n: int) -> int:
        nBinStringRaw = bin(n)[2:]
        paddednBinString = (32 - len(nBinStringRaw))*"0" + nBinStringRaw
        reversedBinString = "".join(list(reversed(paddednBinString)))
        return int(reversedBinString, 2)

n = 43261596
mySol = Solution()
ans = mySol.reverseBits(n)
print("ans:", ans)