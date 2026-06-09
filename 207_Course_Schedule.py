from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(0, numCourses)}

        for edge in prerequisites:
            before, after = edge
            adjList[before].append(after)
        
        unvisited = set(range(0, numCourses))
        while len(unvisited) > 0:
            currentNode = next(iter(unvisited))
            result = hasCycle(currentNode, adjList, unvisited, currentPath = set())
            if result:
                return False

        return True
    
def hasCycle(currentNode, adjList, unvisited, currentPath):
    if currentNode in currentPath:
        return True
    
    # if the current node has been visited before, 
    # we haven't found a cycle yet, so we're done.
    if currentNode not in unvisited:
        return False
    
    currentPath.add(currentNode)

    for neighbor in adjList[currentNode]:
        result = hasCycle(neighbor, adjList, unvisited, currentPath)
        if result:
            return True
    
    currentPath.remove(currentNode)
    unvisited.remove(currentNode)
    return False


s = Solution()

numCourses = 4
prerequisites = [[0,1],[1,2],[2,3]]

ans = s.canFinish(numCourses, prerequisites)
print("ans:", ans)