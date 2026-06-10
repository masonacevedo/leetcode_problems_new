class UnionFind:
    def __init__(self):
        self.parents = {}
        self.sizes = {}
    
    def add(self, x):
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
        if x == self.parents[y] or y == self.parents[x]:
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

nodes = ["a", "b", "c", "d"]

uf = UnionFind()
for node in nodes:
    uf.add(node)

assert(uf.setSize("a") == 1)
assert(uf.setSize("b") == 1)
assert(uf.setSize("c") == 1)
assert(uf.setSize("d") == 1)

assert(not(uf.sameSet("a", "b")))
assert(not(uf.sameSet("a", "c")))
assert(not(uf.sameSet("a", "d")))
assert(not(uf.sameSet("b", "c")))
assert(not(uf.sameSet("b", "d")))
assert(not(uf.sameSet("c", "d")))
uf.merge("a","b")
assert(uf.setSize("a") == 2)
assert(uf.setSize("b") == 2)
assert(uf.setSize("c") == 1)
assert(uf.setSize("d") == 1)

assert(uf.sameSet("a", "b"))
assert(not(uf.sameSet("a", "c")))
assert(not(uf.sameSet("a", "d")))
assert(not(uf.sameSet("b", "c")))
assert(not(uf.sameSet("b", "d")))
assert(not(uf.sameSet("c", "d")))

uf.merge("b", "c")

assert(uf.setSize("a") == 3)
assert(uf.setSize("b") == 3)
assert(uf.setSize("c") == 3)
assert(uf.setSize("d") == 1)

assert(uf.sameSet("a", "b"))
assert(uf.sameSet("a", "c"))
assert(not(uf.sameSet("a", "d")))
assert(uf.sameSet("b", "c"))
assert(not(uf.sameSet("b", "d")))
assert(not(uf.sameSet("c", "d")))

uf.merge("c", "d")

assert(uf.setSize("a") == 4)
assert(uf.setSize("b") == 4)
assert(uf.setSize("c") == 4)
assert(uf.setSize("d") == 4)

assert(uf.sameSet("a", "b"))
assert(uf.sameSet("a", "c"))
assert(uf.sameSet("a", "d"))
assert(uf.sameSet("b", "c"))
assert(uf.sameSet("b", "d"))
assert(uf.sameSet("c", "d"))

print("uf:", uf)
uf.merge("d", "a")