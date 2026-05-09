from typing import List

class Node:
    def __init__(self, value, neighbors = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        ans = ""
        ans += str(self.value)
        ans += "->"
        for n in self.neighbors:
            ans += str(n.value) + ","
        return ans

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        nodeMap = {}

        for i in range(0, n):
            newNode = Node(value=i)
            nodeMap[i] = newNode
        
        for e in edges:
            n1, n2 = e
            node1, node2 = nodeMap[n1], nodeMap[n2]

            node1.neighbors.append(node2)
            node2.neighbors.append(node1)

        for k,v in nodeMap.items():
            print(k, "|",v)
        
        memo = {}
        answer = []
        for i in range(0,n):
            node = nodeMap[i]
            sumOfDistances = calculateSumOfDistance(node, nodeMap, memo)
            answer.append(sumOfDistances)

        return answer

def calculateSumOfDistance(startingNode, nodeMap, memo):

    i = startingNode.value
    n = len(nodeMap)

    distancesFromI = 0

    for j in range(0, n):
        if i == j:
            continue

        destinationNode = nodeMap[j]
        # print("calculating distance from", i, "to", j)
        d = calculateDistance(startingNode, destinationNode, memo, seenBefore = set())
        # print("d from", i, "to", j, ":", d)
        # print("\n\n\n")
        distancesFromI += d

        
    return distancesFromI

def calculateDistance(startingNode, destinationNode, memo, seenBefore):
    # print("startingNode.value:   ", startingNode.value)
    # print("destinationNode.value:", destinationNode.value)
    # input("enter to continue")
    key = (startingNode.value, destinationNode.value)
    reverseKey = (destinationNode.value, startingNode.value)
    
    if startingNode == destinationNode:
        return 0

    seenBefore.add(startingNode.value)

    if key in memo:
        return memo[key]
    
    if reverseKey in memo:
        return memo[reverseKey]
    d = None
    for neighbor in startingNode.neighbors:
        if neighbor.value in seenBefore:
            # print("should be continuing..")
            continue


        recursiveCall = calculateDistance(neighbor, destinationNode, memo, seenBefore)
        if recursiveCall != float('inf'):
            memo[key] = 1 + recursiveCall
            memo[reverseKey] = 1 + recursiveCall
            return 1 + recursiveCall
            
    return float('inf')




s = Solution()

n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

answer = s.sumOfDistancesInTree(n, edges)
print("answer:", answer)