from typing import List
from heapq import heapify, heappush, heappop

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

    def neighbors(self, x):
        root = self.find(x)
        return set([node for node in self.parents.keys() if self.find(node) == root])

    def subsets(self):
        return {node : self.neighbors(node) for node in self.parents.keys() if self.find(node) == node}

    def __repr__(self):
        return str(self.subsets())

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pairs = []

        uf = UnionFind()
        for i in range(0, len(points)):
            uf.add(tuple(points[i]))
            for j in range(i+1, len(points)):
                d = manhattanDistance(points[i], points[j])
                pairs.append((d, tuple(points[i]), tuple(points[j])))
        
        heapify(pairs)
        totalDistance = 0
        mergeCount = 0
        while len(pairs) > 0:
            distance, point_i, point_j = heappop(pairs)
            if uf.find(point_i) == uf.find(point_j):
                continue
            totalDistance += distance
            mergeCount += 1
            uf.merge(point_i, point_j)
            if mergeCount == len(points):
                break
        return totalDistance

        
def manhattanDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1-x2) + abs(y1-y2))


points = [[3,12],[-2,5],[-4,1]]
mySol = Solution()
ans = mySol.minCostConnectPoints(points)
print("ans:", ans)