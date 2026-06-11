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

        i = 0
        currentNode = self.root
        while i < len(word):
            char = word[i]
            availableChars = [c.value for c in currentNode.children]
            if char not in availableChars:
                break

            nextChildIndex = availableChars.index(char)
            currentNode = currentNode.children[nextChildIndex]

            i += 1

        if i == len(word):
            currentNode.isFinal = True
            return

        prevNode = Node(value = word[i], isFinal = False)
        self.root = Node(value="*", isFinal = False, children = [prevNode])
        for char in word[i+1:]:
            prevNode = self._procesChar(char, prevNode)

        prevNode.isFinal = True
        


    def _procesChar(self, char, parentNode):
        newNode = Node(char, isFinal = False)
        parentNode.children.append(newNode)
        return newNode
        

    def search(self, word: str) -> bool:
        # pass
        i = 0
        currentNode = self.root
        while i < len(word):
            char = word[i]
            availableChars = [c.value for c in currentNode.children]
            if char not in availableChars:
                return False

            nextChildIndex = availableChars.index(char)
            currentNode = currentNode.children[nextChildIndex]

            i += 1
        return currentNode.isFinal

        

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

assert(trie.search("apple"))
assert(not(trie.search("app")))
assert(trie.startsWith("app"))
trie.insert("app")
assert(trie.search("app"))
