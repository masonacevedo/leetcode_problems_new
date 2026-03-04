class Node:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

    def __repr__(self):
        ans = "[Node | "
        ans += str(self.key)
        ans += " | "
        ans += str(self.value)
        if self.nxt:
            ans += " next: " + str(self.nxt.key)
        else:
            ans += " next: none"
        ans += " | "

        if self.prev:
            ans += "prev: " + str(self.prev.key)
        else:
            ans += "prev: none"
        ans += "]"
        return ans
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.tail = None
        self.head = None

    def moveToFront(self, node):

        if node == self.head:
            return
        elif node == self.tail:
            # print("moving tail to front")
            # print("node:", node)
            # print("self.head:", self.head)
            # print("self.tail:", self.tail)
            # print("self.mapping:", self.mapping)
            # print("node.prev:", node.prev)
            # print("node.nxt:", node.nxt)
            # input()
            self.head.nxt = node
            self.tail = node.nxt
            
            self.tail.prev = None
            node.nxt = None
            node.prev = self.head
            self.head = node
        else:
            self.head.nxt = node
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            node.prev = self.head
            node.nxt = None
            self.head = node

    def get(self, key: int) -> int:
        if not(key) in self.mapping:
            return -1
        fetchedNode = self.mapping[key]
        fetchedValue = fetchedNode.value

        # now, need to move this node to front.
        self.moveToFront(fetchedNode)
        return fetchedValue
        

    def put(self, key: int, value: int) -> None:
        
        if len(self.mapping) == 0:
            newNode = Node(key, value, nxt=None, prev=None)
            self.head = newNode
            self.tail = newNode
            self.mapping[key] = newNode
            return
        


        if key in self.mapping:
            fetchedNode = self.mapping[key]
            fetchedNode.value = value
        # elif len(self.mapping) == 1:
        #     newNode = Node(key, value, prev = self.head, nxt = None)
        #     oldNode = self.head
        #     self.head.nxt = newNode
        #     self.head = newNode
        #     self.tail = oldNode
        #     self.tail.nxt = self.head
        #     fetchedNode = newNode
        #     self.mapping[key] = newNode
        #     # print("printing self")
        #     # print(self)
        #     # print("done with self")
        #     # input()
        else:
            newNode = Node(key, value, prev = self.head, nxt = None)
            self.head.nxt = newNode
            self.head = newNode
            fetchedNode = newNode
            self.mapping[key] = newNode

        self.moveToFront(fetchedNode)
        
        if len(self.mapping) > self.capacity:
            self.__evict__()
    
    def __evict__(self):
        evictedNode = self.tail
        self.tail = evictedNode.nxt
        self.tail.prev = None
        del self.mapping[evictedNode.key]
    
    def __repr__(self):

        ans = "head\n"
        curNode = self.head
        while curNode:
            ans += str(curNode)
            ans += "\n"
            curNode = curNode.prev
        ans += "\ntail\nmapping\n"
        ans += str(self.mapping)
        ans += "\n"
        return ans


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

myCache = LRUCache(4)
print(myCache)
print()
myCache.put(20, 1)
print(myCache)
myCache.put(40, 2)
print(myCache)
myCache.put(60, 3)
print(myCache)
myCache.put(80, 4)
print(myCache)
myCache.put(100, 5)
print(myCache)

ans = myCache.get(20)
print(myCache)

assert(myCache.get(20) == -1)
assert(myCache.get(40) == 2)
print(myCache)
myCache.put(120, 6)
print(myCache)
assert(myCache.get(60) == -1)
print(myCache)

assert(myCache.get(40) == 2)
print(myCache)
assert(myCache.get(80) == 4)

print(myCache)
assert(myCache.get(100) == 5)
assert(myCache.get(120) == 6)

print(myCache)
myCache.put(80, 7)
print(myCache)