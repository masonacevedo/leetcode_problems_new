from typing import List

class Node:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = [] if neighbors is None else neighbors
        # if neighbors is None:
        #     self.neighbors = []
        # else:
        #     self.neighbors = neighbors
    
    def __repr__(self):
        ans = str(self.value)
        ans += " -> "
        for neighbor in self.neighbors:
            ans += str(neighbor.value)
            ans += ","
        return ans

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        nodeMap = {}
        for i in range(0, numCourses):
            newNode = Node(value = i)
            nodeMap[i] = newNode
        
        for pair in prerequisites:
            fromNodeVal, toNodeVal = pair

            fromNode = nodeMap[fromNodeVal]
            toNode = nodeMap[toNodeVal]

            fromNode.neighbors.append(toNode)
        
        bestCourseOrdering = []
        exploredAlready = set()
        items = []
        for course in nodeMap.keys():
            
            startingNode = nodeMap[course]
            result = topologicalSort(startingNode, set(), exploredAlready, items)
            
            if not(result):
                return []

        return items

def topologicalSort(startingNode, onCurrentPath, exploredAlready, items):
    
    if startingNode.value in onCurrentPath:
        return False
    
    if startingNode.value in exploredAlready:
        return True
    
    onCurrentPath.add(startingNode.value)


    for neighbor in startingNode.neighbors:
        if topologicalSort(neighbor, onCurrentPath, exploredAlready, items) == False:
            return False
    
    onCurrentPath.remove(startingNode.value)
    exploredAlready.add(startingNode.value)

    items.append(startingNode.value)
    return True



# numCourses = 2
# prerequisites = [[1,0]]
# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
numCourses = 7
# numCourses = 2
prerequisites = [
    [6,4],
    [5,4],
    [4,3],
    [4,2],
    [2,0],
    [3,1],
]

# prerequisites = [
#     [0,2],
#     [1,2],
#     [2,3],
#     [2,4],
#     [3,5],
#     [4,6],
# ]

# prerequisites = [
#     [0,1],
#     [1,0]
# ]

s = Solution()
ans = s.findOrder(numCourses, prerequisites)
print("ans:", ans)