class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.end_word = False
    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = self.TrieNode()
            curr = curr.children[char]
        curr.end_word = True

    def search(self, word: str) -> bool:
        def dfs(level, root):
            curr = root
            for i in range(level, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.end_word
        return dfs(0, self.root)

            
