class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        from collections import defaultdict
        groups = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            groups[sorted_word].append(word)
        result = []
        for group in groups.values():
            result.append(group)
        return result
