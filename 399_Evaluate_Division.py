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
    # to evaluate query, we should find a path if it exists,
    # then follow the edges and compute the product along those edges.
    # print("query:", query)
    numerator, denominator = query
    
    if (not(numerator) in nodeMap) or (not(denominator) in nodeMap):
        return -1.0
    # input("")
    seenBefore = set()
    path = findPath(nodeMap[numerator], nodeMap[denominator], seenBefore)
    

    product = 1
    # TODO: TRAVERSE PATH AND COMPUTE PRODUCT! 

    return product

def findPath(startNode, endNode, seenBefore):
    if startNode == endNode:
        return [startNode]
    
    seenBefore.add(startNode.value)

    for pair in startNode.neighbors:
        neighbor, edgeWeight = pair
        if not(neighbor.value) in seenBefore:
            remainingPath = findPath(neighbor, endNode, seenBefore)
            if remainingPath is not None:
                return [startNode] + remainingPath
    
    return None

            




s = Solution()

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

ans = s.calcEquation(equations, values, queries)
print("ans:", ans)