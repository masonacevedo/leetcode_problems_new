from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cityCount = 0
        touchedBefore = set()
        n = len(isConnected)
        provinceCount = 0
        for i in range(0, n):
            # this will add to touchedBefore all the other cities
            # that i is connected to. 
            beforeBFS = len(touchedBefore)
            BFS(i, isConnected, touchedBefore)
            afterBFS = len(touchedBefore)
            if beforeBFS != afterBFS:
                provinceCount += 1
        return provinceCount
    

def BFS(startNode, isConnected, touchedBefore):
    queue = deque([])

    queue.append(startNode)
    currentNode = startNode
    while len(queue) > 0:
        touchedBefore.add(currentNode)
        neighbors = getNeighbors(currentNode, isConnected)
        # print("currentNode:", currentNode)
        # print("neighbors:", neighbors)
        # print("queue:", queue)
        # input()

        for neighbor in neighbors:
            if not(neighbor in touchedBefore):
                queue.append(neighbor)
        currentNode = queue.popleft()

def getNeighbors(startNode, isConnected):
    # print("startNode:", startNode)
    relevantRow = isConnected[startNode]
    ans = []
    for i in range(0, len(relevantRow)):
        if relevantRow[i] == 1 and i != startNode:
            ans.append(i)
    
    # print("ans:", ans)
    # input()
    return ans

mySol = Solution()
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
ans = mySol.findCircleNum(isConnected)
print(ans)