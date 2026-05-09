from typing import List
import copy

class Node:
    def __init__(self, repKey, repVal, neighbors=None):
        self.repKey = repKey
        self.repVal = repVal

        self.neighbors = neighbors if neighbors is not None else []
    
    def __repr__(self):
        ans = ""
        ans += self.repKey
        ans += "->"

        for n in self.neighbors:
            ans += n.repKey + ","
        return ans

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        nodeMap = {}

        for index, pair in enumerate(replacements):
            repKey, repVal = pair
            newNode = Node(repKey, repVal)
            nodeMap[repKey] = newNode
        
        for rep1 in replacements:
            for rep2 in replacements:
                if rep1 == rep2:
                    continue
                
                rep1key, rep1val = rep1
                rep2key, rep2val = rep2

                if rep2key in rep1val:
                    rep1Node = nodeMap[rep1key]
                    rep2Node = nodeMap[rep2key]

                    rep2Node.neighbors.append(rep1Node)

        nodeList = topSortWrapper(nodeMap)
        # print("nodeList:", nodeList)
        # print()

        for nodeKey in nodeList:
            node = nodeMap[nodeKey]
            text = text.replace("%" + node.repKey + "%", node.repVal)
        return text

def topSortWrapper(nodeMap):

    items = []
    exploredAlready = set()

    for node in nodeMap.values():
        result = topSortRecursive(node, exploredAlready, onPath=set(), items=items)
        if not(result):
            raise Exception("Found a cycle! Not possible to perform replacement.")

    return items


def topSortRecursive(node, exploredAlready, onPath, items):
    if node.repKey in exploredAlready:
        return True
    
    if node.repKey in onPath:
        return False
    
    onPath.add(node.repKey)

    for neighbor in node.neighbors:
        if not(topSortRecursive(neighbor, exploredAlready, onPath, items)):
            return False
    
    onPath.remove(node.repKey)
    exploredAlready.add(node.repKey)
    items.append(node.repKey)
    return True

s = Solution()

replacements = [["A","bce"],["B","ace"],["C","abc%B%"]]
text = "%A%_%B%_%C%"

ans = s.applySubstitutions(replacements, text)
print("ans:", ans)