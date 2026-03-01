from typing import List
from heapq import *

class Triplet():
    def __init__(self, p1, p2, d):
        self.p1 = p1
        self.p2 = p2
        self.d = d
    
    def __lt__(self, other):
        return self.d < other.d
    
    def __repr__(self):
        ans = "("
        ans += str(self.p1)
        ans += ","
        ans += str(self.p2)
        ans += ", "
        ans += str(self.d)
        ans += ")"
        return ans
    
    def __hash__(self):
        return hash(str(self.p1) + str(self.p2) + str(self.d))
    
        

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1-x2) + abs(y1-y2)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        pointsAsTuples = [tuple(p) for p in points]
        distancePairs = [Triplet(p1, p2, distance(p1, p2)) for p1 in pointsAsTuples for p2 in pointsAsTuples]
        actualPairs = list(filter(lambda T: T.d != 0, distancePairs))
        heapify(actualPairs)

        inTree = set([pointsAsTuples[0]])
        outOfTree = set(pointsAsTuples)
        outOfTree.remove(pointsAsTuples[0])


        # algorithm to compute MST:
        # find the smallest existing edge that connects the current tree 
        # to something that's not in the tree. 
        # then, add that edge to the tree. remove from the heap. etc... 
        # initially, all such edges are in the tree.
        # when we choose an initial node, then we have to.
        edges = set()
        while len(outOfTree) > 0:
            # point1, point2, dist = getShortestEdge(inTree, outOfTree, actualPairs)
            triplet = getShortestEdge(inTree, outOfTree, actualPairs)
            point1, point2, dist = triplet.p1, triplet.p2, triplet.d
            edges.add(triplet)
            inTree.add(point1)
            inTree.add(point2)
            if point1 in outOfTree:
                outOfTree.remove(point1)
            if point2 in outOfTree:
                outOfTree.remove(point2)
            
            # print("inTree:", inTree)
            # print("edges:", edges)


        ans = 0
        for triplet in edges:
            # print("edge:", tripl)
            ans += triplet.d
        # print("ans:", ans)
        return ans
            

def getShortestEdge(inTree, outOfTree, pairs):
    triplet = heappop(pairs)
    rejects = [triplet]
    # print("inTree:", inTree)
    # print("outOfTree:", outOfTree)
    # print("pairs:", pairs)
    
    while not(connectsToOutside(triplet, inTree, outOfTree)):
        triplet = heappop(pairs)
        rejects.append(triplet)
    
    for r in rejects:
        heappush(pairs, r)

    return triplet
    

    



def connectsToOutside(triplet, inTree, outOfTree):
    p1, p2 = triplet.p1, triplet.p2
    return (p1 in inTree) == (p2 in outOfTree)
        



points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
mySol = Solution()
mySol.minCostConnectPoints(points)