class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(s) == len(t) and mapExists(s,t) and mapExists(t,s)

def mapExists(s,t):
    m = {}
    for sChar, tChar in zip(s,t):
        if sChar in m:
            if m[sChar] != tChar:
                return False
        else:
            m[sChar] = tChar
    return True
