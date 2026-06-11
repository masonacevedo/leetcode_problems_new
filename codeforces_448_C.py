

import sys
input = sys.stdin.readline
import pdb
import copy

def pause():
    p = pdb.Pdb(stdin=open('/dev/tty'), stdout=open('/dev/tty', 'w'))
    p.set_trace(sys._getframe(1))

n = int(input())
a = list(map(int, input().split()))



def numStrokes(plankHeights, memo = None):
    pause()
    if memo is None:
        memo = {}
    if max(plankHeights) == 0:
        return 0
    memoKey = tuple(plankHeights)
    if memoKey in memo:
        return memo[memoKey]
    if len(plankHeights) == 0 or len(plankHeights) == 1:
        return 1
    

    bestVertical = verticalStroke(plankHeights, memo)
    bestHorizontal = horizontalStroke(plankHeights, memo)
    ans = min(bestVertical, bestHorizontal)
    memo[memoKey] = ans
    return ans

def verticalStroke(plankHeights, memo):
    answers = []
    for i in range(0, len(plankHeights)):
        remaining = plankHeights[0:i] + plankHeights[i+1:]
        answers.append(1 + numStrokes(remaining, memo))
    return min(answers)


def horizontalStroke(plankHeights, memo):
    blocks = computeBlocks(plankHeights)
    answers = []
    for block in blocks:
        newPlankHeights, strokesPainted = paintBlocks(plankHeights, block)
        answers.append(strokesPainted + numStrokes(newPlankHeights, memo))
    return min(answers)

def paintBlocks(plankHeights, block):
    blockHeights = [plankHeights[i] for i in block]
    newBlockHeights = [h - min(blockHeights) for h in blockHeights]
    newPlankHeights = []
    blockIndex = 0
    for i, p in enumerate(plankHeights):
        if i in block:
            newPlankHeights.append(newBlockHeights[blockIndex])
            blockIndex += 1
        else:
            newPlankHeights.append(plankHeights[i])
    return newPlankHeights, min(blockHeights)


def computeBlocks(plankHeights):
    ans = []
    current = []
    for i, h in enumerate(plankHeights):
        if h == 0:
            if current != []:
                ans.append(current)
                current = []
        else:
            current.append(i)
    if current != []:
        ans.append(current)

    return ans


print(numStrokes(a))