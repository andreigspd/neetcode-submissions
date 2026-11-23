class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode():
            def __init__(self):
                self.children = {}
                self.end_word = False
                self.word = ""
        class Trie():
            def __init__(self):
                self.root = TrieNode()
            def add_word(self, word):
                curr = self.root
                for char in word:
                    if char not in curr.children:
                        curr.children[char] = TrieNode()
                    curr = curr.children[char]
                curr.end_word = True
                curr.word = word
        words_trie = Trie()
        for word in words:
            words_trie.add_word(word)
        
        n = len(board)
        m = len(board[0])
        used = set()
        ans = []
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j, curr):
            char = board[i][j]
            if char not in curr.children:
                return
            curr = curr.children[char]
            if curr.end_word == True:
                curr.end_word = False
                ans.append(curr.word)
            used.add((i, j))
            for di, dj in dir:
                i_new, j_new = i + di, j + dj
                if (i_new >= 0 and i_new < n and j_new >= 0 and j_new < m) and (i_new, j_new) not in used:
                    dfs(i_new, j_new, curr)
            used.remove((i, j))

        for i in range(n):
            for j in range(m):
                used.clear()
                dfs(i, j, words_trie.root)

        return ans
