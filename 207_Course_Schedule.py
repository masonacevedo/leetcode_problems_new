from typing import List
from collections import deque

# idea: we bulid a directed graph based on the prerequisites. 
# If there are any cycles in the graph, we return true.
# Otherwise, we return false. 

class Node:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []
    
    def __repr__(self):
        ans = str(self.value)
        ans += " | ["
        for node in self.neighbors:
            ans += str(node.value) + ", "
        ans += "]"
        return ans

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        nodeMap = {}
        for courseNumber in range(0, numCourses):
            newNode = Node(value=courseNumber, neighbors=None)
            nodeMap[courseNumber] = newNode
        
        for prereq in prerequisites:
            courseNum1, courseNum2 = prereq
            node1 = nodeMap[courseNum1]
            node2 = nodeMap[courseNum2]

            node1.neighbors.append(node2)

        # seenBefore = set()
        for course in range(0, numCourses):
            # print("course:", course)

            startingNode = nodeMap[course]
            # print("startingNode:", startingNode)
            onCurrentPath = set()
            visitedBefore = set()
            if detectCycle(startingNode, onCurrentPath, visitedBefore):
                # print("cycle detected!")
                return False
            else:
                pass
                # print("cycle not detected")
            # print()
        
        return True
        
        
def detectCycle(startingNode, onCurrentPath, visitedBefore):

    if startingNode.value in visitedBefore:
        # if we've reached a node that we've already explored - no need to explore it again
        return False
    
    if startingNode.value in onCurrentPath:
        # if a starting node is in the current path, we've found a cycle! 
        return True
    
    onCurrentPath.add(startingNode.value)

    for neighbor in startingNode.neighbors:
        if detectCycle(neighbor, onCurrentPath, visitedBefore):
            return True
    
    onCurrentPath.remove(startingNode.value)
    visitedBefore.add(startingNode.value)

    return False
        

numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
# prerequisites = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
# prerequisites = [[0,1], [1,0]]

s = Solution()
ans = s.canFinish(numCourses, prerequisites)

print("ans:", ans)