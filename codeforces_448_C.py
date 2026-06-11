numPlanks = 5
plankHeights = [2, 2, 1, 2, 1]

def numStrokes(plankHeights):
    if len(plankHeights) == 0:
        return 1
    bestVertical = verticalStroke(plankHeights)
    bestHorizontal = horizontalStroke(plankHeights)
    return 1 + min(bestVertical, bestHorizontal)

def verticalStroke(plankHeights):
    answers = []
    for i in range(0, len(plankHeights)):
        remaining = plankHeights[0:i] + plankHeights[i+1:]
        answers.append(numStrokes(remaining))
    return min(answers)


def horizontalStroke(plankHeights):
    newHeights = [h - 1 for h in plankHeights]
    remainingPlanks = list(filter(lambda x: x != 0, newHeights))
    if len(remainingPlanks) == 0:
        return 1
    return numStrokes(remainingPlanks)


ans = numStrokes(plankHeights)
print("ans:", ans)