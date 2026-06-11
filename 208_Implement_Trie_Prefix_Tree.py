class Node:
    def __init__(self, value, isFinal, children=None):
        self.value = value
        self.isFinal = isFinal
        if children:
            self.children = children
        else:
            self.children = []

    def __repr__(self):
        ans = ""
        ans += str(self.value) + "|\n"
        ans += str(self.isFinal) + "|\n"
        ans += "["
        for c in self.children:
            ans += str(c.value) + ","
        ans += "]"
        return ans

class Trie:

    def __init__(self):
        self.root = Node(value = "*", isFinal = False)
        

    def insert(self, word: str) -> None:
        # print("begin insert")
        # breakpoint()

        lastNode, i = self._navigate(word)

        if i == len(word):
            lastNode.isFinal = True
            return
        
        prevNode = Node(value = word[i], isFinal = False)
        lastNode.children.append(prevNode)
        # breakpoint()
        for char in word[i+1:]:
            prevNode = self._procesChar(char, prevNode)

        prevNode.isFinal = True
        
    def _navigate(self, word):
        # print("beging navigate")
        # breakpoint()
        i = 0
        currentNode = self.root
        while i < len(word):
            char = word[i]
            availableChars = [c.value for c in currentNode.children]
            if char not in availableChars:
                # print("end navigate")
                # breakpoint()
                return currentNode, i

            nextChildIndex = availableChars.index(char)
            currentNode = currentNode.children[nextChildIndex]

            i += 1
        # print("end neavigate")
        # breakpoint()
        return currentNode, i

    def _procesChar(self, char, parentNode):
        newNode = Node(char, isFinal = False)
        parentNode.children.append(newNode)
        return newNode
        

    def search(self, word: str) -> bool:
        lastNode, _ = self._navigate(word)
        return lastNode.isFinal

        

    def startsWith(self, prefix: str) -> bool:
        i = 0
        currentNode = self.root
        while i < len(prefix):
            char = prefix[i]
            availableChars = [c.value for c in currentNode.children]
            if char not in availableChars:
                return False

            nextChildIndex = availableChars.index(char)
            currentNode = currentNode.children[nextChildIndex]

            i += 1
        return True



# Your Trie object will be instantiated and called as such:

trie = Trie()
trie.insert("apple")
trie.insert("applexyz")

assert(trie.search("apple"))
assert(not(trie.search("app")))
assert(trie.startsWith("app"))
trie.insert("app")
assert(trie.search("app"))


trie = Trie()

commands = ["Trie","insert","search","search","startsWith","startsWith","insert","search","startsWith","insert","search","startsWith"]
inputs = [[],["ab"],["abc"],["ab"],["abc"],["ab"],["ab"],["abc"],["abc"],["abc"],["abc"],["abc"]]

for command, argument in zip(commands[1:], inputs[1:]):
    if command == "insert":
        # print(f"inserting {argument[0]}")
        trie.insert(argument[0])

assert(trie.search("abc"))
assert(trie.startsWith("abc"))