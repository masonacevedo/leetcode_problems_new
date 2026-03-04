import random

class RandomizedSet:

    def __init__(self):
        self.array = []
        self.mapping = {}
        

    def insert(self, val: int) -> bool:
        if val in self.mapping:
            return False

        newIndex = len(self.array)
        self.mapping[val] = newIndex
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not(val in self.mapping):
            return False

        lastElement = self.array[-1]
        indexOfRemoved = self.mapping[val]
        self.array[indexOfRemoved] = lastElement
        self.mapping[lastElement] = indexOfRemoved
        self.array.pop()
        del self.mapping[val]
        return True
        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.mapping) - 1)
        return self.array[index]
    
    def __repr__(self):
        ans = "array:"
        ans += str(self.array)
        ans += "\n"
        ans += "mapping:"
        ans += str(self.mapping)
        ans += "\n"
        return ans
        


# Your RandomizedSet object will be instantiated and called as such:
# mySet = RandomizedSet()

# mySet.insert(10)
# print(mySet)

# mySet.insert(20)
# print(mySet)


# mySet.insert(30)
# print(mySet)

# mySet.insert(40)
# print(mySet)

# mySet.remove(20)
# print(mySet)

# mySet.insert(20)
# print(mySet)

# mySet.insert(50)
# print(mySet)

# mySet.remove(10)
# print(mySet)