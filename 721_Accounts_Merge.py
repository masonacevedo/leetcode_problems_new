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

    def neighbors(self, x):
        root = self.find(x)
        return set([node for node in self.parents.keys() if self.find(node) == root])

    def subsets(self):
        return {node : self.neighbors(node) for node in self.parents.keys() if self.find(node) == node}

    def __repr__(self):
        return str(self.subsets())

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        uf = UnionFind()
        for account in accounts:
            name, *emails = account
            if len(emails) == 1:
                uf.add(emails[0])
                continue
    
            for email_i, email_j in zip(emails[0:-1], emails[1:]):
                
                uf.add(email_i)
                uf.add(email_j)

                uf.merge(email_i, email_j)
                    

        emailMap = {}
        for account in accounts:
            name, *emails = account
            for email in emails:
                if uf.find(email) in emailMap:
                    emailMap[uf.find(email)][1].add(email)
                else:
                    emailMap[uf.find(email)] = (name, set([email]))
        
        
        ans = []
        for k,v in emailMap.items():
            name, associatedEmails = v
            ans.append([name] + sorted(associatedEmails))
        return ans

                    




s = Solution()
accounts = [
    ["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
    ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],
    ["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
    ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],
    ["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]
]
ans = s.accountsMerge(accounts)

for a in ans:
    print(a)