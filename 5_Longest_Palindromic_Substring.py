class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]
        DPTable = {}
        for i in range(0, len(s)):
            DPTable[(i,i)] = ((i, i), True)
            DPTable[(i+1,i)] = ((i+1, i), True)
        coords = (0,1)
        while coords is not None:
            i, j = coords[0], coords[1]
            DPKey = (i,j)
            cornerEntry = DPTable[(i+1, j-1)]
            cornerCoords, cornerIsPalindrome = cornerEntry
            if s[i] == s[j] and cornerIsPalindrome:
                DPTable[DPKey] = ((i, j+1,), True)
            else:
                aboveEntry = DPTable[(i+1, j)][0]
                rightEntry = DPTable[(i, j-1)][0]

                aboveEntryLength = aboveEntry[1] - aboveEntry[0]
                rightEntryLength = rightEntry[1] - rightEntry[0]

                if aboveEntryLength > rightEntryLength:
                    longer = aboveEntry
                else:
                    longer = rightEntry

                DPTable[DPKey] = (longer, False)
            coords = nextEntry(coords[0], coords[1], len(s))
        
        bestEntry, _ = DPTable[(0, len(s)-1)]
        ans = s[bestEntry[0]:bestEntry[1]]
        if len(ans) == 0:
            return s[0]
        else:
            return ans


def nextEntry(i,j, numRows):
    if j == numRows - 1 and i == 0:
        return None
    elif j == numRows - 1:
        diff = j - i
        return (0, diff+1)
    else:
        return (i+1, j+1)
        


sol = Solution()

s = "babad"
assert(sol.longestPalindrome(s) == "aba" or sol.longestPalindrome(s) == "bab")

s = "racecar"
assert(sol.longestPalindrome(s) == "racecar")

s = "cmmrracelnclsbtdmuxtfiyahrvxuwreyorosyqapfpnsntommsujibzwhgugwtvxsdsltiiyymiofbslwbwevmjrsbbssicnxptvwmsmiifypoujftxylpyvirfueagprfyyydxeiftathaygmolkcwoaavmdmjsuwoibtuqoewaexihispsshwnsurjopdwttlzyqdbkypvjsbuidsdnpgklhwfnqdvlffcysnxeywvwvblatmxbflnuykhfhjptenhcxqinomlwalvlezefqybpuepbnymzlruuirpiatqgjgcnfmrlzshauoxuoqopcikogfwpssjdeplytcapmujyvgtfmmolnuadpwblgmcaututcrwsqrlpaaqobjfnhudmsulztbdkxpfejavastxejtpbqfftdtcdhvtpbzfuqcwkxtldtjycreimiujtxudtmokcoebhodbkgkgxjzrgyuqhozqtidltodlkziyofdeszwiobkwesdijxbbagguxvofvtphqxgvidqfkljufgubjmjllxoanbizwtedykwmneaosopynzlzvrlqcmyaahdcagfatlhwtgqxsyxwjhexfiplwtrtydjzrsysrcwszlntwrpgfedhgjzhztffqnjotlfudvczwfkhuwmdzcqgrmfttwaxocohtuscdxwfvhcymjpkqexusdaccw"
print(sol.longestPalindrome(s))

s = "abcda"
assert(len(sol.longestPalindrome(s)) == 1)

s = "aaaa"
print(sol.longestPalindrome(s))

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"