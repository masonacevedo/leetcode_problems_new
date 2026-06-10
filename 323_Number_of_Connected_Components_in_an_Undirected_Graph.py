from typing import List
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.sizes = {}
    
    def add(self, x):
        if x in self.parents:
            return
        self.parents[x] = None
        self.sizes[x] = 1
    
    def find(self, x):
        currentNode = x
        nodesSeen = []
        while self.parents[currentNode] is not None:
            nodesSeen.append(currentNode)
            currentNode = self.parents[currentNode]
        
        for node in nodesSeen:
            self.parents[node] = currentNode
        return currentNode
    
    def setSize(self, x):
        return self.sizes[self.find(x)]

    def merge(self, x, y):
        if not(x in self.parents and y in self.parents):
            raise Exception(f"One of {x} and {y} is not in the data structure!")

        if self.find(x) == self.find(y):
            return

        root_x = self.find(x)
        root_y = self.find(y)

        if self.sizes[root_x] > self.sizes[root_y]:
            bigger, smaller = root_x, root_y
        else:
            bigger, smaller = root_y, root_x
        
        self.parents[smaller] = bigger
        self.sizes[bigger] += self.sizes[smaller]
    
    def sameSet(self, x, y):
        return self.find(x) == self.find(y)

    def __repr__(self):
        return str(self.parents) + "\n" + str(self.sizes)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()
        nodes = set(range(0, n))
        for node in nodes:
            uf.add(node)
        for edge in edges:
            x,y = edge
            uf.merge(x,y)
        
        uniqueComponents = set()
        for node in nodes:
            uniqueComponents.add(uf.find(node))
        return len(uniqueComponents)



s = Solution()

n = 4
edges = [[2,3],[1,2],[1,3]]

ans = s.countComponents(n, edges)
print("ans:", ans)