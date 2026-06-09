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
        
        
        return not(hasCycle(inDegrees, adjList))
    
def hasCycle(inDegrees, adjList):
    
    # algorithm: identify a node w/ inDegree 0. 
    #           while there remains nodes of length 0:
    #               pop a node off the queue.
    #               add it to the answer.
    #               remove it from the graph.
    #               if any other nodes have inDegree 0,
    #               add them to the queue. 
    #               keep a set of nodes we've visited, and if we visit the same node twice, 

    queue = deque([])
    for node, inDegree in inDegrees.items():
        if inDegree == 0:
            queue.append(node)
    
    if len(queue) == 0:
        return True
    
    processed = 0
    while len(queue) > 0:
        currentNode = queue.popleft()
        for neighbor in adjList[currentNode]:
            inDegrees[neighbor] -= 1
            if inDegrees[neighbor] == 0:
                queue.append(neighbor)
        processed += 1

    # print("processed:", processed)
    # print("len(adjList):", len(adjList))
    return processed != len(adjList)        
    

        

s = Solution()

numCourses = 6
prerequisites = [[0,1],[1,2],[2,3], [3,4], [4,5], [5,3]]

ans = s.canFinish(numCourses, prerequisites)
print("ans:", ans)