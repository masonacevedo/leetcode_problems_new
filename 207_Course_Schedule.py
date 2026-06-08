from typing import List
import copy

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}
        for i in range(0, numCourses):
            adjList[i] = []
        
        for pair in prerequisites:
            beforeCourse, afterCourse = pair
            adjList[beforeCourse].append(afterCourse)
        
        allOrderings = topSort(adjList)
        if len(allOrderings) == 0:
            return []
        return allOrderings[0]

def topSort(adjList):
    inDegreeMap = {node: 0 for node in adjList.keys()}

    for node, neighbors in adjList.items():
        for neighbor in neighbors:
            inDegreeMap[neighbor] += 1

    visited = set()
    
    orderings = topSortRecursive(inDegreeMap, adjList)
    return orderings

def topSortRecursive(inDegreeMap, adjList):
    if len(adjList) == 1:
        onlyKey = list(adjList.keys())[0]
        return [[onlyKey]]

    allOrderings = []
    for node, degree in inDegreeMap.items():
        if degree != 0:
            continue

        newAdjList = copy.deepcopy(adjList)
        newInDegreeMap = copy.deepcopy(inDegreeMap)

        for neighbor in newAdjList[node]:
            newInDegreeMap[neighbor] -= 1

        del newAdjList[node]
        del newInDegreeMap[node]
        recursiveResult = topSortRecursive(newInDegreeMap, newAdjList)

        for ordering in recursiveResult:
            ordering.append(node)
            allOrderings.append(ordering)

    return allOrderings

    
s = Solution()

numCourses = 4
prerequisites = [
    [2,1],
    [3,1],
    [1,0],
    

]
# prerequisites = [
#     [0,1],
#     [1,0]
# ]

# prerequisites = [[1,0],[1,2],[0,1]]

ans = s.findOrder(numCourses, prerequisites)
print("ans:", ans)