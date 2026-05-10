from typing import List

class Node:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []
    
    def __repr__(self):
        ans = ""
        ans += str(self.value)
        ans += "->"
        for pair in self.neighbors:
            node, value = pair
            ans += "(" + str(node.value) + "," + str(value) + "); "

        return ans
        

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        nodeMap = {}
        for index in range(0, len(equations)):
            equation = equations[index]
            ratio = values[index]

            numerator, denominator = equation

            if not(numerator in nodeMap):
                nodeMap[numerator] = Node(value=numerator)
            
            if not(denominator in nodeMap):
                nodeMap[denominator] = Node(value=denominator)
            
            numeratorNode = nodeMap[numerator]
            denominatorNode = nodeMap[denominator]

            normalPair = (denominatorNode, ratio)
            numeratorNode.neighbors.append(normalPair)

            inversePair = (numeratorNode, 1/ratio)
            denominatorNode.neighbors.append(inversePair)

        answers = [evaluateQuery(query, nodeMap) for query in queries]
        return answers

def evaluateQuery(query, nodeMap):
    numerator, denominator = query
    
    if (not(numerator) in nodeMap) or (not(denominator) in nodeMap):
        return -1.0

    seenBefore = set()
    pathProduct = findPath(nodeMap[numerator], nodeMap[denominator], seenBefore)
    if pathProduct:
        return pathProduct
    else:
        return -1.0

def findPath(startNode, endNode, seenBefore):
    if startNode == endNode:
        return 1
    
    seenBefore.add(startNode.value)

    for pair in startNode.neighbors:
        neighbor, edgeWeight = pair
        if not(neighbor.value) in seenBefore:
            remainingPath = findPath(neighbor, endNode, seenBefore)
            if remainingPath is not None:
                return edgeWeight * remainingPath
    
    return None

            




s = Solution()

# equations = [["a","b"],["b","c"]]
# values = [2.0,3.0]
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

equations = [["a","b"],["c","d"]]
values = [1.0,1.0]
queries = [["a","c"],["b","d"],["b","a"],["d","c"]]

ans = s.calcEquation(equations, values, queries)
print("ans:", ans)