from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
    
        allPossibilities = enumeratePossibilities(s)
        validAddresses = []
        for possibleAddress in allPossibilities:
            if validAddress(possibleAddress):
                validAddresses.append(possibleAddress)
        return validAddresses

def validAddress(possibleAddress):
    numsAsStrings = possibleAddress.split(".")
    numsAsInts = [int(s) for s in numsAsStrings]
    for index in range(0, len(numsAsStrings)):
        numStr = numsAsStrings[index]
        numInt = numsAsInts[index]
        if not(0 <= numInt and numInt <= 255) or len(numStr) != len(str(numInt)):
            return False
        
    return True

def enumeratePossibilities(s):

    n = len(s)
    possibleStrings = []
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                newString = s[0:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:]
                possibleStrings.append(newString)
    
    return possibleStrings
    
s = "101023"

mySol = Solution()
ans = mySol.restoreIpAddresses(s)

print("ans:", ans)