from typing import List

class Node:
    def __init__(self, value, neighbors=None):
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
    def alienOrder(self, words: List[str]) -> str:
        try:
            edgeSet = calcEdges(words)
        except:
            return ""        
        nodeMap = buildNodes(words)

        for edge in edgeSet:
            letter1, letter2 = edge
            
            if not(letter1 in nodeMap):
                newNode = Node(value=letter1)
                nodeMap[letter1] = newNode
            
            if not(letter2 in nodeMap):
                newNode = Node(value=letter2)
                nodeMap[letter2] = newNode
            
            node1 = nodeMap[letter1]
            node2 = nodeMap[letter2]

            node2.neighbors.append(node1)

        sortedList = topologicalSort(nodeMap)

        if not(sortedList):
            return ""
        else:
            return "".join(sortedList)

def buildNodes(words):
    nodeMap = {}
    for word in words:
        for char in word:
            if not(char in nodeMap):
                nodeMap[char] = Node(value=char)
    return nodeMap

def topologicalSort(nodeMap):
    items = []
    exploredAlready = set()

    for letter, currentNode in nodeMap.items():
        result = topSortRecursive(currentNode, currentPath=set(), exploredAlready=exploredAlready, items=items)
        if not(result):
            return None
    
    return items


def topSortRecursive(currentNode, currentPath, exploredAlready, items):

    if currentNode.value in currentPath:
        return False
    
    if currentNode.value in exploredAlready:
        return True
    
    currentPath.add(currentNode.value)

    for neighbor in currentNode.neighbors:
        result = topSortRecursive(neighbor, currentPath, exploredAlready, items)
        if not(result):
            return False
    
    currentPath.remove(currentNode.value)
    exploredAlready.add(currentNode.value)
    items.append(currentNode.value)

    return True

def calcEdges(words):
    edges = set()
    for i in range(0, len(words)):
        for j in range(i+1, len(words)):

            word_i = words[i]
            word_j = words[j]
            if word_i == word_j:
                continue
            newEdge = computeEdge(word_i, word_j)
            if newEdge is not None:
                edges.add(newEdge)

    return edges

def computeEdge(beforeWord, afterWord):
    beforePointer = 0
    afterPointer = 0
    

    while (beforePointer < len(beforeWord)) and (afterPointer < len(afterWord)):
        beforeLetter = beforeWord[beforePointer]
        afterLetter = afterWord[afterPointer]

        if beforeLetter == afterLetter:
            beforePointer += 1
            afterPointer += 1
        else:
            return (beforeLetter, afterLetter)
    
    if len(afterWord) < len(beforeWord):
        raise Exception("Word ordering in dictionary is invalid!")
    else:
        return None





s = Solution()
# words = ["wrt","wrf","er","ett","rftt"]
# words = ["z", "x", "z"]
# words = ["wrt","wrtkj"]
words = ["bc","b","cbc"]

ans = s.alienOrder(words)
print("ans:", ans)