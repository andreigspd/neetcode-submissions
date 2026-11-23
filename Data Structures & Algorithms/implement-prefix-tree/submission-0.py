class PrefixTree:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.end_word = False
            self.prefix_count = 0
    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = self.TrieNode()
            curr = curr.children[char]
            curr.prefix_count += 1
        curr.end_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        