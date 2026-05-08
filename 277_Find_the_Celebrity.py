# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return (a,b) in edge_set

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(0, n):
            # print("checking if", i, "is a celebrity")
            if isCelebrity(i, n):
                return i
            print()
        return -1

def isCelebrity(i, n):
    for j in range(0, n):
        if j == i:
            continue
        # if i knows somebody, they're not a celebrity
        if knows(i, j):
            # print("i:", i)
            # print("j:", j)
            # print("not a celebrity! someone knows i")
            return False
        
        # if someone doesn't know i, they're not a celebrity
        if not(knows(j, i)):
            # print("j:", j)
            # print("i:", i)
            # print("not a celebrity! someone doesn't know them!")
            return False
    return True

edge_set = [
    (2,0),
    (2,1),
    (0,1)
]

s = Solution()

ans = s.findCelebrity(3)
print("ans:", ans)