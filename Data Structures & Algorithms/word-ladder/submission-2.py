class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        if beginWord in words:
            words.remove(beginWord)

        from collections import deque
        q = deque()
        q.append((beginWord, 1))

        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                original_letter = word[i]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original_letter:
                        continue
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in words:
                        words.remove(new_word)
                        q.append((new_word, level + 1))
        return 0
