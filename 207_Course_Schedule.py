from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(0, numCourses)}

        for edge in prerequisites:
            before, after = edge
            adjList[before].append(after)
        
        inDegrees = {i:0 for i in range(0, numCourses)}

        for node, neighbors in adjList.items():
            for neighbor in neighbors:
                inDegrees[neighbor] += 1
        
        
        if topOrder(inDegrees, adjList):
            return True
        else:
            return False
        
    
def topOrder(inDegrees, adjList):
    
    queue = deque([])
    for node, inDegree in inDegrees.items():
        if inDegree == 0:
            queue.append(node)
    
    if len(queue) == 0:
        return None
    

    result = []
    processed = 0
    while len(queue) > 0:
        currentNode = queue.popleft()
        result.append(currentNode)
        for neighbor in adjList[currentNode]:
            inDegrees[neighbor] -= 1
            if inDegrees[neighbor] == 0:
                queue.append(neighbor)
        processed += 1

    if processed != len(adjList):
        return None
    else:
        return result
    

        

s = Solution()

numCourses = 6
prerequisites = [[0,1],[1,2],[2,5], [1,4], [0,3], [3,4], [4,5]]

ans = s.canFinish(numCourses, prerequisites)
print("ans:", ans)