
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __repr__(self):
        ans = str(self.val)
        ans += "| ["
        for n in self.neighbors:
            ans += str(n.val)
            ans += ", "

        ans += "]"
        return ans

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        # copyOfNode = Node(val = node.val, neighbors=None)
        queue = deque([node])
        seen_before = set([node.val])
        
        firstTime = True

        nodeMap = {}
        edge_list = []
        while len(queue) > 0:


            currentNode = queue.popleft()
            # print("currentNode:", currentNode)
            # input("enter to con")
            neighbors = currentNode.neighbors

            copyOfNode = Node(val = currentNode.val, neighbors=None)
            nodeMap[currentNode.val] = copyOfNode

            for neighbor in neighbors:
                if not(neighbor.val in seen_before):
                    queue.append(neighbor)
                    seen_before.add(neighbor.val)
                edge = (currentNode.val, neighbor.val)
                edge_list.append(edge)

            
            if firstTime:
                answerNode = copyOfNode
            firstTime = False
        
        print('edge_list:', edge_list)
        for edge in edge_list:
            (node1Val, node2Val) = edge

            node1 = nodeMap[node1Val]
            node2 = nodeMap[node2Val]

            node1.neighbors.append(node2)
            # node2.neighbors.append(node1)
        
        return answerNode


        


Node1 = Node(val = 1)
Node2 = Node(val = 2)
Node3 = Node(val = 3)
Node4 = Node(val = 4)

Node1.neighbors = [Node2, Node4]
Node2.neighbors = [Node1, Node3]
Node3.neighbors = [Node2, Node4]
Node4.neighbors = [Node1, Node3]

s = Solution()
ans = s.cloneGraph(Node1)
print("ans:", ans)