class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        allStrings = binaryStrings(k)
        foundStrings = set()
        for i in range(0, len(s)-k+1):
            foundStrings.add(s[i:i+k])
            # print("s[i:i+k]:", s[i:i+k])

        return len(foundStrings) == len(allStrings)


def binaryStrings(k):
    ans = set()
    final_length = len(bin(2**k-1)[2:])

    for i in range(0, (2**k)):
        s = bin(i)[2:]
        s = "0"*(final_length-len(s)) + s
        ans.add(s)
    
    return ans


mySol = Solution()
assert(mySol.hasAllCodes("00110110", 2))
assert(mySol.hasAllCodes("0110", 1))
assert(not(mySol.hasAllCodes("0110", 2)))
