from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        
        # 1. Dacă endWord nu e în listă, drumul este imposibil
        if endWord not in words:
            return 0
        
        # Dacă beginWord este în set, îl scoatem pentru a nu ne întoarce la el
        if beginWord in words:
            words.remove(beginWord)

        # Coada ține perechi de (cuvânt_curent, nivel/lungime_lanț)
        q = deque([(beginWord, 1)])

        while q:
            current_word, level = q.popleft()

            # Dacă am ajuns la cuvântul destinație
            if current_word == endWord:
                return level

            # Încercăm să înlocuim fiecare literă cu literele 'a' - 'z'
            for i in range(len(current_word)):
                original_char = current_word[i]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original_char:
                        continue
                    
                    next_word = current_word[:i] + c + current_word[i+1:]

                    if next_word in words:
                        words.remove(next_word)  # Marcare ca vizitat în O(1)
                        q.append((next_word, level + 1))

        return 0