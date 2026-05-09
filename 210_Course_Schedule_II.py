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
            toNodeVal, fromNodeVal = pair

            fromNode = nodeMap[fromNodeVal]
            toNode = nodeMap[toNodeVal]

            fromNode.neighbors.append(toNode)
        
        for k, v in nodeMap.items():
            print(k, "|", v)
        

        bestCourseOrdering = []
        for course in nodeMap.keys():
            
            startingNode = nodeMap[course]
            items = []
            result = topologicalSort(startingNode, set(), set(), items)
            print("result:", result)
            print("bestCourseOrdering:", bestCourseOrdering)
            if result:
                if len(result) > len(bestCourseOrdering):
                    bestCourseOrdering = result

        return list(reversed(bestCourseOrdering))        

def topologicalSort(startingNode, onCurrentPath, exploredAlready, items):
    
    # print('startingNode:', startingNode)
    if startingNode.value in onCurrentPath:
        return False
    
    if startingNode.value in exploredAlready:
        # print("getting here!!")
        return items
    
    onCurrentPath.add(startingNode.value)


    for neighbor in startingNode.neighbors:
        topologicalSort(neighbor, onCurrentPath, exploredAlready, items)
    
    onCurrentPath.remove(startingNode.value)
    exploredAlready.add(startingNode.value)


    items.append(startingNode.value)
    return items



# numCourses = 2
# prerequisites = [[1,0]]
# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
numCourses = 7
prerequisites = [
    [6,4],
    [5,4],
    [4,3],
    [4,2],
    [2,0],
    [3,1],

]
s = Solution()
ans = s.findOrder(numCourses, prerequisites)
print("ans:", ans)