

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# your logic here


def numStrokes(plankHeights, memo = None):
    if memo is None:
        memo = {}
    
    memoKey = tuple(plankHeights)
    if memoKey in memo:
        return memo[memoKey]
    if len(plankHeights) == 0 or len(plankHeights) == 1:
        return 1
    

    bestVertical = verticalStroke(plankHeights, memo)
    bestHorizontal = horizontalStroke(plankHeights, memo)
    ans = 1 + min(bestVertical, bestHorizontal)
    memo[memoKey] = ans
    return ans

def verticalStroke(plankHeights, memo):
    answers = []
    for i in range(0, len(plankHeights)):
        remaining = plankHeights[0:i] + plankHeights[i+1:]
        answers.append(numStrokes(remaining, memo))
    return min(answers)


def horizontalStroke(plankHeights, memo):
    newHeights = [h - 1 for h in plankHeights]
    remainingPlanks = list(filter(lambda x: x != 0, newHeights))
    if len(remainingPlanks) == 0:
        return 1
    return numStrokes(remainingPlanks, memo)


print(numStrokes(a))