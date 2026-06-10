class UnionFind:
    def __init__(self):
        self.parents = {}
    
    def add(self, x):
        self.parents[x] = None
    
    def find(self, x):
        currentNode = x
        while self.parents[currentNode] is not None:
            currentNode = self.parents[currentNode]
        return currentNode
    
    def merge(self, x, y):
        if not(x in self.parents and y in self.parents):
            raise Exception(f"One of {x} and {y} is not in the data structure!")
        root_x = self.find(x)
        root_y = self.find(y)

        self.parents[root_x] = root_y
    
    def sameSet(self, x, y):
        return self.find(x) == self.find(y)    
    
    def __repr__(self):
        return str(self.parents)

nodes = ["a", "b", "c", "d"]

uf = UnionFind()
for node in nodes:
    uf.add(node)

assert(not(uf.sameSet("a", "b")))
assert(not(uf.sameSet("a", "c")))
assert(not(uf.sameSet("a", "d")))
assert(not(uf.sameSet("b", "c")))
assert(not(uf.sameSet("b", "d")))
assert(not(uf.sameSet("c", "d")))

uf.merge("a","b")
assert(uf.sameSet("a", "b"))
assert(not(uf.sameSet("a", "c")))
assert(not(uf.sameSet("a", "d")))
assert(not(uf.sameSet("b", "c")))
assert(not(uf.sameSet("b", "d")))
assert(not(uf.sameSet("c", "d")))

uf.merge("b", "c")
assert(uf.sameSet("a", "b"))
assert(uf.sameSet("a", "c"))
assert(not(uf.sameSet("a", "d")))
assert(uf.sameSet("b", "c"))
assert(not(uf.sameSet("b", "d")))
assert(not(uf.sameSet("c", "d")))

uf.merge("c", "d")

assert(uf.sameSet("a", "b"))
assert(uf.sameSet("a", "c"))
assert(uf.sameSet("a", "d"))
assert(uf.sameSet("b", "c"))
assert(uf.sameSet("b", "d"))
assert(uf.sameSet("c", "d"))

print(uf)