class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list)
        for s in strs:
            aux = s
            key = "".join(sorted(s))
            groups[key].append(aux)
        return list(groups.values())
