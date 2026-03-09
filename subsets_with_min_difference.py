from typing import List

def subsetsWithMinDifference(L: List[int]) -> List[List[int]]:

    # given a list of numbers, this returns 
    # two subsets of those numbers such that 
    # they have the minimum possible difference.
    if len(L) == 0:
        return [[],[]]
    
    item = L[0]
    recursiveCall = subsetsWithMinDifference(L[1:])
    leftPile, rightPile = recursiveCall

    leftPileTotal = sum(leftPile)
    rightPileTotal = sum(rightPile)

    addToLeft = abs((leftPileTotal+item) - rightPileTotal)
    addToRight = abs(leftPileTotal - (rightPileTotal + item))
    if addToLeft < addToRight:
        return [leftPile + [item], rightPile]
    else:
        return [leftPile, rightPile + [item]]

arr = [20, 25, 27, 18, 10, 100,99]

ans = subsetsWithMinDifference(arr)

print("ans:", ans)
leftPile, rightPile = ans
print("sum(left):", sum(leftPile))
print("sum(right):", sum(rightPile))